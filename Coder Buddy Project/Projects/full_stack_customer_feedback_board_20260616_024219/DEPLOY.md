# Deployment Guide

This guide explains how to deploy the Customer Feedback Board application.

---

## 🐳 1. Local Containerized Deployment (Docker)

If you have Docker installed on your computer, you can run the entire database and backend stack inside isolated containers.

### Prerequisites:
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

### How to Run:
1. Open a terminal in the project root directory:
   ```bash
   cd Projects/full_stack_customer_feedback_board_20260616_024219
   ```
2. Run the build command:
   ```bash
   docker-compose up --build
   ```
   This will:
   - Download the official PostgreSQL 16 image.
   - Build a custom Python image for your FastAPI backend.
   - Expose the API endpoints at `http://localhost:8000`.

---

## 🚀 2. Cloud Deployment

### A. Backend Deployment (Render / Railway)
You can deploy your Python FastAPI backend directly to **Render** or **Railway**.

#### Render Deployment Steps:
1. Create a free account at [Render](https://render.com/).
2. Push your project code to GitHub (this happens automatically via `git_auto_sync.py`).
3. In the Render Dashboard, click **New +** and select **Web Service**.
4. Connect your GitHub repository.
5. Configure the service settings:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
6. Under **Environment Variables**, click **Add Environment Variable**:
   - `DATABASE_URL` (You can link it to a PostgreSQL database instance on Render).
7. Click **Deploy Web Service**. Render will assign a public URL (e.g., `https://my-api.onrender.com`).

---

### B. Frontend Deployment (Vercel / Netlify / GitHub Pages)
Since the frontend is a static single-page application (`index.html` + `style.css`), it can be hosted for free on **Vercel** or **Netlify**.

#### Vercel Deployment Steps:
1. Create a free account at [Vercel](https://vercel.com/).
2. Install the Vercel CLI locally (`npm install -g vercel`) or deploy via Vercel Dashboard.
3. Open your terminal in the `frontend` folder:
   ```bash
   cd Projects/full_stack_customer_feedback_board_20260616_024219/frontend
   ```
4. Run:
   ```bash
   vercel
   ```
5. Follow the CLI prompt to log in and deploy. Your static site will be assigned a public URL (e.g., `https://my-dashboard.vercel.app`).
6. *Note:* Ensure that the `fetch` URLs in `frontend/index.html` (e.g., `http://localhost:8000/auth/login`) are updated to point to your hosted Render backend URL (e.g., `https://my-api.onrender.com/auth/login`).
