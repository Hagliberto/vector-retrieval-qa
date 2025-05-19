# ingest.py

import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_documents(path: str):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(path)
    elif ext in (".txt", ".md"):
        loader = TextLoader(path, encoding="utf-8")
    else:
        raise ValueError(f"Formato não suportado: {ext}")
    return loader.load_and_split()

def build_vector_db(input_path: str, index_path: str = "faiss_index"):
    # 1) Carrega e divide em chunks
    docs = load_documents(input_path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len
    )
    chunks = splitter.split_documents(docs)
    print(f"Gerados {len(chunks)} chunks.")

    # 2) Cria embeddings e constrói o índice FAISS
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)

    # 3) Salva o índice localmente
    db.save_local(index_path)
    print(f"✅ Índice FAISS salvo em '{index_path}'")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python ingest.py <caminho para PDF ou TXT>")
        sys.exit(1)
    build_vector_db(sys.argv[1])
