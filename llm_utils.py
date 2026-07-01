import requests
import json


# -----------------------------------------
# OpenRouter API Key
# -----------------------------------------

API_KEY = "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"


# -----------------------------------------
# AI Resume Summary
# -----------------------------------------

def generate_resume_summary(resume_text):

    prompt = f"""

    Analyze the following resume and generate
    a short professional candidate summary.

    Resume:
    {resume_text}

    """


    response = requests.post(

        url="https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },

        data=json.dumps({

            "model": "deepseek/deepseek-chat",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        })
    )


    result = response.json()

    return result['choices'][0]['message']['content']


# -----------------------------------------
# AI Interview Questions
# -----------------------------------------

def generate_interview_questions(
    resume_text,
    job_description,
    missing_skills
):

    prompt = f"""

    Based on the following resume,
    job description,
    and missing skills,

    generate technical interview questions.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Missing Skills:
    {missing_skills}

    Generate 10 interview questions.

    """


    response = requests.post(

        url="https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },

        data=json.dumps({

            "model": "deepseek/deepseek-chat",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        })
    )


    result = response.json()

    return result['choices'][0]['message']['content']