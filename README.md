# Local AI Assistant - Cloud Version

### ☁️ Runs 24/7 on Hugging Face Spaces

Offline ChatGPT clone using TinyLlama 1.1B. No API keys, no cost, always online.

### 🚀 Live Demo
https://huggingface.co/spaces/HarshRaghuwanshi/python

![Demo](demo.png)

### Why this is cool:
- **Zero API costs** - no OpenAI key needed
- **Always online** - hosted free on HF Spaces  
- **Full privacy** - your data never leaves the container
- **Runs on CPU** - works anywhere, no GPU needed

### Tech Stack:
Python, Gradio, TinyLlama, Hugging Face Spaces

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


