import gradio as gr
from huggingface_hub import InferenceClient

with gr.Blocks(theme="soft") as demo:
    gr.ChatInterface(
        fn=None,
        chatbot=gr.Chatbot(label="💬 ChatKU"),
        title="Any Queries about Kenyatta University",
        autoscroll=True
    )
    gr.Markdown("⚠️ *ChatKu can make mistakes,check important info.*", elem_id="footer")


if __name__ == "__main__":
    demo.launch()
