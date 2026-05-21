import gradio as gr
import subprocess
import re

def chat_with_ollama(message, history):
    result = subprocess.run(
        ["ollama", "run", "tinyllama", message], 
        capture_output=True,
        text=False
    )
    # Decode + strip ALL ANSI escape codes
    text = result.stdout.decode('utf-8', errors='ignore')
    clean_output = re.sub(r'\x1b\[[0-9;]*[mGKHABCD]', '', text)
    clean_output = re.sub(r'\r', '', clean_output) # Remove carriage returns
    return clean_output.strip()

demo = gr.ChatInterface(
    fn=chat_with_ollama,
    title="Local AI Assistant 🔒",
    description="100% Offline ChatGPT build by Harsh Raghuwanshi - Zero API costs. Powered by TinyLama"
)

demo.launch(share=True)