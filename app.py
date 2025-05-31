import gradio as gr
from huggingface_hub import InferenceClient

demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value="You are a friendly Chatbot.", label="System message"),
    ],
    description = 'ChatKU',
    theme = 'Dark'
)


if __name__ == "__main__":
    demo.launch()
