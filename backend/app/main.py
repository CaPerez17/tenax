from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.student_profiles import router as student_profiles_router

app = FastAPI(
    title="Tenax API",
    description="MVP Educativo - Backend", 
    version="0.1.0"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(student_profiles_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello from Tenax Backend!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
