from fastapi import FastAPI
from pydantic import BaseModel
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

app = FastAPI()

storage_context = StorageContext.from_defaults(persist_dir="storage")

# load with ollama embeddings
embed_model = OllamaEmbedding(model_name="nomic-embed-text")
index = load_index_from_storage(storage_context, embed_model=embed_model)

llm = Ollama(model="gemma2:2b")   # ✅ lightweight model for your RTX 3050
query_engine = index.as_query_engine(llm=llm)

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask(request: QueryRequest):
    response = query_engine.query(request.query)
    return {"answer": str(response)}
