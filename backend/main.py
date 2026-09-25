from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SatQuery AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "SatQuery AI backend is running!"
    }


@app.post("/analyze")
async def analyze(
    image: UploadFile = File(...),
    query: str = Form(...)
):
    image_data = await image.read()

    return {
        "success": True,
        "filename": image.filename,
        "query": query,
        "image_size": len(image_data),
        "analysis": (
            "Satellite image received successfully. "
            "SatQuery AI is ready to analyze the image."
        )
    }
