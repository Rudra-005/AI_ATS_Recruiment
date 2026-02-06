from app.services.openai_service import OpenAIService
from app.services.groq_service import GroqService
from app.services.mock_openai_service import MockOpenAIService
from app.models.schemas import ResumeData
from app.utils.text_cleaner import TextCleaner
from app.config import Config

class ResumeAgent:
    def __init__(self):
        if Config.DEMO_MODE:
            self.llm_service = MockOpenAIService()
        elif Config.USE_GROQ:
            self.llm_service = GroqService()
        else:
            self.llm_service = OpenAIService()
        self.text_cleaner = TextCleaner()
    
    def process_resume(self, resume_text: str) -> ResumeData:
        cleaned_text = self.text_cleaner.clean_text(resume_text)
        prompt = self.llm_service.load_prompt("resume_compression.prompt", resume_text=cleaned_text)
        response = self.llm_service.chat_completion(prompt)
        return ResumeData(**response)