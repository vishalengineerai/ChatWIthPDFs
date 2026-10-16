# Chat with Multiple PDFs

An AI-powered PDF chatbot built with Python, LangChain, and Google Gemini. Upload multiple PDF documents and ask questions about their contents through an interactive chat interface.

## Features

- **Multiple PDF Uploads:** Upload multiple PDF documents simultaneously.
- **PDF Text Extraction:** Extract text from uploaded documents using PyPDF2.
- **Text Chunking:** Split extracted text into smaller chunks for efficient retrieval.
- **Semantic Search:** Generate embeddings using Hugging Face's `all-MiniLM-L6-v2` model and store them in a FAISS vector store.
- **AI-Powered Answers:** Use Google Gemini through LangChain to generate responses based on retrieved document content.
- **Conversation Memory:** Maintain conversation history during the active application session.
- **Custom Chat Interface:** Use Streamlit with custom HTML and CSS styling for chat messages.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | LLM orchestration and RAG pipeline |
| Google Gemini | Language model for generating answers |
| Hugging Face | Text embedding model |
| FAISS | Vector storage and similarity search |
| PyPDF2 | PDF text extraction |
| python-dotenv | Environment variable management |

## How It Works

1. **Upload PDFs:** Select one or more PDF documents.
2. **Extract Text:** Extract text from each document's pages.
3. **Split Text:** Divide the extracted text into chunks with overlapping content.
4. **Generate Embeddings:** Convert text chunks into vector embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
5. **Store Vectors:** Store the embeddings in a FAISS vector store.
6. **Ask Questions:** Enter a question about the uploaded documents.
7. **Generate Responses:** Retrieve relevant document content and use Google Gemini to generate an answer.
8. **Maintain Context:** Use LangChain conversation memory to retain chat history during the active session.

## Project Structure

```text
Chat_pdf/
├── app.py
├── HT.py
├── requirements.txt
├── .env
├── .gitignore
└── venv/
```

- `app.py` — Main application, PDF processing, embeddings, retrieval, and conversation chain.
- `HT.py` — Custom HTML templates and CSS styling for user and assistant messages.
- `requirements.txt` — Python dependency list.
- `.env` — Local environment variables and API keys; do not upload this file.
- `venv/` — Local Python virtual environment; do not upload this folder.

## Installation and Setup

### 1. Clone the repository

### 2. Create a virtual environment

### 3. Install dependencies

### 4. Configure your Google Gemini API key

Obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Run the application

## Models

**Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`

Used to convert document text into vector embeddings for similarity search.

**Language Model:** Google Gemini, configured through LangChain's `ChatGoogleGenerativeAI`.

Used to generate responses based on retrieved document context and conversation history.

## Future Improvements

- Persistent conversation history across application restarts.
- Support for saving and reloading processed document indexes.
- Improved handling of scanned PDFs and documents without extractable text.
- Better source citations to identify which PDF pages support an answer.
- Support for multiple document collections and chat sessions.
