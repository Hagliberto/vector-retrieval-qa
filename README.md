# Vector RetrievalQA com FAISS e LangChain

Esse projeto demonstra como criar um **sistema de recuperação de informações** baseado em vetores de embeddings, usando **FAISS** e **LangChain**, e responder perguntas em linguagem natural via **RetrievalQA**.

---

## 📋 Descrição

1. **Ingestão**  
   - Carrega documentos (PDF, TXT, MD).  
   - Divide em chunks de tamanho configurável.  
   - Gera embeddings com HuggingFace (modelo `all-MiniLM-L6-v2`).  
   - Indexa esses embeddings em um banco vetorial FAISS.

2. **Consulta (RetrievalQA)**  
   - Carrega o índice FAISS previamente salvo.  
   - Consulta os chunks mais relevantes via embeddings da pergunta.  
   - Usa um LLM (Ollama Llama 3.2) para sintetizar a resposta.

---

## 🚀 Como executar

### 1. Pré-requisitos

- Python 3.8+  
- Conta e setup do Ollama (se for usar OllamaLLM)  
- Variável de ambiente (opcional):  
  ```bash
  export OPENAI_API_KEY="sua_chave_aqui"
  ```

### 2. Setup

1. Clone este repositório e entre na pasta:  
   ```bash
   git clone https://github.com/SEU_USUARIO/vector-retrieval-qa.git
   cd vector-retrieval-qa
   ```

2. Crie e ative o virtualenv:  
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

### 3. Gerar o índice vetorial

Para **PDF**:  
```bash
python ingest.py data/seu_documento.pdf
```

Para **TXT/MD**:  
```bash
python ingest.py data/seu_texto.txt
```

- **Saída esperada:**  
  ```
  Gerados 256 chunks.
  ✅ Índice FAISS salvo em 'faiss_index'
  ```

### 4. Rodar o RetrievalQA

```bash
python qa.py
```

- Digite suas perguntas:  
  ```
  👉 Qual o nome do curso?
  🗒️ Resposta: Superior de Tecnologia em Sistemas para Internet.
  ```

- Para sair, digite `sair` ou `exit`.

---

## 📁 Estrutura de pastas

```
vector-retrieval-qa/
├── data/                 # Documentos para indexação (PDF, TXT, MD)
│   ├── exemplo.pdf
│   └── exemplo.txt
├── faiss_index/          # Índice gerado pelo ingest.py
├── ingest.py             # Ingestão: chunking + embeddings + FAISS
├── qa.py                 # Consulta: RetrievalQA + LLM
├── requirements.txt      # Dependências do projeto
└── README.md             # (este arquivo)
```

---

## ⚙️ Configurações e personalizações

- **Ajuste de chunking**:  
  No `ingest.py`, modifique:
  ```python
  chunk_size=1000
  chunk_overlap=50
  ```
- **Modelos de embeddings**:  
  - `all-MiniLM-L6-v2` (leve e rápido)  
  - Outros: `sentence-transformers/all-mpnet-base-v2`, etc.
- **LLM**:  
  - Ollama Llama3.2 (`llama3.2:latest`)  


---

## 🎥 Demonstração em vídeo

  1. Execução de `ingest.py` e criação do índice.  
  2. Execução de `qa.py` com perguntas e respostas.  
  3. Breve tour pelo README e estrutura de pastas.

Apresentação:  
```
Parte 1: https://www.loom.com/share/43bcf623b7c84edcbf0df6bb55a7d2c5?sid=ae8664f8-efdd-407d-b8cf-6cfcb6b758b9

0:00
Introdução ao Projeto
0:40
Configuração do Arquivo de Ingestão
1:28
Processamento e Indexação
2:36
Execução do Arquivo de Consulta

Parte 2: https://www.loom.com/share/df280efff8fe41a680037985d491879a?sid=f62e86e5-5b5e-4311-a5be-9102703341c9
0:00
Interação com o Usuário

```

---

## 📄 Licença

MIT License © Hagliberto
