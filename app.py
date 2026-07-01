import streamlit as st
from utils.preprocess import preprocess_text
from utils.matcher import calculate_ats_score
from utils.skills import extract_skills, skill_match
from utils.llm_utils import generate_resume_summary
from utils.llm_utils import generate_interview_questions
from utils.career_recommender import recommend_career
from utils.job_recommender import recommend_jobs
from utils.job_api import search_jobs
import os

from utils.parser import extract_resume_text


# ---------------------------------
# Streamlit Page Config
# ---------------------------------

st.set_page_config(
    page_title="Resume Screening Chatbot",
    page_icon="📄",
    layout="centered"
)


# ---------------------------------
# Better UI Title
# ---------------------------------

st.markdown(
    """
    # 📄 Resume Screening Chatbot

    Upload your resume and analyze ATS compatibility.
    """
)


# ---------------------------------
# File Uploader
# ---------------------------------

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)
# ---------------------------------
# Job Description Input
# ---------------------------------

st.subheader("📋 Enter Job Description")

job_description = st.text_area(
    "Paste Job Description Here",
    height=250
)
# ---------------------------------
# Extract Resume Text
# ---------------------------------

if uploaded_resume is not None and job_description:

    st.success("Resume Uploaded Successfully ✅")


    # ---------------------------------
    # Save Uploaded Resume
    # ---------------------------------

    save_path = os.path.join(
        "resumes",
        uploaded_resume.name
    )

    with open(save_path, "wb") as f:

        f.write(uploaded_resume.getbuffer())
    
    # ---------------------------------
    # Extract Resume Text
    # ---------------------------------

    resume_text = extract_resume_text(uploaded_resume)
    cleaned_resume = preprocess_text(resume_text)
    # Clean Job Description
    cleaned_jd = preprocess_text(job_description)


    # Calculate ATS Score
    ats_score = calculate_ats_score(
        cleaned_resume,
        cleaned_jd
    )


    # ---------------------------------
    # Display Resume Text
    # ---------------------------------

    st.subheader("📜 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )


    # ---------------------------------
    # Display Cleaned Resume Text
    # ---------------------------------

    st.subheader("🧹 Cleaned Resume Text")

    st.text_area(
        "Cleaned Resume",
        cleaned_resume,
        height=300
    )
    # ---------------------------------
    # Display ATS Score
    # ---------------------------------

    if ats_score >= 75:

        st.success(f"Excellent Match: {ats_score}%")

    elif ats_score >= 50:

        st.warning(f"Average Match: {ats_score}%")

    else:

        st.error(f"Low Match: {ats_score}%")
    # ---------------------------------
    # Extract Skills
    # ---------------------------------

    resume_skills = extract_skills(cleaned_resume)

    jd_skills = extract_skills(cleaned_jd)


    # ---------------------------------
    # Skill Matching
    # ---------------------------------

    matched_skills, missing_skills = skill_match(
        resume_skills,
        jd_skills
    )
    # ---------------------------------
    # Display Resume Skills
    # ---------------------------------

    st.subheader("🛠️ Resume Skills")
    st.write(resume_skills)


    # ---------------------------------
    # Display JD Skills
    # ---------------------------------

    st.subheader("📋 JD Skills")
    st.write(jd_skills)

    # ---------------------------------
    # Display Matched Skills
    # ---------------------------------

    st.subheader("✅ Matched Skills")
    st.write(matched_skills)

    # ---------------------------------
    # Display Missing Skills
    # ---------------------------------

    st.subheader("❌ Missing Skills")
    st.write(missing_skills)
    # ---------------------------------
    # Generate AI Resume Summary
    # ---------------------------------

    ai_summary = generate_resume_summary(
        resume_text
    )
    # ---------------------------------
    # Display AI Summary
    # ---------------------------------

    st.subheader("🤖 AI Resume Summary")
    st.write(ai_summary)
    # ---------------------------------
    # Generate Interview Questions
    # ---------------------------------

    interview_questions = generate_interview_questions(
        resume_text,
        job_description,
        missing_skills
    )
    # ---------------------------------
    # Display Interview Questions
    # ---------------------------------

    st.subheader("🎤 AI Interview Questions")

    st.write(interview_questions)

    # ---------------------------------
    # Career Recommendation
    # ---------------------------------

    best_role, matching_role_skills = recommend_career(
        resume_skills
    )
    # ---------------------------------
    # Display Career Recommendation
    # ---------------------------------

    st.subheader("🎯 Recommended Career Role")

    st.success(f"Best Role For You: {best_role}")

    st.subheader("✅ Matching Skills For This Role")

    st.write(matching_role_skills)
    st.subheader("🧠 Why This Role?")

    st.write(

        f"You are suitable for the role of "
        f"{best_role} because your resume "
        f"contains relevant skills such as "
        f"{', '.join(matching_role_skills)}."

    )
    # ---------------------------------
    # Job Recommendations
    # ---------------------------------

    job_data = recommend_jobs(best_role)
    # ---------------------------------
    # Display Job Recommendations
    # ---------------------------------

    st.subheader("💼 Recommended Job Roles")

    for role in job_data["roles"]:

        st.write(f"✅ {role}")
    # ---------------------------------
    # Display Job Platforms
    # ---------------------------------

    st.subheader("🌐 Recommended Job Platforms")

    platform_links = {

        "LinkedIn Jobs":
        "https://www.linkedin.com/jobs/",

        "Naukri":
        "https://www.naukri.com/",

        "Indeed":
        "https://in.indeed.com/",

        "Internshala":
        "https://internshala.com/",

        "Wellfound":
        "https://wellfound.com/",

        "Hirist":
        "https://www.hirist.tech/"
    }


    for platform in job_data["platforms"]:

        st.markdown(

            f"[{platform}]"
            f"({platform_links[platform]})"

        )
    # ---------------------------------
    # AI Career Guidance
    # ---------------------------------

    st.subheader("📈 Career Guidance")

    st.write(

        f"Based on your resume and skills, "
        f"you are currently best suited for "
        f"the role of {best_role}. "
        f"Apply for beginner-friendly roles "
        f"and internships to strengthen "
        f"your practical experience."

    )
    # ---------------------------------
    # Search Real-Time Jobs
    # ---------------------------------

    live_jobs = search_jobs(best_role)
    # ---------------------------------
    # Display Live Jobs
    # ---------------------------------

    st.subheader("🔥 Live Job Openings")


    for job in live_jobs:

        st.markdown(f"### {job['title']}")

        st.write(f"🏢 Company: {job['company']}")

        st.write(f"📍 Location: {job['location']}")

        st.markdown(

            f"[🔗 Apply Here]"
            f"({job['apply_link']})"

        )

        st.divider()

    

