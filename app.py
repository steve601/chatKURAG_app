import gradio as gr
from huggingface_hub import InferenceClient

with gr.Blocks(theme="soft-dark") as demo:
    gr.Markdown(
        "<h2 style='text-align: center;'>Any Queries about Kenyatta University</h2>"
    )

    gr.ChatInterface(
        fn=None,
        chatbot=gr.Chatbot(label="💬 ChatKU"),
        autoscroll=True
    )

    gr.Markdown(
        "⚠️ *ChatKU can make mistakes, check important info.*",
        elem_id="footer"
    )
if __name__ == "__main__":
    demo.launch(share = True)
