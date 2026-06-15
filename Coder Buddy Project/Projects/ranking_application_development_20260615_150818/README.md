# Ranking Application API

A FastAPI backend application demonstrating ranking algorithms, data persistence, and schemas.

## 📂 Project Structure

- `main.py`: FastAPI server exposing CRUD endpoints for Users and Items.
- `schemas.py`: Pydantic models for data validation.
- `models.py`: SQLAlchemy database models (defined for production structure).
- `database.py`: Establishes DB sessions.
- `ranking_algorithm.py`: Core logic computing user rankings based on metrics.
- `Technical_Design.md`: Documentation on system architecture and ranking formulas.

---

## 🚀 How to Run the Project

### 1. Open Terminal and Navigate to Project Directory
```powershell
cd "Coder Buddy Project/Projects/ranking_application_development_20260615_150818"
```

### 2. Start the Backend API Server
Launch the backend server using the workspace virtual environment:
```powershell
..\..\.venv\Scripts\python.exe main.py
```
The server will start up on [http://localhost:8000](http://localhost:8000). You can navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to view and test the API interactive documentation.
