# API Reference Guide

## ATSAgent API

### Overview
The ATSAgent class provides 6 core methods for resume screening and analysis.

---

## Methods

### 1. screen_resume()

Complete ATS screening with hiring decision.

**Signature**:
```python
def screen_resume(resume_text: str, job_description: str) -> ATSScreeningResult
```

**Parameters**:
- `resume_text` (str): Full text extracted from resume PDF
- `job_description` (str): Complete job description text

**Returns**: `ATSScreeningResult` object with:
- `overall_match_score`: float (0-100)
- `technical_skill_match`: float (0-100)
- `project_relevance_score`: float (0-100)
- `experience_score`: float (0-100)
- `matched_skills`: List[str]
- `missing_critical_skills`: List[str]
- `nice_to_have_missing_skills`: List[str]
- `strengths`: List[str]
- `weaknesses`: List[str]
- `final_decision`: "SHORTLIST" or "REJECT"
- `decision_reason`: str

**Example**:
```python
from app.agents.ats_agent import ATSAgent

agent = ATSAgent()
result = agent.screen_resume(
    resume_text="John Doe, 5 years Python developer...",
    job_description="Looking for Senior Python Developer..."
)

print(f"Decision: {result.final_decision}")
print(f"Score: {result.overall_match_score}%")
print(f"Reason: {result.decision_reason}")
```

---

### 2. scan_resume_format()

Evaluate resume ATS-friendliness and formatting.

**Signature**:
```python
def scan_resume_format(resume_text: str) -> ATSScanResult
```

**Parameters**:
- `resume_text` (str): Resume text to analyze

**Returns**: `ATSScanResult` object with:
- `ats_score`: float (0-100)
- `ats_issues`: List[str]
- `improvement_suggestions`: List[str]

**Example**:
```python
scan = agent.scan_resume_format(resume_text)
print(f"ATS Score: {scan.ats_score}%")
for issue in scan.ats_issues:
    print(f"Issue: {issue}")
```

---

### 3. analyze_skill_gaps()

Identify missing skills and provide learning recommendations.

**Signature**:
```python
def analyze_skill_gaps(resume_text: str, job_description: str) -> SkillGapAnalysis
```

**Parameters**:
- `resume_text` (str): Candidate's resume
- `job_description` (str): Job requirements

**Returns**: `SkillGapAnalysis` object with:
- `must_have_missing_skills`: List[str]
- `good_to_have_missing_skills`: List[str]
- `learning_recommendations`: List[str]

**Example**:
```python
gaps = agent.analyze_skill_gaps(resume_text, job_description)
print("Critical Missing Skills:")
for skill in gaps.must_have_missing_skills:
    print(f"- {skill}")
print("\nRecommended Learning:")
for rec in gaps.learning_recommendations:
    print(f"- {rec}")
```

---

### 4. summarize_candidate()

Generate quick candidate summary for dashboard.

**Signature**:
```python
def summarize_candidate(resume_text: str) -> CandidateSummary
```

**Parameters**:
- `resume_text` (str): Resume to summarize

**Returns**: `CandidateSummary` object with:
- `candidate_level`: str ("Fresher", "Junior", "Mid", "Senior")
- `key_expertise`: List[str]
- `most_impressive_project`: str
- `hiring_recommendation`: str

**Example**:
```python
summary = agent.summarize_candidate(resume_text)
print(f"Level: {summary.candidate_level}")
print(f"Expertise: {', '.join(summary.key_expertise)}")
print(f"Recommendation: {summary.hiring_recommendation}")
```

---

### 5. generate_interview_questions()

Create personalized interview questions.

**Signature**:
```python
def generate_interview_questions(resume_text: str, job_description: str) -> InterviewQuestions
```

**Parameters**:
- `resume_text` (str): Candidate's resume
- `job_description` (str): Job requirements

**Returns**: `InterviewQuestions` object with:
- `technical_questions`: List[str] (5 questions)
- `project_questions`: List[str] (3 questions)
- `hr_questions`: List[str] (2 questions)

**Example**:
```python
questions = agent.generate_interview_questions(resume_text, job_description)
print("Technical Questions:")
for q in questions.technical_questions:
    print(f"- {q}")
```

---

### 6. answer_recruiter_question()

Interactive Q&A about candidates.

**Signature**:
```python
def answer_recruiter_question(resume_text: str, job_description: str, question: str) -> str
```

**Parameters**:
- `resume_text` (str): Candidate's resume
- `job_description` (str): Job requirements
- `question` (str): Recruiter's question

**Returns**: str (Answer text)

**Example**:
```python
answer = agent.answer_recruiter_question(
    resume_text,
    job_description,
    "Does this candidate have leadership experience?"
)
print(answer)
```

---

## Error Handling

All methods may raise:
- `ValueError`: Invalid input or JSON parsing error
- `Exception`: API errors, network issues, or service failures

**Example**:
```python
try:
    result = agent.screen_resume(resume_text, job_description)
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"Processing error: {e}")
```

---

## Configuration

Set environment variables in `.env`:

```env
GROQ_API_KEY=your_key_here
USE_GROQ=true
DEMO_MODE=false
```

---

## Rate Limits

- **Groq Free Tier**: 30 requests/minute
- **OpenAI**: Based on account tier
- Implement exponential backoff for retries

---

## Best Practices

1. **Clean Input**: Use TextCleaner before processing
2. **Error Handling**: Always wrap calls in try-except
3. **Batch Processing**: Process multiple resumes in parallel
4. **Caching**: Cache results for repeated queries
5. **Monitoring**: Log API usage and errors
