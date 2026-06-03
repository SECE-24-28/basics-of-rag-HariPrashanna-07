from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import ollama

VECTOR_DB = "vector_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    VECTOR_DB,
    embedding_model,
    allow_dangerous_deserialization=True
)

print("=" * 50)
print("RAG Chatbot Using Llama3")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    docs = db.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    print("\nBot:", answer)
