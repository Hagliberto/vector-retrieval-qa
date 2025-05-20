# qa.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.chains import RetrievalQA

def load_db(index_path: str = "faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

def main():
    db = load_db()
    llm = OllamaLLM(model="llama3.2:latest")
    retriever = db.as_retriever(search_kwargs={"k": 5})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    print("Digite sua pergunta (ou 'sair'):")
    while True:
        query = input("👉 ")
        if query.lower() in ("sair", "exit"):
            break
        response = qa_chain.invoke({"query": query})
        print("\n🗒️ Resposta:", response["result"], "\n")

if __name__ == "__main__":
    main()
