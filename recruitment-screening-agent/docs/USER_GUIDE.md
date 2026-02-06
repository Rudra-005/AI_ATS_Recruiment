# User Guide - AI Recruitment Screening System

## Getting Started

### First Time Setup

1. **Install Application**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**
   - Open `.env` file
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_key_here
     USE_GROQ=true
     ```

3. **Launch Application**
   ```bash
   python -m streamlit run app/main.py
   ```

4. **Access Interface**
   - Open browser to `http://localhost:8501`

---

## Features Guide

### 1. Single Resume Screening

**Step-by-Step**:

1. Select **"Single Resume"** mode at the top
2. Click **"Upload Resume PDF"** button
3. Choose a PDF file from your computer
4. Paste job description in the text area
5. Click **"🚀 Start ATS Screening"**
6. Wait 5-10 seconds for processing
7. Review results:
   - ✅ SHORTLISTED or ❌ REJECTED badge
   - Overall match score
   - Skill breakdown
   - Strengths and weaknesses

**Tips**:
- Ensure PDF is text-based (not scanned image)
- Provide detailed job description for better accuracy
- Include required skills, experience level, and education requirements

---

### 2. Bulk Resume Processing

**Step-by-Step**:

1. Select **"Bulk Upload (Up to 50)"** mode
2. Click **"Upload up to 50 Resumes"**
3. Select multiple PDF files (Ctrl+Click or Cmd+Click)
4. Paste job description
5. Click **"🚀 Start ATS Screening"**
6. Watch progress bar (5-8 minutes for 50 resumes)
7. Review results:
   - Summary statistics
   - Ranking table sorted by score
   - Individual candidate details
   - Download CSV button

**Tips**:
- Maximum 50 resumes per batch
- All resumes should be for the same job role
- Use consistent naming for easy identification

---

### 3. Understanding Results

#### Score Breakdown

**Overall Match Score (0-100%)**:
- 75-100%: Strong fit (likely SHORTLIST)
- 50-74%: Moderate fit (case-by-case)
- 0-49%: Weak fit (likely REJECT)

**Component Scores**:
- **Technical Skills**: Percentage of required skills matched
- **Project Relevance**: Alignment with job requirements
- **Experience**: Years and quality of experience

#### Decision Logic

**SHORTLIST Criteria**:
- Overall score ≥ 60%
- All critical skills present
- Experience level matches
- Education requirements met

**REJECT Criteria**:
- Overall score < 60%
- Missing critical skills
- Insufficient experience
- Education mismatch

---

### 4. Skill Gap Analysis

**What It Shows**:
- **Must-Have Missing**: Critical skills preventing hire
- **Good-to-Have Missing**: Nice-to-have skills
- **Learning Recommendations**: Courses/topics to learn

**Use Cases**:
- Identify training needs for internal candidates
- Provide feedback to rejected candidates
- Plan upskilling programs

---

### 5. Interview Question Generator

**What You Get**:
- 5 Technical questions based on job requirements
- 3 Project questions about candidate's work
- 2 HR/behavioral questions

**How to Use**:
1. Screen candidate first
2. Generate questions for shortlisted candidates
3. Use in actual interviews
4. Customize as needed

---

### 6. Candidate Summary Dashboard

**Quick Overview Includes**:
- Experience level (Fresher/Junior/Mid/Senior)
- Top 3-5 key skills
- Most impressive project
- One-sentence hiring recommendation

**Best For**:
- Quick candidate reviews
- Hiring manager briefings
- Shortlist presentations

---

## Advanced Features

### Recruiter Q&A

Ask questions about candidates:
- "Does this candidate have leadership experience?"
- "How many years of Python experience?"
- "What's their biggest achievement?"

**Note**: Feature available in API, UI integration coming soon.

---

## Exporting Results

### CSV Export

**Bulk Results Include**:
- Candidate name (filename)
- Decision (SHORTLIST/REJECT)
- Overall score
- Technical score
- Project score
- Experience score
- Matched skills count
- Missing critical skills count

**How to Export**:
1. Complete bulk screening
2. Click **"📥 Download Results CSV"**
3. Open in Excel/Google Sheets
4. Sort, filter, and analyze

---

## Troubleshooting

### Common Issues

**Problem**: PDF not uploading
- **Solution**: Ensure file is valid PDF, not corrupted
- **Check**: File size < 10MB

**Problem**: Slow processing
- **Solution**: Check internet connection
- **Note**: Groq API is faster than OpenAI

**Problem**: Low accuracy
- **Solution**: Provide more detailed job description
- **Tip**: Include specific skills, years of experience

**Problem**: API quota exceeded
- **Solution**: Switch to Groq (free tier available)
- **Alternative**: Add credits to OpenAI account

---

## Best Practices

### For Recruiters

1. **Write Detailed Job Descriptions**
   - List all required skills
   - Specify experience level (e.g., "3-5 years")
   - Include education requirements
   - Mention key responsibilities

2. **Review Results Carefully**
   - Don't rely solely on scores
   - Read decision reasoning
   - Check skill gaps
   - Consider candidate potential

3. **Use Bulk Processing Efficiently**
   - Group resumes by job role
   - Process in batches of 20-30 for faster results
   - Export and share with hiring managers

### For HR Teams

1. **Standardize Process**
   - Use same job description for all candidates
   - Set minimum score thresholds
   - Document decision criteria

2. **Track Metrics**
   - Monitor shortlist rates
   - Measure time savings
   - Track hiring outcomes

3. **Provide Feedback**
   - Share skill gaps with rejected candidates
   - Offer learning recommendations
   - Maintain candidate relationships

---

## Keyboard Shortcuts

- **Ctrl/Cmd + Enter**: Submit form
- **Ctrl/Cmd + R**: Refresh page
- **Esc**: Close modals

---

## Tips for Better Results

1. **Resume Quality**
   - Use text-based PDFs (not scanned images)
   - Ensure clear formatting
   - Include contact information

2. **Job Descriptions**
   - Be specific about requirements
   - Separate required vs preferred skills
   - Include years of experience needed

3. **Batch Processing**
   - Use consistent file naming
   - Process similar roles together
   - Review top candidates first

---

## Getting Help

### Documentation
- README.md - Quick start guide
- PROJECT_DOCUMENTATION.md - Technical details
- API_REFERENCE.md - Developer guide

### Support
- Check troubleshooting section
- Review error messages
- Contact technical support

---

## Updates & New Features

Check README.md for:
- Latest version information
- New feature announcements
- Bug fixes and improvements

---

**Happy Recruiting! 🎯**
