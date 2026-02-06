from app.services.openai_service import OpenAIService
from app.services.groq_service import GroqService
from app.services.mock_openai_service import MockOpenAIService
from app.models.schemas import ATSScreeningResult, ATSScanResult, SkillGapAnalysis, CandidateSummary, InterviewQuestions
from app.utils.text_cleaner import TextCleaner
from app.config import Config

class ATSAgent:
    def __init__(self):
        if Config.DEMO_MODE:
            self.llm_service = MockOpenAIService()
        elif Config.USE_GROQ:
            self.llm_service = GroqService()
        else:
            self.llm_service = OpenAIService()
        self.text_cleaner = TextCleaner()
    
    def screen_resume(self, resume_text: str, job_description: str) -> ATSScreeningResult:
        cleaned_resume = self.text_cleaner.clean_text(resume_text)
        cleaned_jd = self.text_cleaner.clean_text(job_description)
        
        prompt = self.llm_service.load_prompt(
            "ats_screening.prompt",
            resume_text=cleaned_resume,
            job_description=cleaned_jd
        )
        
        response = self.llm_service.chat_completion(prompt)
        return ATSScreeningResult(**response)
    
    def scan_resume_format(self, resume_text: str) -> ATSScanResult:
        cleaned_resume = self.text_cleaner.clean_text(resume_text)
        
        prompt = self.llm_service.load_prompt(
            "ats_scanner.prompt",
            resume_text=cleaned_resume
        )
        
        response = self.llm_service.chat_completion(prompt)
        return ATSScanResult(**response)
    
    def analyze_skill_gaps(self, resume_text: str, job_description: str) -> SkillGapAnalysis:
        cleaned_resume = self.text_cleaner.clean_text(resume_text)
        cleaned_jd = self.text_cleaner.clean_text(job_description)
        
        prompt = self.llm_service.load_prompt(
            "skill_gap.prompt",
            resume_text=cleaned_resume,
            job_description=cleaned_jd
        )
        
        response = self.llm_service.chat_completion(prompt)
        return SkillGapAnalysis(**response)
    
    def summarize_candidate(self, resume_text: str) -> CandidateSummary:
        cleaned_resume = self.text_cleaner.clean_text(resume_text)
        
        prompt = self.llm_service.load_prompt(
            "candidate_summary.prompt",
            resume_text=cleaned_resume
        )
        
        response = self.llm_service.chat_completion(prompt)
        return CandidateSummary(**response)
    
    def answer_recruiter_question(self, resume_text: str, job_description: str, question: str) -> str:
        cleaned_resume = self.text_cleaner.clean_text(resume_text)
        cleaned_jd = self.text_cleaner.clean_text(job_description)
        
        prompt = self.llm_service.load_prompt(
            "recruiter_qa.prompt",
            resume_text=cleaned_resume,
            job_description=cleaned_jd,
            question=question
        )
        
        # For Q&A, we expect a text response, not JSON
        try:
            response = self.llm_service.chat_completion(prompt)
            # If it returns JSON with an answer field, extract it
            if isinstance(response, dict) and 'answer' in response:
                return response['answer']
            # Otherwise return as string
            return str(response)
        except:
            # Fallback: call without JSON parsing
            from app.services.openai_service import OpenAIService
            if not Config.DEMO_MODE:
                service = GroqService() if Config.USE_GROQ else OpenAIService()
                resp = service.client.chat.completions.create(
                    model=Config.GROQ_MODEL if Config.USE_GROQ else Config.OPENAI_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=Config.MAX_TOKENS,
                    temperature=Config.TEMPERATURE
                )
                return resp.choices[0].message.content.strip()
            return "The candidate has relevant experience for this role."
    
    def generate_interview_questions(self, resume_text: str, job_description: str) -> InterviewQuestions:
        cleaned_resume = self.text_cleaner.clean_text(resume_text)
        cleaned_jd = self.text_cleaner.clean_text(job_description)
        
        prompt = self.llm_service.load_prompt(
            "interview_questions.prompt",
            resume_text=cleaned_resume,
            job_description=cleaned_jd
        )
        
        response = self.llm_service.chat_completion(prompt)
        return InterviewQuestions(**response)