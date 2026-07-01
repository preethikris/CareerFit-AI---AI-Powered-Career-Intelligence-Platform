# -----------------------------------------
# Skill Database
# -----------------------------------------

SKILLS_DB = [

    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "data analysis",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "power bi",
    "tableau",
    "excel",
    "streamlit",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "git",
    "github",
    "mysql",
    "mongodb",
    "flask",
    "fastapi",
    "statistics",
    "data visualization"
]


# -----------------------------------------
# Skill Extraction Function
# -----------------------------------------

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:

        if skill in text:

            found_skills.append(skill)

    return list(set(found_skills))


# -----------------------------------------
# Skill Matching Function
# -----------------------------------------

def skill_match(resume_skills, jd_skills):

    matched_skills = list(
        set(resume_skills).intersection(set(jd_skills))
    )

    missing_skills = list(
        set(jd_skills).difference(set(resume_skills))
    )

    return matched_skills, missing_skills