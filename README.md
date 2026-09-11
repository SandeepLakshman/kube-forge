# KubeForge

KubeForge is a containerized Flask application deployed and managed using Kubernetes.

## Tech Stack

- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- Helm

## Kubernetes Features

- Namespace isolation
- Deployment with multiple replicas
- Service exposure
- ConfigMap configuration
- Kubernetes Secret
- Scaling
- Rolling updates
- Rollbacks
- Ingress

## Application

The application exposes:

- `/` - KubeForge application
- `/health` - Health check endpoint

## Kubernetes Deployment

```bash
kubectl apply -f k8s/

## Hands-on Activity

- Deployed KubeForge using Kubernetes Deployment
- Configured 3 replicas and scaled the application
- Performed rolling update and rollback
- Exposed the application using a Kubernetes Service
