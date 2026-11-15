# ENGHIA - Asistente IA Local estilo Iron Man (JARVIS)

ENGHIA es un asistente de voz de código abierto, 100% local y privado. Inspirado en el HUD de Iron Man, utiliza microservicios en Docker, Ollama para el LLM y ChromaDB para memoria a largo plazo (RAG).

## 🚀 Características
- **Voz a Texto (STT):** Whisper.
- **Texto a Voz (TTS):** Kokoro (voz femenina en español).
- **Cerebro (LLM):** Llama 3 (vía Ollama).
- **Memoria (RAG):** ChromaDB + Nomic-Embed-Text.
- **HUD:** Interfaz en HTML/JS con partículas 3D y visualizador de voz.

## 🛠️ Arquitectura
- **Servidor Dell (Ubuntu):** Docker, Nginx Proxy Manager, ChromaDB, Microservicios (FastAPI).
- **Laptop Lenovo (Windows):** Ollama (Llama 3, Nomic-Embed).
- **Red:** Tailscale (acceso remoto seguro).

## ⚙️ Instalación Rápida
1. Clona el repo: `git clone https://github.com/tu-usuario/enghia-ai.git`
2. Renombra `.env.example` a `.env` y pon tus claves.
3. Levanta los servicios: `docker compose up -d --build`
4. Abre el `frontend/index.html` en tu navegador.

## 🗺️ Roadmap
- [x] HUD Interactivo
- [x] Memoria a Largo Plazo (RAG)
- [x] Skill de Clima en tiempo real
- [ ] Conector de Telegram
- [ ] Conector de Gmail
