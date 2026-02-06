from app.services.openai_service import OpenAIService
from app.services.groq_service import GroqService
from app.services.mock_openai_service import MockOpenAIService
from app.models.schemas import JobRequirements
from app.utils.text_cleaner import TextCleaner
from app.config import Config

class JDAgent:
    def __init__(self):
        if Config.DEMO_MODE:
            self.llm_service = MockOpenAIService()
        elif Config.USE_GROQ:
            self.llm_service = GroqService()
        else:
            self.llm_service = OpenAIService()
        self.text_cleaner = TextCleaner()
    
    def process_job_description(self, job_description: str) -> JobRequirements:
        cleaned_text = self.text_cleaner.clean_text(job_description)
        prompt = self.llm_service.load_prompt("jd_extraction.prompt", job_description=cleaned_text)
        response = self.llm_service.chat_completion(prompt)
        return JobRequirements(**response)