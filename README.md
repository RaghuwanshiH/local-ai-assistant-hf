# Local AI Assistant

## 🚀 Live Demo

 **1. Permanent Cloud Link - 24/7:**   https://huggingface.co/spaces/HarshRaghuwanshi/python  
*Runs TinyLlama 1.1B on Hugging Face CPU. Always online.*

**2. Temporary GPU Link:** https://301ff5f802a78f1822.gradio.live  
*Faster demo, but only works when my laptop is running. Last updated: 2026-05-21*
![Demo](demo.png)

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

**CLI version - terminal only:**
```bash
python python/test.py
```

### Features:
- Chat with local LLM through terminal or browser
- One-click launcher with `run.bat`
- Public sharing via Gradio links
- Fully offline after setup

### How to get a public link:
In `python/app.py`, change the last line to:
```python
demo.launch(share=True)
```
Restart the app and you'll get a https://xxxx.gradio.live link.

---
**Built with ❤️ to prove AI doesn't need the cloud**


