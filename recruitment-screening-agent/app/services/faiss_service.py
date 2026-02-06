import faiss
import numpy as np
import pickle
import os
from typing import List, Tuple
from app.config import Config

class FAISSService:
    def __init__(self, dimension: int = 1536):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)
        self.texts = []
        self.index_path = Config.FAISS_INDEX_PATH
        self.load_index()
    
    def add_vectors(self, vectors: List[List[float]], texts: List[str]):
        vectors_np = np.array(vectors, dtype=np.float32)
        faiss.normalize_L2(vectors_np)
        self.index.add(vectors_np)
        self.texts.extend(texts)
        self.save_index()
    
    def search(self, query_vector: List[float], k: int = 5) -> List[Tuple[str, float]]:
        query_np = np.array([query_vector], dtype=np.float32)
        faiss.normalize_L2(query_np)
        scores, indices = self.index.search(query_np, min(k, self.index.ntotal))
        return [(self.texts[idx], float(score)) for score, idx in zip(scores[0], indices[0]) if idx < len(self.texts)]
    
    def similarity_score(self, vec1: List[float], vec2: List[float]) -> float:
        v1 = np.array(vec1, dtype=np.float32)
        v2 = np.array(vec2, dtype=np.float32)
        v1 = v1 / np.linalg.norm(v1)
        v2 = v2 / np.linalg.norm(v2)
        return max(0.0, min(1.0, float(np.dot(v1, v2))))
    
    def save_index(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.index_path + ".texts", "wb") as f:
            pickle.dump(self.texts, f)
    
    def load_index(self):
        if os.path.exists(self.index_path) and os.path.exists(self.index_path + ".texts"):
            self.index = faiss.read_index(self.index_path)
            with open(self.index_path + ".texts", "rb") as f:
                self.texts = pickle.load(f)