# -----------------------------------------
# Career Role Database
# -----------------------------------------

CAREER_PATHS = {

    "Data Analyst": [

        "sql",
        "excel",
        "power bi",
        "tableau",
        "data analysis",
        "data visualization",
        "pandas"
    ],

    "Data Scientist": [

        "python",
        "machine learning",
        "statistics",
        "scikit-learn",
        "numpy",
        "pandas",
        "matplotlib"
    ],

    "AI Engineer": [

        "deep learning",
        "nlp",
        "tensorflow",
        "pytorch",
        "machine learning",
        "python"
    ],

    "ML Engineer": [

        "machine learning",
        "docker",
        "kubernetes",
        "aws",
        "flask",
        "fastapi"
    ],

    "Business Analyst": [

        "excel",
        "sql",
        "power bi",
        "tableau",
        "data visualization"
    ]
}


# -----------------------------------------
# Career Recommendation Function
# -----------------------------------------

def recommend_career(resume_skills):

    best_role = None

    best_score = 0

    best_matching_skills = []


    for role, skills in CAREER_PATHS.items():

        matched_skills = list(
            set(resume_skills).intersection(set(skills))
        )

        score = len(matched_skills)


        if score > best_score:

            best_score = score

            best_role = role

            best_matching_skills = matched_skills


    return best_role, best_matching_skills