# Full-Stack Database Explorer Dashboard

This project is a database exploration portal. It exposes a FastAPI backend managing connection interfaces for MySQL and MongoDB database schemas, coupled with an interactive web dashboard frontend.

## 📂 Project Structure

- `backend/`: API services and connection managers.
  - `main.py`: FastAPI server setting up connections and `/health` checkers.
- `frontend/`: Web UI portal.
  - `index.html`: Main status dashboard layout.
  - `style.css`: Modern visual styling sheet.
  - `app.js`: Connects to backend endpoints and handles interface updates.

---

## 🚀 How to Run the Project

### 1. Open Terminal and Navigate to Project Directory
```powershell
cd "Coder Buddy Project/Projects/full_stack_database_explorer_dashboard_20260615_191911"
```

### 2. Start the Backend API Server
Launch the backend server using the virtual environment:
```powershell
..\..\.venv\Scripts\python.exe -m backend.main
```
The server will start up on [http://localhost:8000](http://localhost:8000).

### 3. Start the Frontend
- **Double click** the `frontend/index.html` file in your file explorer to open it in your browser.
- **Or run a local static server** inside the `frontend/` directory if you prefer:
  ```powershell
  cd frontend
  python -m http.server 8080
  ```
  Then open [http://localhost:8080](http://localhost:8080) in your browser.
