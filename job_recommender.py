# -----------------------------------------
# Job Recommendation Database
# -----------------------------------------

JOB_RECOMMENDATIONS = {

    "Data Analyst": {

        "roles": [

            "Data Analyst Intern",
            "Junior Data Analyst",
            "Business Analyst",
            "SQL Analyst"

        ],

        "platforms": [

            "LinkedIn Jobs",
            "Naukri",
            "Indeed",
            "Internshala"

        ]
    },


    "Data Scientist": {

        "roles": [

            "Data Scientist Intern",
            "Junior Data Scientist",
            "ML Analyst",
            "AI Analyst"

        ],

        "platforms": [

            "LinkedIn Jobs",
            "Wellfound",
            "Indeed",
            "Hirist"

        ]
    },


    "AI Engineer": {

        "roles": [

            "AI Engineer Intern",
            "NLP Engineer",
            "LLM Engineer",
            "Generative AI Engineer"

        ],

        "platforms": [

            "LinkedIn Jobs",
            "Wellfound",
            "Hirist",
            "Indeed"

        ]
    },


    "ML Engineer": {

        "roles": [

            "ML Engineer Intern",
            "MLOps Engineer",
            "AI Developer",
            "Machine Learning Engineer"

        ],

        "platforms": [

            "LinkedIn Jobs",
            "Wellfound",
            "Hirist"

        ]
    },


    "Business Analyst": {

        "roles": [

            "Business Analyst",
            "Reporting Analyst",
            "MIS Analyst",
            "BI Analyst"

        ],

        "platforms": [

            "LinkedIn Jobs",
            "Naukri",
            "Indeed"

        ]
    }
}


# -----------------------------------------
# Job Recommendation Function
# -----------------------------------------

def recommend_jobs(best_role):

    if best_role in JOB_RECOMMENDATIONS:

        return JOB_RECOMMENDATIONS[best_role]

    else:

        return None