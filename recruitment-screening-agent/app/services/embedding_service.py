from app.services.openai_service import OpenAIService
import numpy as np
from typing import List

class EmbeddingService:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    def get_embedding(self, text: str) -> List[float]:
        return self.openai_service.generate_embedding(text)
    
    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        v1 = np.array(vec1)
        v2 = np.array(vec2)
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))