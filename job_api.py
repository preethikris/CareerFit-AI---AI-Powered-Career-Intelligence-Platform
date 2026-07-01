import requests


# -----------------------------------------
# RapidAPI Key
# -----------------------------------------

API_KEY = "9a84f21740msh828d5a3d3dab3b2p1f2e29jsne94a22d6e3d6"


# -----------------------------------------
# Search Jobs Function
# -----------------------------------------

def search_jobs(role):

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {

        "query": f"{role} in India",

        "page": "1",

        "num_pages": "1"
    }


    headers = {

        "X-RapidAPI-Key": API_KEY,

        "X-RapidAPI-Host":
        "jsearch.p.rapidapi.com"
    }


    response = requests.get(

        url,

        headers=headers,

        params=querystring
    )


    data = response.json()


    jobs = []


    if "data" in data:

        for job in data["data"][:5]:

            jobs.append({

                "title": job.get("job_title"),

                "company": job.get("employer_name"),

                "location": job.get("job_city"),

                "apply_link": job.get("job_apply_link")

            })


    return jobs