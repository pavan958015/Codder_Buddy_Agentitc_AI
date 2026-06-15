# Modern Scientific Calculator App

This project is a modern, responsive scientific calculator featuring a beautiful glassmorphic frontend UI connected to a FastAPI backend service.

## 📂 Project Structure

- `frontend/`: Frontend web assets.
  - `index.html`: Main HTML interface with async fetch integrations.
  - `style.css`: Dark-slate glassmorphic styling sheet.
- `calculator_app/`: Backend FastAPI application.
  - `main.py`: Main entry point mounting endpoints and static frontend folders.
  - `routes/main.py`: Exposes `/api/calculate` endpoint routes.
  - `services/calculator_service.py`: Implements Memory and math logic routing.
  - `utils/math_operations.py`: Core mathematical library (basic and scientific operations).
  - `tests/`: Automated unit tests.

---

## 🚀 How to Run the Project

Since the virtual environment is managed in the root workspace folder, follow these steps to run the application from this project's directory:

### 1. Open Terminal and Navigate to Project Directory
```powershell
cd "Coder Buddy Project/Projects/simple_scientific_calculator_20260616_034102"
```

### 2. Start the FastAPI Server
Run the module using the workspace virtual environment:
```powershell
..\..\.venv\Scripts\python.exe -m calculator_app.main
```

### 3. Open in Browser
Open [http://localhost:8000](http://localhost:8000) in your web browser to use the calculator.

---

## 🧪 Running Unit Tests

To run the full suite of **25 unit tests** verifying backend arithmetic, service layers, and routing:
```powershell
..\..\.venv\Scripts\python.exe -m unittest discover -s calculator_app/tests
```
