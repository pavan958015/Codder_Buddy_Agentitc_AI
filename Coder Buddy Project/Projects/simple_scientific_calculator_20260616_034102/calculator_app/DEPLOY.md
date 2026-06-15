# Deployment Guide for Calculator Application

This guide provides instructions on how to deploy the calculator application using Docker and Docker Compose. This setup is ideal for environments like Render, AWS ECS/EC2, or any cloud provider supporting container orchestration.

## Prerequisites

1.  **Docker:** Ensure Docker is installed on your deployment environment.
2.  **Cloud Provider Account:** An active account with a cloud provider (e.g., Render, AWS).
3.  **Database Access:** If using the provided `docker-compose.yml`, ensure you have access to manage external services if migrating beyond local setup.

## 1. Environment Variables

The application relies on several environment variables for configuration. These should be set in your deployment platform's environment variable settings:

| Variable Name | Description | Example Value (Local/Render) | Required For |
| :--- | :--- | :--- | :--- |
| `PORT` | The port the application listens on. | `8000` | Application Startup |
| `DATABASE_URL` | Connection string for the database. | `postgresql://user:password@host:port/dbname` | Database Connection |
| `MONGO_URI` | MongoDB connection string (if applicable). | `mongodb://mongo:27017/CoderBuddy` | MongoDB Connection |

**Note:** For production, use secure secrets management provided by your cloud provider instead of hardcoding values.

## 2. Infrastructure Setup Instructions

### Option A: Using Docker Compose (Recommended for Render/Self-Managed)

If deploying on a platform that supports `docker-compose.yml` directly (like Render's web service setup), use the provided configuration file.

1.  **Build Image:** The deployment system will automatically build the image based on the `Dockerfile`.
2.  **Run Services:** Deploy the services defined in `docker-compose.yml`:
    *   The `web` service handles the application logic and exposes port 8000.
    *   The `db` service provides a MySQL database instance.
    *   The `mongo` service provides a MongoDB instance.

### Option B: Using Cloud Provider Specific Instructions (e.g., AWS ECS/EC2)

If deploying on a more complex infrastructure like AWS, follow these general steps:

1.  **Containerize:** Build the Docker image locally and push it to a container registry (e.g., Amazon ECR).
    ```bash
    docker build -t calculator-app .
    docker push <your-registry>/calculator-app:latest
    ```
2.  **Provision Database:** Set up your managed database service (e.g., AWS RDS for MySQL or MongoDB Atlas).
3.  **Deploy Application:** Configure your orchestration service (ECS/EKS) to run the container, ensuring it has network access to the provisioned database endpoints using the environment variables defined in Section 1.

## 3. Deployment Steps Summary

1.  **Prepare Files:** Ensure `app.py`, `requirements.txt`, and `Dockerfile` are committed to your repository.
2.  **Configure Environment Variables:** Set all necessary environment variables (`PORT`, `DATABASE_URL`, etc.) in the deployment platform's configuration panel.
3.  **Deploy:** Initiate the deployment process using the chosen method (e.g., connecting Render to your GitHub repo).

## 4. Verification

After deployment, verify that:
*   The application starts successfully without errors.
*   All database connections are established correctly.
*   The application is accessible via the configured public URL/port.