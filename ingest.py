import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_FOLDER = "data"
VECTOR_DB = "vector_db"

documents = []

for file in os.listdir(DATA_FOLDER):
    path = os.path.join(DATA_FOLDER, file)

    if file.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            documents.append(f.read())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = []

for doc in documents:
    chunks.extend(text_splitter.split_text(doc))

print(f"Total Chunks: {len(chunks)}")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_texts(
    chunks,
    embedding_model
)

db.save_local(VECTOR_DB)

print("Vector Database Created Successfully!")
