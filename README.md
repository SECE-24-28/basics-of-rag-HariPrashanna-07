# RAG Chatbot using Llama3 + FAISS + LangChain

## Overview

This project implements a Retrieval-Augmented Generation (RAG)
chatbot using:

- Llama3 (Ollama)
- FAISS Vector Database
- Sentence Transformers
- LangChain

The chatbot retrieves relevant information from local documents
before generating responses.

---

## Features

- Local LLM (Llama3)
- FAISS vector search
- Semantic retrieval
- Fast document indexing
- Offline operation
- Easy to extend

---

## Architecture

User Query
     |
     V
FAISS Retrieval
     |
     V
Relevant Chunks
     |
     V
Llama3 Prompt
     |
     V
Generated Answer

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourname/rag-chatbot.git
cd rag-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download:

https://ollama.com

### Pull Model

```bash
ollama pull llama3
```

---

## Add Documents

Place all .txt files inside:

```text
data/
```

---

## Create Embeddings

```bash
python ingest.py
```

This creates:

```text
vector_db/
```

containing the FAISS index.

---

## Run Chatbot

```bash
python chatbot.py
```

---

## Example

```text
You: What is RAG?

Bot: RAG stands for Retrieval-Augmented Generation. It combines information retrieval and language models to generate accurate answers using retrieved context.
```

---

## Technologies Used

- Python
- LangChain
- FAISS
- Ollama
- Llama3
- Sentence Transformers

---

## Future Improvements

- PDF Support
- Web Interface
- Chat History
- Hybrid Search
- Reranking
- Multi-document Retrieval
- API Deployment
- Docker Support

---

## License

MIT License
