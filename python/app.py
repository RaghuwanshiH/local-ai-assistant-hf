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
    try:
        result = subprocess.run(
            ["ollama", "run", "tinyllama", message],
            capture_output=True,
            text=False,
            timeout=120
        )
        text = result.stdout.decode('utf-8', errors='ignore')
        clean_output = re.sub(r'\x1b\[[0-9;]*[mGKHABCD]', '', text)
        clean_output = re.sub(r'\r', '', clean_output).strip()

        if not clean_output:
            return "Ollama didn't respond. Is it running? Check terminal."

        return clean_output

demo = gr.ChatInterface(
    fn=chat_with_ollama,
    title="Local AI Assistant 🔒",
    description="100% Offline ChatGPT build by Harsh Raghuwanshi - Zero API costs. Powered by TinyLama"
)
    except subprocess.TimeoutExpired:
        return "TinyLlama took too long. Try a shorter question."
    except FileNotFoundError:
        return "Error: Ollama not found. Make sure 'ollama' is in your PATH."
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="Local AI") as demo:
    gr.Markdown("# 🤖 Local AI Assistant 🔒")
    gr.Markdown("**100% Offline ChatGPT built by Harsh Raghuwanshi - Zero API costs. Powered by TinyLlama**")

    gr.ChatInterface(
        fn=chat_with_ollama,
        examples=["Explain Python in simple terms", "Write a haiku about coding", "What's 15% of 80?"],
    )

demo.launch(share=True)
if __name__ == "__main__":
    demo.launch(share=True)
