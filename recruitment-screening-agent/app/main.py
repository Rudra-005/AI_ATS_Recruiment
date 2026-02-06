import streamlit as st
import pandas as pd
from app.utils.pdf_parser import PDFParser
from app.agents.ats_agent import ATSAgent
from app.config import Config
import time

st.set_page_config(page_title="AI ATS Recruitment", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem;
        animation: fadeIn 1s;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem;
        font-size: 1.1rem;
        border-radius: 10px;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        animation: slideIn 0.5s;
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    .shortlist-badge {
        background: #10b981;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
    }
    .reject-badge {
        background: #ef4444;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def process_resume(resume_file, job_description, ats_agent):
    resume_text = PDFParser.extract_text(resume_file)
    result = ats_agent.screen_resume(resume_text, job_description)
    return {'filename': resume_file.name, 'result': result}

def main():
    st.markdown('<h1 class="main-header">🎯 AI-Powered ATS Recruitment System</h1>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.header("⚙️ Configuration")
        if Config.DEMO_MODE:
            st.info("🔧 DEMO MODE")
        elif Config.USE_GROQ:
            st.success("⚡ Groq API")
        else:
            st.success("🤖 OpenAI API")
        
        st.markdown("---")
        st.markdown("### 📊 ATS Features")
        st.markdown("✅ Strict Recruiter Analysis")
        st.markdown("✅ Skill Gap Detection")
        st.markdown("✅ SHORTLIST/REJECT Decision")
        st.markdown("✅ Bulk Processing (50)")
        st.markdown("✅ Export Rankings")
    
    mode = st.radio("📋 Select Mode", ["Single Resume", "Bulk Upload (Up to 50)"], horizontal=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📄 Resume Upload")
        if mode == "Single Resume":
            resume_files = st.file_uploader("Upload Resume PDF", type=['pdf'], accept_multiple_files=False)
            resume_files = [resume_files] if resume_files else []
        else:
            resume_files = st.file_uploader("Upload up to 50 Resumes", type=['pdf'], accept_multiple_files=True)
            if len(resume_files) > 50:
                st.error("⚠️ Maximum 50 resumes")
                resume_files = resume_files[:50]
            if resume_files:
                st.success(f"✅ {len(resume_files)} resume(s) uploaded")
    
    with col2:
        st.markdown("### 📋 Job Description")
        job_description = st.text_area("Enter detailed job requirements", height=200, placeholder="Required skills, experience, education...")
    
    if st.button("🚀 Start ATS Screening", type="primary"):
        if not resume_files or not job_description.strip():
            st.error("❌ Provide resume(s) and job description")
            return
        
        try:
            with st.spinner("🔧 Initializing ATS Agent..."):
                ats_agent = ATSAgent()
            
            results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for idx, resume_file in enumerate(resume_files):
                status_text.text(f"🔍 Screening {resume_file.name} ({idx+1}/{len(resume_files)})...")
                result = process_resume(resume_file, job_description, ats_agent)
                results.append(result)
                progress_bar.progress((idx + 1) / len(resume_files))
                time.sleep(0.1)
            
            progress_bar.empty()
            status_text.empty()
            st.success(f"✅ Screening completed for {len(results)} candidate(s)!")
            
            if mode == "Single Resume":
                display_single_result(results[0])
            else:
                display_bulk_results(results)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

def display_single_result(data):
    result = data['result']
    st.markdown("---")
    st.markdown("## 📊 ATS Screening Result")
    
    # Decision badge
    if result.final_decision == "SHORTLIST":
        st.markdown('<div class="shortlist-badge">✅ SHORTLISTED</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="reject-badge">❌ REJECTED</div>', unsafe_allow_html=True)
    
    st.info(f"**Recruiter Decision:** {result.decision_reason}")
    
    # Score cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h2>🎯</h2>
            <h1>{result.overall_match_score:.1f}%</h1>
            <p>Overall Match</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h2>💻</h2>
            <h1>{result.technical_skill_match:.1f}%</h1>
            <p>Technical Skills</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h2>📁</h2>
            <h1>{result.project_relevance_score:.1f}%</h1>
            <p>Project Relevance</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h2>⏱️</h2>
            <h1>{result.experience_score:.1f}%</h1>
            <p>Experience</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Skills analysis
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### ✅ Matched Skills")
        for skill in result.matched_skills:
            st.success(f"✓ {skill}")
    
    with col2:
        st.markdown("### ❌ Missing Critical")
        for skill in result.missing_critical_skills:
            st.error(f"✗ {skill}")
    
    with col3:
        st.markdown("### ⚠️ Nice-to-Have Missing")
        for skill in result.nice_to_have_missing_skills:
            st.warning(f"○ {skill}")
    
    # Strengths & Weaknesses
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💪 Strengths")
        for strength in result.strengths:
            st.markdown(f"✅ {strength}")
    
    with col2:
        st.markdown("### 🔍 Weaknesses")
        for weakness in result.weaknesses:
            st.markdown(f"⚠️ {weakness}")

def display_bulk_results(results):
    st.markdown("---")
    st.markdown("## 📊 Bulk ATS Screening Results")
    
    # Summary
    shortlisted = sum(1 for r in results if r['result'].final_decision == "SHORTLIST")
    rejected = len(results) - shortlisted
    avg_score = sum(r['result'].overall_match_score for r in results) / len(results)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Total Screened", len(results))
    with col2:
        st.metric("✅ Shortlisted", shortlisted)
    with col3:
        st.metric("❌ Rejected", rejected)
    with col4:
        st.metric("📈 Avg Score", f"{avg_score:.1f}%")
    
    # Results table
    df_data = []
    for data in results:
        r = data['result']
        df_data.append({
            'Candidate': data['filename'],
            'Decision': r.final_decision,
            'Overall': f"{r.overall_match_score:.1f}%",
            'Technical': f"{r.technical_skill_match:.1f}%",
            'Projects': f"{r.project_relevance_score:.1f}%",
            'Experience': f"{r.experience_score:.1f}%",
            'Matched Skills': len(r.matched_skills),
            'Missing Critical': len(r.missing_critical_skills)
        })
    
    df = pd.DataFrame(df_data)
    df = df.sort_values('Overall', ascending=False)
    
    st.markdown("### 📋 Candidate Rankings")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    csv = df.to_csv(index=False)
    st.download_button("📥 Download Results CSV", csv, "ats_results.csv", "text/csv")
    
    # Individual details
    st.markdown("### 👥 Detailed Candidate Analysis")
    for idx, data in enumerate(sorted(results, key=lambda x: x['result'].overall_match_score, reverse=True)):
        r = data['result']
        badge = "🟢 SHORTLIST" if r.final_decision == "SHORTLIST" else "🔴 REJECT"
        with st.expander(f"{idx+1}. {data['filename']} - {r.overall_match_score:.1f}% - {badge}"):
            st.info(r.decision_reason)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Strengths:**")
                for s in r.strengths:
                    st.markdown(f"✅ {s}")
            with col2:
                st.markdown("**Weaknesses:**")
                for w in r.weaknesses:
                    st.markdown(f"⚠️ {w}")

if __name__ == "__main__":
    main()
