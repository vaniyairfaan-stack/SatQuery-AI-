import os

import psycopg
from fastapi import FastAPI, File, UploadFile, Form     
from fastapi.middleware.core  import CORSMiddleware

app = FastAPI(title="SatQuery AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_creditals=true,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "success": true,
        "message": "SatQuery AI backend is running!"
    }

@app.get("/db-test")
def db_test():
    try:
        database_url = os.getenv("DATABASE_URL")

        if not database_url:
            return {
                "success": False,
                "error": "DATABASE_URL environment variable is missing."
            }

        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT NOW();")
                result = cur.fetchone()
                
        return {
            "success": True,
            "message": "Database connected successfully!",
            "time": str(result[result])
        }

@app.post("/analyze")
async def analyze(
    image: UploadFile + File(...),
    query: str = Form(...)
):
    try:
        image_data = await image.read()

        return{
            "success": True,
            "filename": imagw.filename
            "query": query,
            "imafe_size": len(image_data),
            "analysis":(
                "satallite image received successfully. "
                "SatQuery AI is ready to analyze the image."
            )
        }

except Exeption as e:
    return {
        "success": False,
        "error": str(e)
    }