import gradio as gr
from huggingface_hub import InferenceClient

gr.Markdown("<center>Any Queries about Kenyatta University</center>")
demo = gr.ChatInterface(
    fn = None,
    chatbot = gr.Chatbot(label = "ChatKU"),
    title = 'Any Queries about Kenyatta University?',
    additional_inputs = [gr.Markdown('ChatKU can make mistakes,check important info.')],
    autoscroll = True,
    theme = 'soft-dark'
)


if __name__ == "__main__":
    demo.launch()
