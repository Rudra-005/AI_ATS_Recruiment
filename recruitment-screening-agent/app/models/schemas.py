from pydantic import BaseModel, Field, field_validator
from typing import List

class ResumeData(BaseModel):
    skills: List[str]
    experience: str
    education: str
    summary: str
    
    @field_validator('skills')
    def validate_skills(cls, v):
        filtered = [skill.strip() for skill in v if skill.strip()]
        if not filtered:
            raise ValueError("At least one skill required")
        return filtered
    
    @field_validator('experience', 'education', 'summary')
    def validate_strings(cls, v):
        return v.strip() if v and v.strip() else "Not specified"

class JobRequirements(BaseModel):
    required_skills: List[str]
    preferred_skills: List[str] = []
    experience_level: str
    education_requirements: str
    job_summary: str
    
    @field_validator('required_skills', 'preferred_skills')
    def validate_skills(cls, v):
        return [skill.strip() for skill in v if skill.strip()]
    
    @field_validator('experience_level', 'education_requirements', 'job_summary')
    def validate_strings(cls, v):
        return v.strip() if v and v.strip() else "Not specified"

class ATSScreeningResult(BaseModel):
    overall_match_score: float = Field(ge=0, le=100)
    technical_skill_match: float = Field(ge=0, le=100)
    project_relevance_score: float = Field(ge=0, le=100)
    experience_score: float = Field(ge=0, le=100)
    matched_skills: List[str]
    missing_critical_skills: List[str]
    nice_to_have_missing_skills: List[str]
    strengths: List[str]
    weaknesses: List[str]
    final_decision: str
    decision_reason: str
    
    @field_validator('final_decision')
    def validate_decision(cls, v):
        if v.upper() not in ['SHORTLIST', 'REJECT']:
            return 'REJECT'
        return v.upper()

class ATSScanResult(BaseModel):
    ats_score: float = Field(ge=0, le=100)
    ats_issues: List[str]
    improvement_suggestions: List[str]

class SkillGapAnalysis(BaseModel):
    must_have_missing_skills: List[str]
    good_to_have_missing_skills: List[str]
    learning_recommendations: List[str]

class CandidateSummary(BaseModel):
    candidate_level: str
    key_expertise: List[str]
    most_impressive_project: str
    hiring_recommendation: str

class InterviewQuestions(BaseModel):
    technical_questions: List[str]
    project_questions: List[str]
    hr_questions: List[str]

class MatchingScore(BaseModel):
    overall_score: float = Field(ge=0, le=100)
    skills_match: float = Field(ge=0, le=100)
    experience_match: float = Field(ge=0, le=100)
    education_match: float = Field(ge=0, le=100)
    reasoning: str
    
    @field_validator('reasoning')
    def validate_reasoning(cls, v):
        return v.strip() if v and v.strip() else "Analysis completed"

class ExplanationResult(BaseModel):
    strengths: List[str]
    gaps: List[str] = []
    recommendations: List[str]
    fit_assessment: str
    
    @field_validator('strengths', 'recommendations')
    def validate_lists(cls, v):
        filtered = [item.strip() for item in v if item and item.strip()]
        if not filtered:
            return ["Not specified"]
        return filtered
    
    @field_validator('fit_assessment')
    def validate_assessment(cls, v):
        return v.strip() if v and v.strip() else "Assessment completed"