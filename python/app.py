import gradio as gr
import os
import subprocess
import re
import gc

IS_HF = os.getenv("SPACE_ID") is not None

if IS_HF:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch

    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    model = AutoModelForCausalLM.from_pretrained(
        model_id, dtype=torch.float32, low_cpu_mem_usage=True, device_map="cpu"
    )

    def chat(message, history):
        # Fix 1: History poori clear. Sirf current message bhejo.
        # HF free tier pe chat memory afford nahi kar sakta
        messages = [{"role": "user", "content": message}]

        prompt = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = tokenizer(prompt, return_tensors="pt").to("cpu")

        # Fix 2: Tokens kam karo HF ke liye
        outputs = model.generate(
            **inputs,
            max_new_tokens=80,  # 150 se 80 kiya
            do_sample=True,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
        )
        response = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1] :], skip_special_tokens=True
        )

        # Fix 3: Aggressive memory cleanup
        del inputs, outputs, prompt, messages
        gc.collect()
        torch.cuda.empty_cache()

        return response.strip()

else:

    def chat(message, history):
        try:
            result = subprocess.run(
                ["ollama", "run", "tinyllama", message],
                capture_output=True,
                text=False,
                timeout=120,
            )
            text = result.stdout.decode("utf-8", errors="ignore")
            clean_output = re.sub(r"\x1b\[[0-9;]*[mGKHFABCD]", "", text)
            clean_output = re.sub(r"\r", "", clean_output).strip()
            if not clean_output:
                return "Ollama didn't respond. Is it running? Check terminal."
            return clean_output
        except subprocess.TimeoutExpired:
            return "TinyLlama took too long. Try a shorter question."
        except FileNotFoundError:
            return "Error: Ollama not found. Make sure 'ollama' is in your PATH."
        except Exception as e:
            return f"Error: {str(e)}"


if IS_HF:
    css = ".gradio-container {max-width: 700px!important; margin: auto!important} footer {display: none!important}"
    demo = gr.ChatInterface(
        fn=chat,
        title="🤖 JARVIS-Lite Offline AI Assistant 🔒",
        description="**100% Free ChatGPT built by Harsh Raghuwanshi - Zero API costs. Powered by TinyLlama**",
        examples=[
            "Explain Python in simple terms",
            "Write a haiku about coding",
            "What's 15% of 80",
        ],
        css=css,
    )
    demo.launch()
else:
    demo = gr.ChatInterface(
        fn=chat,
        title="🤖 JARVIS-Lite Offline AI Assistant 🔒",
        description="**100% Free ChatGPT built by Harsh Raghuwanshi - Zero API costs. Powered by TinyLlama**",
        examples=[
            "Explain Python in simple terms",
            "Write a haiku about coding",
            "What's 15% of 80",
        ],
    )
    demo.launch(inbrowser=True, server_name="127.0.0.1", share=False)
