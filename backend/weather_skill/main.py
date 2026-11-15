from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

API_KEY = os.getenv("OPENWEATHER_API_KEY", "TU_API_KEY_AQUI")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# REGRESAMOS A LA RUTA SIMPLE
@app.get("/weather")
async def get_weather(city: str):
    if API_KEY == "TU_API_KEY_AQUI":
        return {"error": "Falta configurar la API Key."}
    
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "es"}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            hum = data['main']['humidity']
            return {"text": f"En {city} hay {desc}, con una temperatura de {temp}°C y {hum}% de humedad."}
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error al consultar el clima")
