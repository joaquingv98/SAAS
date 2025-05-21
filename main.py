from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import datetime
import os

app = FastAPI()

# Crear carpeta si no existe
os.makedirs("submisiones", exist_ok=True)

@app.post("/registro")
async def recibir_datos(request: Request):
    data = await request.json()
    instagram_url = data.get("link instagram bio.")  # Esto depende del nombre exacto del campo en Tally

    if not instagram_url:
        return JSONResponse(status_code=400, content={"error": "No se encontró ninguna URL"})

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"submisiones/instagram_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(instagram_url)

    print(f"✅ Guardado: {instagram_url}")
    return {"mensaje": "URL recibida correctamente"}
