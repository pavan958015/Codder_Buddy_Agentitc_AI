# Deployment Documentation: Galgotias University Landing Page

This document outlines the complete engineering process for building, containerizing, and deploying the Galgotias University landing page application using Docker and Docker Compose. This setup ensures a consistent, reproducible environment across development, testing, and production stages.

## 1. Overview
The deployment strategy utilizes Docker to package the application and its dependencies into portable containers, and Docker Compose to orchestrate the entire multi-container environment (e.g., web server, database, cache) seamlessly.

**Goal:** To provide a scalable and reliable infrastructure for the Galgotias University landing page.

## 2. Prerequisites
Before starting the deployment process, ensure you have the following installed on your local machine or CI/CD runner:
*   **Docker Engine:** Installed and running (for building images and running containers).
*   **Docker Compose:** Installed (version 1.27+ recommended) for defining and managing multi-container applications.

## 3. Project Structure Assumption
This deployment assumes the following structure in your project root:
```
/project_root
├── backend/          # Contains application source code (e.g., main.py, requirements.txt)
│   └── ...
├── Dockerfile        # Defines how the application image is built
├── docker-compose.yml # Defines the services and network for the entire stack
└── deployment/       # This documentation file
```

## 4. Building the Docker Image
The first step is to build the Docker image from the `Dockerfile`. This process compiles your source code, installs dependencies, and creates a runnable artifact.

**Command:**
Navigate to the root directory of your project and run:
```bash
docker build -t galgotias-landing-page:latest .
```
*   `-t`: Tags the image with a name (`galgotias-landing-page`) and version (`latest`).
*   `.`: Tells Docker to look for the `Dockerfile` in the current directory.

## 5. Setting up Docker Compose
Docker Compose is used to define and run the entire application stack, including the web service, database (e.g., MySQL), and any other necessary services. This simplifies complex setups by allowing you to start all required containers with a single command.

**Command:**
Navigate to the root directory of your project and run:
```bash
docker-compose up -d
```
*   `up`: Creates and starts the containers defined in `docker-compose.yml`.
*   `-d`: Runs the containers in detached mode (in the background).

**Note on Environment Variables:**
Ensure that all environment variables specified in `docker-compose.yml` (e.g., database credentials, port mappings) are correctly configured for your target environment. For production, these should be managed via a secure secret management system rather than hardcoded values.

## 6. Deployment Steps Summary

| Step | Action | Command Example | Description |
| :--- | :--- | :--- | :--- |
| **1** | Build Image | `docker build -t galgotias-landing-page:latest .` | Creates the application image based on the Dockerfile. |
| **2** | Start Stack | `docker-compose up -d` | Starts all services (Web, DB, etc.) defined in `docker-compose.yml`. |
| **3** | Verify Status | `docker ps` | Check if all containers are running and healthy. |

## 7. Verification and Troubleshooting

### Checking Container Status
To see the logs of your running services:
```bash
docker-compose logs -f web
# Or check all services:
docker-compose ps
```

### Common Issues & Solutions
*   **Port Conflicts:** If you encounter issues mapping ports, ensure that the host port (e.g., `8000`) is not already in use on your machine. Adjust the `ports` section in `docker-compose.yml`.
*   **Database Connection Errors:** Verify that the service names used in environment variables (e.g., `MYSQL_HOST=db`) correctly match the service names defined in `docker-compose.yml`.
*   **Build Failures:** Check the output of `docker build` for syntax errors or missing dependencies specified in the `Dockerfile`.

This documentation serves as the single source of truth for deploying the Galgotias University landing page infrastructure.