# ChatKU: A RAG-Based Campus Assistant for Kenyatta University

**ChatKU** is a specialized chatbot created for users at Kenyatta University. It uses **ChatGrog** as its language model, along with LangChain for managing operations, **PyPDF** for handling documents, and **Gradio** to provide a user-friendly interface. With ChatKU, students and staff can easily access important university information in a conversational way, ensuring quick and accurate responses.

The chatbot processes university documents stored in PDF format with PyPDF, making it easy to search and retrieve the information users need. By integrating with LangChain, it generates answers that are not only relevant but also enriched by the content pulled from those documents. The frontend, designed with Gradio, creates an accessible web interface that allows real-time interaction, making it a breeze for everyone on campus to connect with the information they seek.

This project aims to: 

-**Simplify access to university information (admissions, departments, timetables, contacts, etc.)**

-**Provide a conversational interface for interacting with institutional documents**

-**Demonstrate the effectiveness of RAG architecture in domain-specific knowledge systems**

## Key Features

1.**🔍 Document-Aware Q&A** – Answers questions using actual university documents

2.**📄 PDF Parsing** – Loads and processes university PDFs using PyPDF

3.**🤖 RAG Architecture** – Combines retrieval with generation for grounded responses

4.**🌐 Gradio Interface** – Clean, web-based chatbot interface for interaction

5.**🏫 Campus-Specific Knowledge** – Custom knowledge base focused on Kenyatta University

## Tech stack

1.**ChatGrog** – LLM for response generation

2.**LangChain** – Framework for chaining retrieval and generation

3.**PyPDF** – Library for parsing and extracting text from PDFs

4.**Gradio** – Lightweight UI for deploying the chatbot on the web

## Workflow

![Rag workflow](https://d3lkc3n5th01x7.cloudfront.net/wp-content/uploads/2024/08/26051537/Advanced-RAG.png)

1.**PDF Ingestion:** University documents are loaded and parsed using PyPDF.

2.**Chunking & Embedding:** Text is split into chunks and embedded using a model supported by LangChain.

3.**Retrieval:** Relevant chunks are retrieved based on the user’s question(keyword and vector retriever)

4.**Response Generation:** ChatGrog generates a context-aware response using retrieved chunks.

5.**UI:** Gradio handles the user interface for real-time interaction.

## Example Questions
"What are the admission requirements for undergraduate students?"

"How can I contact the School of Engineering?"

"How do i replace my Student ID card, incase it's lost?"

## Future Improvements

🔊 Add voice input/output support

🌍 Support for Kiswahili and other local languages

🧠 Plug in a more powerful LLM like GPT-4 or Mistral

**You can view the app via mobile phone through; https://huggingface.co/spaces/SgmkerAI/chatku.**
