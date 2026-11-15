from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import httpx, json

app = FastAPI()

@app.post("/v1/chat/completions")
async def chat(request: Request):
    data = await request.json()
    user_msg = data['messages'][-1]['content'].lower()
    context = ""

    async with httpx.AsyncClient(timeout=60) as client:
        # Buscar en memoria
        try:
            r = await client.post("http://192.168.100.59:8893/query", json={"query": user_msg})
            if r.status_code == 200 and r.json().get('contexto'):
                context += "MEMORIA: " + " ".join(r.json()['contexto']) + "\n"
        except: pass

    prompt = f"Eres ENGHIA. Responde en español, breve. Usa este contexto si es útil:\n{context}\nPregunta: {user_msg}"

    async def stream():
        async with httpx.AsyncClient(timeout=120) as client:
            async with client.stream("POST", "http://192.168.100.57:11434/api/generate", 
                json={"model": "llama3:latest", "prompt": prompt, "stream": True}) as r:
                async for line in r.aiter_lines():
                    if line:
                        try:
                            d = json.loads(line)
                            if "response" in d:
                                yield f"data: {json.dumps({'choices':[{'delta':{'content':d['response']}}]})}\n\n"
                        except: pass
        yield "data: [DONE]\n\n"
    return StreamingResponse(stream(), media_type="text/event-stream")
