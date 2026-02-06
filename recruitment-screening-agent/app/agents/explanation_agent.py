from app.services.openai_service import OpenAIService
from app.services.groq_service import GroqService
from app.services.mock_openai_service import MockOpenAIService
from app.models.schemas import ResumeData, JobRequirements, MatchingScore, ExplanationResult
from app.config import Config

class ExplanationAgent:
    def __init__(self):
        if Config.DEMO_MODE:
            self.llm_service = MockOpenAIService()
        elif Config.USE_GROQ:
            self.llm_service = GroqService()
        else:
            self.llm_service = OpenAIService()
    
    def generate_explanation(self, resume_data: ResumeData, job_requirements: JobRequirements, matching_results: MatchingScore) -> ExplanationResult:
        prompt = self.llm_service.load_prompt(
            "explanation.prompt",
            resume_data=resume_data.model_dump(),
            job_requirements=job_requirements.model_dump(),
            matching_results=matching_results.model_dump()
        )
        
        response = self.llm_service.chat_completion(prompt)
        return ExplanationResult(**response)