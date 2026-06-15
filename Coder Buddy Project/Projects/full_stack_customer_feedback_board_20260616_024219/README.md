# Full-Stack Customer Feedback Board

A full-stack web application for submitting, storing, and displaying customer feedback. Powered by a FastAPI backend backed by SQLite (SQLAlchemy) and a simple responsive HTML/CSS/JS frontend. Includes user JWT token registration and login authentication.

## 📂 Project Structure

- `backend/`: Python API backend code.
  - `main.py`: FastAPI server exposing registration, login, and feedback CRUD endpoints.
  - `auth_service.py`: Handles JWT token creation, decoding, and password hashing logic.
  - `database.py`: Establishes SQLAlchemy connection engines, schemas, and sessions.
- `frontend/`: Web UI folder.
  - `index.html`: Feedback dashboard interface.
  - `style.css`: Responsive CSS stylesheets.
- `DEPLOY.md`: Render and Docker containerization deployment guide.

---

## 🚀 How to Run the Project

### 1. Open Terminal and Navigate to Project Directory
```powershell
cd "Coder Buddy Project/Projects/full_stack_customer_feedback_board_20260616_024219"
```

### 2. Start the Backend API Server
Use the workspace virtual environment to run the backend server:
```powershell
..\..\.venv\Scripts\python.exe -m backend.main
```
The server will start up on [http://localhost:8000](http://localhost:8000).

### 3. Run the Frontend
Since the frontend uses standard vanilla JS with CORS enabled, you can run the frontend page directly:
- **Double click** the `frontend/index.html` file in your file explorer to open it in your browser.
- **Or run a local static server** inside the `frontend/` directory if you prefer:
  ```powershell
  cd frontend
  python -m http.server 8080
  ```
  Then open [http://localhost:8080](http://localhost:8080) in your browser.
