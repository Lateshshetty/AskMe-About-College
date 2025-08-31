# 🤖 AskMe About College

A **FastAPI-powered chatbot** that uses **LlamaIndex** with **Ollama
embeddings** and a lightweight **Gemma2 model** to answer
**college-related queries**.\
This bot runs **fully offline**---no OpenAI API keys needed---and is
optimized for systems with an **RTX 3050** or equivalent GPU.

You can **add your own college's documents** (like admission details,
courses, staff info) to make the bot specific to your institution! 🎓

------------------------------------------------------------------------

## 🚀 Features

✅ **FastAPI Backend** with `/ask` endpoint\
✅ **Ollama Models** for embeddings & LLM inference (no cloud
dependencies)\
✅ **Persistent Vector Index** (no need to rebuild on every run)\
✅ **Swagger UI Docs** for easy API testing\
✅ **Lightweight & GPU-Friendly**\
✅ **Customizable Data** --- add your own PDFs, docs, or notes

------------------------------------------------------------------------

## 📂 Project Structure

    AskMe-About-College/
    │
    ├── data/                 <-- Place your own text/PDF files here
    ├── storage/              <-- Generated vector index (auto-created)
    ├── app.py                <-- FastAPI server code
    ├── build_index.py        <-- Script to build the document index
    ├── requirements.txt      <-- Python dependencies
    └── .venv/                <-- Virtual environment (optional)

------------------------------------------------------------------------

## 🖥️ 1. Installed Software

Before running the project, install:\
- [Python 3.10+](https://www.python.org/downloads/) (3.13 works fine)\
- [pip](https://pip.pypa.io/) (comes with Python)\
- [Ollama](https://ollama.ai) (desktop app; runs models locally on port
`11434`)\
- VS Code or your favorite editor (optional)\
- Git (optional for version control)

------------------------------------------------------------------------

## 🔧 2. Create a Python Virtual Environment

``` powershell
cd "C:\Users\Lates\OneDrive\Documents\AskMe-About-College"
python -m venv .venv
.venv\Scripts\activate
```

------------------------------------------------------------------------

## 📦 3. Install Python Dependencies

Make sure `requirements.txt` includes:

    fastapi
    uvicorn
    llama-index
    llama-index-llms-ollama
    llama-index-embeddings-ollama

Then install them:

``` powershell
pip install -r requirements.txt
```

💡 Update requirements if needed:

``` powershell
pip freeze > requirements.txt
```

------------------------------------------------------------------------

## 🧠 4. Download Ollama Models

Run these commands **once**:

``` powershell
ollama pull gemma2:2b
ollama pull nomic-embed-text
```

------------------------------------------------------------------------

## 📥 5. Add Your Own Data

Put all your **college-specific documents** (admission info, courses,
staff details, etc.) inside the `data/` folder:

    AskMe-About-College/data/
    │
    ├── admission.txt
    ├── courses.pdf
    └── staff.txt

You can add, edit, or replace these files anytime to make the bot
**specific to your own college**.

------------------------------------------------------------------------

## 🏗️ 6. Build the Index

This step reads your documents, converts them to vector embeddings, and
saves them in `storage/`.

``` powershell
python build_index.py
```

You only need to run this again **if you add or update documents**.

------------------------------------------------------------------------

## 🚀 7. Run the API Server

Make sure Ollama is running (it auto-starts when models are used).

``` powershell
uvicorn app:app --reload --port 8000
```

Access your API:\
<http://127.0.0.1:8000>

------------------------------------------------------------------------

## 📜 8. Test the API

Visit:\
<http://127.0.0.1:8000/docs>

Use the `/ask` endpoint:

``` json
{
  "query": "What is the admission process?"
}
```

Sample response:

``` json
{
  "answer": "The admission process involves..."
}
```

------------------------------------------------------------------------

## 🔥 Quick Start Script (Optional)

Create a `start.bat` for one-click setup & launch:

``` bat
@echo off
cd /d "C:\Users\Lates\OneDrive\Documents\AskMe-About-College"
call .venv\Scripts\activate
pip install -r requirements.txt
ollama pull gemma2:2b
ollama pull nomic-embed-text
python build_index.py
uvicorn app:app --reload --port 8000
```

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Technology       Purpose
  ---------------- ------------------------------------
  **FastAPI**      REST API backend
  **Uvicorn**      ASGI server for FastAPI
  **LlamaIndex**   Vector store and query engine
  **Ollama**       Local LLM inference & embeddings
  **Gemma2:2b**    Lightweight LLM for RTX-class GPUs

------------------------------------------------------------------------

## 🎯 How to Customize for Your College

-   Add your **college's documents** (admission brochures, syllabus,
    staff details) to the `data/` folder.\
-   Run `python build_index.py` to re-index data.\
-   Start the server and your bot will now answer based on your custom
    data.

------------------------------------------------------------------------

## 🌐 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/latesh-shetty-ab0a70308/)\
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/iam_latesh/)
