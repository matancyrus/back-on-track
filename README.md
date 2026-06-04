# back-on-track

A portfolio project that demonstrates how to build, containerize, and deploy a simple FastAPI application with Redis on Kubernetes.

## Overview

This project is a small API built with FastAPI that stores and retrieves key-value data from Redis.

It was created to practice and demonstrate:

- Python backend basics with FastAPI
- Redis integration
- Docker image creation with a custom Dockerfile
- Kubernetes Deployments and Services
- ConfigMaps and Secrets
- Liveness and Readiness probes
- Local Kubernetes testing with a cluster environment

## Architecture

The application consists of:

- **FastAPI app** – exposes HTTP endpoints
- **Redis** – stores key-value data
- **Docker** – packages the application into a container image
- **Kubernetes** – runs and manages the app and Redis as workloads

## Endpoints

- `GET /`  
  Returns a basic welcome message

- `GET /health`  
  Health check endpoint used by Kubernetes probes

- `POST /set?key=<key>&value=<value>`  
  Stores a value in Redis

- `GET /get/{key}`  
  Retrieves a value from Redis by key

## Project Structure

```text
back-on-track/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── k8s/
│   ├── namespace.yaml
│   ├── app-deployment.yaml
│   ├── app-service.yaml
│   ├── redis-deployment.yaml
│   ├── redis-service.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   └── ingress.yaml
└── README.md
