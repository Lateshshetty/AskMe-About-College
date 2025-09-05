from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.embeddings.ollama import OllamaEmbedding


embed_model = OllamaEmbedding(model_name="nomic-embed-text")  

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,  
)

index.storage_context.persist("storage")
