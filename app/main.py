from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import redis
import os
from prometheus_client import Counter, CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST


# Create a custom registry
registry = CollectorRegistry()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def get_redis_client():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/")
def root():
    try:
        r = get_redis_client()
        r.ping()    
        return {"message": "FastAPI + Redis app is running"}
    except Exception as e:        
        return {"message": "FastAPI app is running, but Redis connection failed", "error": str(e)}


@app.get("/health") 
def health():
    try:
        r = get_redis_client()
        r.ping()
        return {"status": "ok", "redis": "Connected"}
    except Exception as e:
        return {"status": "degraded", "redis": "not connected", "error": str(e)}

@app.post("/set")
def set_value(key: str, value: str):
    try:
        r = get_redis_client()
        r.set(key, value)
        return {"message": f"Stored {key}={value}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get/{key}")
def get_value(key: str):
    try:
        r = get_redis_client()
        value = r.get(key)
        if value is None:
            raise HTTPException(status_code=404, detail="Key not found")
        return {"key": key, "value": value}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/del/{key}")
def del_value(key: str):
    try:
        r = get_redis_client()
        value = r.get(key)
        if value is None:
            raise HTTPException(status_code=404, detail="Key not found")
        r.delete(key)
        print("hey")
        return {f"The key '{key}' has been deleted"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/metrics")
def metrics():
    """ Exposes application metrics in a Prometheus-compatible format. """
    return generate_latest(registry), 200, {'Content-Type': CONTENT_TYPE_LATEST}


# Metrics:
# Create a counter metric
http_requests_total = Counter(
    "http_requests_total",
    "Total number of HTTP requests received",
    ["status", "path", "method"],
    registry=registry,
)

@app.middleware("http")
async def after_request(request, call_next):
    response = await call_next(request)

    http_requests_total.labels(
        status=str(response.status_code),
        path=request.url.path,
        method=request.method,
    ).inc()

    return response