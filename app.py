import gradio as gr
from huggingface_hub import InferenceClient

gr.Markdown("<center>Any Queries about Kenyatta University</center>")
demo = gr.ChatInterface(
    fn = None,
    chatbot = gr.Chatbot(placeholder = "Message me..."),
    title = 'ChatKU',
    description = 'ChatKU',
    autoscroll = True,
    theme = 'soft-dark'
)


if __name__ == "__main__":
    demo.launch()
