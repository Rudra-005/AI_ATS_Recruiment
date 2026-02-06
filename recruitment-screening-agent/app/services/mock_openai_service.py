import json
import time
from typing import Dict, Any, List

class MockOpenAIService:
    def __init__(self):
        self.responses = {
            "resume_compression.prompt": {
                "skills": ["Python", "JavaScript", "React", "SQL", "AWS"],
                "experience": "5 years software development experience",
                "education": "Bachelor's in Computer Science",
                "summary": "Experienced full-stack developer with cloud expertise"
            },
            "jd_extraction.prompt": {
                "required_skills": ["Python", "React", "SQL"],
                "preferred_skills": ["AWS", "Docker", "Kubernetes"],
                "experience_level": "3-5 years",
                "education_requirements": "Bachelor's degree in Computer Science",
                "job_summary": "Full-stack developer position"
            },
            "matching_reasoning.prompt": {
                "overall_score": 82.5,
                "skills_match": 85.0,
                "experience_match": 80.0,
                "education_match": 85.0,
                "reasoning": "Strong technical skills match with 4/5 required skills. Experience aligns well with requirements."
            },
            "explanation.prompt": {
                "strengths": ["Strong Python skills", "Relevant React experience", "Cloud knowledge"],
                "gaps": ["Missing Docker experience", "No Kubernetes background"],
                "recommendations": ["Learn Docker containerization", "Get Kubernetes certification"],
                "fit_assessment": "Good technical fit with some skill gaps to address"
            },
            "ats_screening.prompt": {
                "overall_match_score": 78.0,
                "technical_skill_match": 82.0,
                "project_relevance_score": 75.0,
                "experience_score": 80.0,
                "matched_skills": ["Python", "JavaScript", "React", "SQL"],
                "missing_critical_skills": ["Docker"],
                "nice_to_have_missing_skills": ["Kubernetes", "CI/CD"],
                "strengths": ["Strong full-stack development experience", "Proven track record with modern frameworks", "Cloud platform expertise"],
                "weaknesses": ["Limited containerization experience", "No DevOps background mentioned"],
                "final_decision": "SHORTLIST",
                "decision_reason": "Candidate demonstrates strong technical foundation with 5 years of relevant experience. Core skills align well with job requirements. While missing some DevOps tools, the candidate's solid programming background and cloud experience make them a viable fit for the role."
            },
            "ats_scanner.prompt": {
                "ats_score": 85.0,
                "ats_issues": ["Missing quantifiable achievements", "Skills section could be more prominent"],
                "improvement_suggestions": ["Add metrics to project descriptions", "Use bullet points for better readability", "Include keywords from job description"]
            },
            "skill_gap.prompt": {
                "must_have_missing_skills": ["Docker", "Kubernetes"],
                "good_to_have_missing_skills": ["CI/CD", "Jenkins", "Terraform"],
                "learning_recommendations": ["Docker & Kubernetes Fundamentals Course", "DevOps CI/CD Pipeline Tutorial", "Infrastructure as Code with Terraform"]
            },
            "candidate_summary.prompt": {
                "candidate_level": "Mid",
                "key_expertise": ["Full-stack Development", "React", "Python", "Cloud Architecture", "SQL"],
                "most_impressive_project": "Built scalable e-commerce platform handling 10K+ daily users with microservices architecture",
                "hiring_recommendation": "Strong mid-level candidate with proven full-stack expertise and cloud experience, ideal for teams building modern web applications."
            },
            "interview_questions.prompt": {
                "technical_questions": [
                    "Explain how you would implement Docker containerization for your e-commerce project",
                    "Describe your experience with Kubernetes orchestration",
                    "How do you handle database scaling in high-traffic applications?",
                    "Walk me through your CI/CD pipeline setup",
                    "What's your approach to microservices communication?"
                ],
                "project_questions": [
                    "Tell me about the architecture decisions in your e-commerce platform",
                    "How did you handle 10K+ daily users - what challenges did you face?",
                    "What would you do differently if you rebuilt this project today?"
                ],
                "hr_questions": [
                    "Why are you interested in learning DevOps technologies?",
                    "How do you stay updated with new technologies in your field?"
                ]
            }
        }
    
    def chat_completion(self, prompt: str, max_retries: int = 3) -> Dict[str, Any]:
        time.sleep(1)
        
        # Extract prompt filename from the prompt
        for prompt_file, response in self.responses.items():
            if prompt_file in prompt:
                return response
        
        # Default fallback
        return self.responses["ats_screening.prompt"]
    
    def generate_embedding(self, text: str, max_retries: int = 3) -> List[float]:
        return [0.1] * 1536
    
    def load_prompt(self, prompt_file: str, **kwargs) -> str:
        with open(f"app/prompts/{prompt_file}", 'r') as f:
            content = f.read().format(**kwargs)
        return f"{prompt_file}\n{content}"