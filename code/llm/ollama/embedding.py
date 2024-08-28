from phi.embedder.ollama import OllamaEmbedder

embedder = OllamaEmbedder(model="llama3.1")
embeddings = embedder.get_embedding("Embed me")

print(f"Embeddings: {embeddings}")
print(f"Dimensions: {len(embeddings)}")
