from app.services.openai_service import OpenAIService
from app.services.groq_service import GroqService
from app.services.mock_openai_service import MockOpenAIService
from app.services.embedding_service import EmbeddingService
from app.services.faiss_service import FAISSService
from app.models.schemas import ResumeData, JobRequirements, MatchingScore
from app.config import Config

class MatchingAgent:
    def __init__(self):
        if Config.DEMO_MODE:
            self.llm_service = MockOpenAIService()
        elif Config.USE_GROQ:
            self.llm_service = GroqService()
        else:
            self.llm_service = OpenAIService()
        self.embedding_service = EmbeddingService()
        self.faiss_service = FAISSService()
    
    def calculate_match_score(self, resume_data: ResumeData, job_requirements: JobRequirements) -> MatchingScore:
        if not Config.DEMO_MODE and not Config.USE_GROQ:
            semantic_score = self._calculate_semantic_similarity(resume_data, job_requirements)
        else:
            semantic_score = 0.8
        
        prompt = self.llm_service.load_prompt(
            "matching_reasoning.prompt",
            resume_data=resume_data.model_dump(),
            job_requirements=job_requirements.model_dump()
        )
        
        response = self.llm_service.chat_completion(prompt)
        if not Config.DEMO_MODE and not Config.USE_GROQ:
            response['overall_score'] = (response['overall_score'] + semantic_score * 100) / 2
        
        return MatchingScore(**response)
    
    def _calculate_semantic_similarity(self, resume_data: ResumeData, job_requirements: JobRequirements) -> float:
        resume_text = f"{resume_data.summary} {' '.join(resume_data.skills)} {resume_data.experience}"
        job_text = f"{job_requirements.job_summary} {' '.join(job_requirements.required_skills)} {' '.join(job_requirements.preferred_skills)}"
        
        resume_embedding = self.embedding_service.get_embedding(resume_text)
        job_embedding = self.embedding_service.get_embedding(job_text)
        
        return self.faiss_service.similarity_score(resume_embedding, job_embedding)