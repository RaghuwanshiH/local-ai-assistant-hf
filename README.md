# Local AI Assistant

## 🚀 Live Demo 
https://2a5b6cc7a70624be3d.gradio.live
*Link works only when my laptop is running. Last updated: 2026-05-21*

Offline ChatGPT clone running 100% on your laptop using Ollama + Python + Gradio.

### Why this is cool:
- **Zero API costs** - no OpenAI key needed
- **Works without internet** - AI runs locally on your CPU
- **Full privacy** - your data never leaves your machine
- **Two versions** - CLI for speed, Web UI for sharing

### Tech Stack:
Python, Ollama, TinyLlama, Gradio

### Run it locally:

**0. Install Python 3.10+** 
Download from https://python.org. During install, check **"Add Python to PATH"**.

**1. Install Ollama + download model** 
Download from https://ollama.com then run:
```bash
ollama pull tinyllama
```

**2. Install Python packages**
```bash
pip install gradio
```
Web UI - recommended:
```bash
python python/app.py
```
Then open http://127.0.0.1:7860. For a public link, set share=True in app.py.
CLI version - terminal only:
```bash
python python/test.py

