# API Hosting - Flask + MySQL (Dockerized & Kubernetes)

This repository provides a lightweight Flask-based API that connects to an RDS MySQL database and serves plan details. The API is containerized with Docker for easy deployment and is designed to be deployed on AWS EC2 and Kubernetes (EKS). This documentation provides a complete breakdown of the entire workflow from local development to cloud deployment.

## Features

 - REST API built with Flask
 - Connects to MySQL database (RDS)
 - Containerized using Docker
 - Hosted locally and on EC2
 - Kubernetes Deployment with ConfigMaps & Secrets
 - Pushed to Docker Hub & deployed on AWS EKS
 - Scalable and production-ready setup
 - IAM roles & policies for secure access
 - Kubernetes services for load balancing

## Project Overview

 - Developing the Flask API – Creating an API that interacts with an RDS MySQL database.
 - Local Hosting & Testing – Running the API locally using Python.
 - Dockerizing the API – Creating a Docker image and running the container locally.
 - Pushing to Docker Hub – Storing the Docker image in a cloud repository.
 - Deploying on AWS EC2 – Running the containerized API on an EC2 instance.
 - Deploying on AWS EKS – Running the API in a managed Kubernetes cluster.
 - Using ConfigMaps & Secrets – Managing environment variables securely in Kubernetes.
 - Creating IAM Roles & Policies – Granting secure permissions to the cluster.
 - Using Kubernetes Services – Exposing the API externally.

## Running the API Locally
### Prerequisites

 - Python 3.x
 - Flask & dependencies installed using:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```
 - Run the API locally:
    ```bash
    python python_file.py
    ```
 - The API will be accessible at: `http://127.0.0.1:5000`

## Running with Docker

 - Pull the Docker Image
    ```bash
    docker pull joshmajoby/api-host-app:latest
    ```
 - Run the Container Locally
    ```bash
    docker run -p 8080:8080 -d joshmajoby/api-host-app
    ```    
 - The API will be available at: `http://localhost:8080`
 - Check out my Docker Hub Repository for the image: `https://hub.docker.com/r/joshmajoby/api-host-app`

## Hosting on EC2
 
 - Install Docker in a public EC2 instance
 - Pull the image from Docker Hub
 - Run it as a container
 - API available at `http://<EC2_public_ip>:8080`


## IAM User, Roles and Policies for AWS EKS

### **EKS Cluster IAM Role**
 Attach these policies:
 - `AmazonEKSClusterPolicy`
 - `AmazonEKSServicePolicy`

### **EKS Node IAM Role**
 Attach these policies:
 - `AmazonEKSWorkerNodePolicy`
 - `AmazonEC2ContainerRegistryReadOnly`
 - `AmazonEKS_CNI_Policy`

### **IAM User Access Configuration**
 Attach these policies:
 - `AdministratorAccess`
 - `AmazonEKSClusterPolicy`
 - `AmazonEKSAdminPolicy`
 - `AmazonEc2FullAccess`

## Deploying on AWS EKS

For deploying in AWS EKS, the following steps were completed:
 - Created a ConfigMap to store non-sensitive environment variables.
 - Created a Secret to securely store database credentials.
 - Deployed the API using Kubernetes Deployment.
 - Exposed the API using a Kubernetes Service to make it accessible externally.
All configuration files (`deployment.yaml`, `service.yaml`, `configmap.yaml`, `secret.yaml`) are located in the `k8s-manifests/` directory.

## Database Schema

The API is built to interact with a MySQL database that contains the `plans` table. Below is the schema for the table that the API uses:

### **SQL Schema for `plans` Table**:

```sql
CREATE TABLE IF NOT EXISTS plans (
    category VARCHAR(100),              -- Business Service Category
    plans VARCHAR(100),                 -- Specific plan name
    created_by VARCHAR(100),            -- Username of creator
    created_date TIMESTAMP,             -- Time of creation
    last_update_by VARCHAR(100),        -- Username of last updater
    last_updated_date TIMESTAMP,        -- Time of last update
    price DECIMAL(10,2),                -- Cost of the plan
    description TEXT                    -- Details of the plan
);

```
--- 
## Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/plans` | Get all plans |
| **GET** | `/plans/category/<category>` | Get plans by category |
| **GET** | `/plans/<plan_name>` | Get plan by name |

---
