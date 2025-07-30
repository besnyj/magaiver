import io
from fastapi import FastAPI, File, UploadFile, HTTPException
from projeto.backend.start import start
from .models import GenmaResponse
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()


api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.post('/upload_overview')
async def overview(file: UploadFile = File()):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Selecione o Overview salvo como um arquivo Excel (.xlsx)")

    contents = await file.read()
    buffer = io.BytesIO(contents)
    response = GenmaResponse(message=start(buffer))

    try:
        return response.model_dump()
    except:
        HTTPException(status_code=500, detail="Falha na criação do portfolio")
