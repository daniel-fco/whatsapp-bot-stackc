from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Carga variables desde .env (si existe)
load_dotenv()

app = FastAPI()

@app.get("/health")
async def health():
    whatsapp_token = os.getenv("WHATSAPP_TOKEN")
    phone_id = os.getenv("PHONE_NUMBER_ID")

    missing = []
    if not whatsapp_token:
        missing.append("WHATSAPP_TOKEN")
    if not phone_id:
        missing.append("PHONE_NUMBER_ID")

    env_ok = len(missing) == 0

    return {
        "status": "ok",            # el servidor responde
        "env_ok": env_ok,           # ¿están las variables?
        "missing_env": missing      # cuáles faltan (si faltan)
    }