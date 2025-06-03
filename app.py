import gradio as gr
import os
import time
from langchain_community.llms import HuggingFaceHub
from langchain_community.retrievers import BM25Retriever
from langchain_huggingface import HuggingFaceEmbeddings # embeding the documents in the vectorstore
from langchain_huggingface import ChatHuggingFace # chat model
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.retrievers import EnsembleRetriever
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.messages import HumanMessage,AIMessage
from langchain.tools.retriever import create_retriever_tool
from langchain_groq import ChatGroq

token = os.getenv('gr_tkn')
os.environ["GROQ_API_KEY"] = token
def build_rag_chain():
    pdfloader = PyPDFLoader('kuDoc.pdf')
    docs = pdfloader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
    texts = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    db = Chroma.from_documents(texts,embedding=embeddings)

    vector_retriever = db.as_retriever(search_type='similarity',search_kwargs = {'k':5})
    keyword_retriever = BM25Retriever.from_documents(documents=texts,k=5)

    ensemble_retriever = EnsembleRetriever(
        retrievers=[keyword_retriever, vector_retriever],
        weights=[0.5, 0.5]
    )

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    chat_model = llm

    memory_system_prompt = (
        "You are ChatKU, an AI assistant that helps users learn more about Kenyatta University. "
        "Greet the user by saying: 'Hello my name is ChatKU, I can help you to get to know more about Kenyatta University, so how can I help you dear?' "
        "You should help reformulate follow-up questions into standalone questions. "
        "Given the chat history and the latest user message, rewrite the user’s message as a clear, self-contained question that incorporates all relevant context. "
        "Do not invent new information. "
        "If the user introduces themselves (e.g., 'Hello, I am Steve' or 'My name is Joy'), remember their name for the rest of the conversation. "
        "If the user later asks 'What is my name?' or similar, respond using the name they previously provided. "
        )
    memory_prompt = ChatPromptTemplate.from_messages([
        ('system',memory_system_prompt),
        MessagesPlaceholder('chat_history'),# allow us to pass a list of messages to the prompt using 'chat_history'
        ('human','{input}')
    ])

    system_prompt = (
        "You are ChatKU, an AI assistant that helps users learn more about Kenyatta University."
        "Greet the user by saying: 'Hello my name is ChatKU, I can help you to get to know more about Kenyatta University, so how can I help you dear?' "
        "Remember the user's name when they introduce it (e.g., 'Hello, am Steve') and"
        "use it in future responses when the user asks about their name"
        "Use only the information provided in the context below. "
        "think like an agent before answering the question and give the correct answer"
        "Do not make up information or add external knowledge. "
        "If the answer cannot be found in the context, say so clearly. "
        "Keep your answers concise, natural, and friendly. "
        "Feel free to address the user by name if mentioned in the chat history. "
        "Avoid repeating long context word-for-word. "
        "Never start your answer with phrases like 'Based on the provided context'. "
        "Consider bolded or stylized text in the context as important keywords.\n\n"
        "Context:\n{context}\n\n"
    )

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(chat_model,ensemble_retriever,memory_prompt)

    question_answer_chain = create_stuff_documents_chain(chat_model, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    return rag_chain

rag_chain = build_rag_chain()
chat_history = []

def chatku_fn(message, history):
    global chat_history
    response = rag_chain.invoke({
        "input": message,
        "chat_history": chat_history
    })
    answer = response["answer"]

    chat_history.append(HumanMessage(content=message))
    chat_history.append(AIMessage(content=answer))

with gr.Blocks(fill_height = True) as demo:
    gr.Markdown(
        "<h2 style='text-align: center;'>Any Queries about Kenyatta University?</h2>"
    )

    gr.ChatInterface(
        fn=chatku_fn,
        chatbot=gr.Chatbot(label="💬 ChatKU"),
        autoscroll=True
    )

    gr.Markdown(
        "⚠️ *ChatKU can make mistakes, check important info.*",
        elem_id="footer"
    )
if __name__ == "__main__":
    demo.launch(share = True)
