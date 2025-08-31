from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.embeddings.ollama import OllamaEmbedding

# use Ollama embeddings instead of OpenAI
embed_model = OllamaEmbedding(model_name="nomic-embed-text")  

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,   # ✅ force Ollama embeddings
)

index.storage_context.persist("storage")
