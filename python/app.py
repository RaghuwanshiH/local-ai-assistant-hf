import gradio as gr
import os
import subprocess
import re

# Check if we're on Hugging Face Spaces
IS_HF = os.getenv('SPACE_ID') is not None

if IS_HF:
    # CODE FOR HUGGING FACE - uses transformers directly
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
    
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True)
    
    def chat(message, history):
        messages = []
        for user_msg, bot_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": bot_msg})
        messages.append({"role": "user", "content": message})
        
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=256, do_sample=True, temperature=0.7)
        response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        return response.strip()

else:
    # CODE FOR YOUR LOCAL PC - uses Ollama
    def chat(message, history):
        try:
            result = subprocess.run(
                ["ollama", "run", "tinyllama", message],
                capture_output=True,
                text=False,
                timeout=120
            )
            text = result.stdout.decode('utf-8', errors='ignore')
            clean_output = re.sub(r'\x1b\[[0-9;]*[mGKHFABCD]', '', text)
            clean_output = re.sub(r'\r', '', clean_output).strip()
            if not clean_output:
                return "Ollama didn't respond. Is it running? Check terminal."
            return clean_output
        except subprocess.TimeoutExpired:
            return "TinyLlama took too long. Try a shorter question."
        except FileNotFoundError:
            return "Error: Ollama not found. Make sure 'ollama' is in your PATH."
        except Exception as e:
            return f"Error: {str(e)}"

# Same UI for both
with gr.Blocks(title="Local AI") as demo:
    gr.Markdown("# 🤖 JARVIS-Lite Offline AI Assistant 🔒")
    gr.Markdown("**100% Free ChatGPT built by Harsh Raghuwanshi - Zero API costs. Powered by TinyLlama**")
    gr.ChatInterface(
        fn=chat,
        examples=["Explain Python in simple terms", "Write a haiku about coding", "What's 15% of 80"],
    )

# For local: don't use share=True, set explicit host/port, auto-open browser
if IS_HF:
    demo.launch()  # HF Spaces handles this
else:
    demo.launch(inbrowser=True, server_name="127.0.0.1", server_port=7860, share=False)
