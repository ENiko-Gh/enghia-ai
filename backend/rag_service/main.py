from fastapi import FastAPI
from pydantic import BaseModel
import chromadb, httpx, hashlib

app = FastAPI()
client = chromadb.PersistentClient(path="/app/db")
col = client.get_or_create_collection(name="memoria")
OLLAMA = "http://192.168.100.57:11434/api/embed"

class Ingest(BaseModel):
    text: str
class Query(BaseModel):
    query: str

@app.post("/ingest")
async def ingest(req: Ingest):
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(OLLAMA, json={"model":"nomic-embed-text", "input":req.text})
        emb = r.json()["embeddings"][0]
        col.add(embeddings=[emb], documents=[req.text], ids=[hashlib.md5(req.text.encode()).hexdigest()])
    return {"status":"ok"}

@app.post("/query")
async def query(req: Query):
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(OLLAMA, json={"model":"nomic-embed-text", "input":req.query})
        emb = r.json()["embeddings"][0]
    res = col.query(query_embeddings=[emb], n_results=1)
    return {"contexto": res['documents'][0] if res['documents'] else []}
