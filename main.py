from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

class InstagramData(BaseModel):
    instagram_url: str

@app.post("/registro")
async def recibir_instagram(request: Request):
    data = await request.json()
    instagram_url = data.get("instagram_url")

    if instagram_url:
        # Aquí puedes imprimirlo, guardarlo, o lanzar el procesamiento automático
        print(f"✅ Nueva URL recibida: {instagram_url}")
        return {"message": "URL recibida correctamente."}
    else:
        return {"error": "No se proporcionó ninguna URL."}

# Solo si ejecutas localmente
if __name__ == "__main__":
    uvicorn.run("nombre_del_archivo:app", host="0.0.0.0", port=8000, reload=True)
