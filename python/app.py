import gradio as gr
import ollama

def extract_text(msg_content):
    if isinstance(msg_content, list) and len(msg_content) > 0:
        return msg_content[0].get('text', '')
    return str(msg_content)

def chat(message, history):
    messages = [
        {
            "role": "system",
            "content": "You are a casual chatbot. Reply like a friend texting. NEVER explain, translate, or add notes. NEVER use parentheses for translations. Match the user's language. If user says 'bro', reply 'Bro! Kya haal?' Keep replies under 2 lines. No essays. Be direct."
        }
    ]

    for msg in history:
        content = extract_text(msg['content'])
        messages.append({"role": msg['role'], "content": content})

    messages.append({"role": "user", "content": message})

    try:
        response = ollama.chat(
            model='phi3:mini',
            messages=messages,
            stream=False,
            options={
                "temperature": 0.7,
                "num_predict": 100,
                "stop": ["User:", "Assistant:"]
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 MaNe Offline AI Assistant")
    gr.Markdown("**Model:** Microsoft Phi-3 3.8B | **Backend:** Ollama + RTX 3050 | **100% Local**")
    gr.Markdown("*Built by Harsh Raghuwanshi*")

    chatbot = gr.Chatbot(height=500, label="Chat with Phi-3")
    msg = gr.Textbox(label="Your Message", placeholder="Ask me anything...")

    with gr.Row():
        submit = gr.Button("Send", variant="primary")
        clear = gr.ClearButton([msg, chatbot], value="Clear")

    def respond(message, chat_history):
        if not message.strip():
            return "", chat_history
        bot_message = chat(message, chat_history)
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": bot_message})
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    submit.click(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(share=True)