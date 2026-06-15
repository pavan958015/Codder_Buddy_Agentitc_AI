from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from calculator_app.routes.main import calculator_router

app = FastAPI(title="Scientific Calculator API")

# Include calculator endpoints
app.include_router(calculator_router)

# Resolve path to frontend assets
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

@app.get("/")
def read_root():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

# Mount frontend folder under /static
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)