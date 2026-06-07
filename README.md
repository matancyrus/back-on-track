# Back On Track

Back On Track is a small full-stack snippet board project built to practice real-world application deployment and DevOps workflow.

The project includes a Python backend, a Redis datastore, a static frontend served by Nginx, Docker images for each service, Docker Compose for local multi-service testing, and Kubernetes manifests for deployment.

## Project Goal

The goal of this project was to build something small but complete.

Instead of creating only backend code or only Kubernetes YAMLs, I wanted to build a working application that includes:

- frontend and backend separation
- containerization
- reverse proxying with Nginx
- Redis integration
- Docker Compose for local development
- Kubernetes deployment manifests
- CI/CD practice with Jenkins

---

## Tech Stack

### Backend
- Python
- FastAPI
- Redis

### Frontend
- HTML
- CSS
- JavaScript
- Nginx

### DevOps / Infrastructure
- Docker
- Docker Compose
- Kubernetes
- Jenkins

---

## Features

- Save a snippet by key
- Retrieve a snippet by key
- Show Redis/backend health status in the UI
- Frontend communicates with backend through Nginx `/api` proxying
- Separate frontend and backend services
- Local multi-service development with Docker Compose
- Kubernetes manifests for frontend, backend, Redis, and ConfigMaps

---

## Architecture

The application is split into three main components:

### Frontend
A static frontend built with HTML, CSS, and vanilla JavaScript.  
It is served by Nginx and sends API requests through `/api/...`.

### Backend
A FastAPI application that handles snippet creation, retrieval, and health checks.

### Redis
Redis stores snippet data and supports the backend.

### Request Flow

1. User opens the frontend in the browser
2. Nginx serves the static frontend files
3. Frontend JavaScript sends requests to `/api/...`
4. Nginx proxies those requests to the FastAPI backend
5. FastAPI reads from or writes to Redis
6. Response is returned to the frontend and displayed to the user

---

## Project Structure

```text
back-on-track/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── nginx.conf
│   ├── script.js
│   └── style.css
├── jenkins/
│   └── Jenkinsfile
├── k8s/
│   ├── api/
│   │   ├── api-configmap.yaml
│   │   ├── api-deployment.yaml
│   │   ├── api-service.yaml
│   │   ├── redis-service.yaml
│   │   └── redis.yaml
│   └── frontend/
│       ├── app-configmap.yaml
│       ├── app-deployment.yaml
│       └── app-service.yaml
├── .gitignore
└── docker-compose.yml