from pydantic import BaseModel


class GenmaResponse(BaseModel):
    message: str

