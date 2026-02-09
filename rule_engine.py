def recommend_domain(profile):

    scores = {
        "SDE": 0,
        "Data Science": 0,
        "Core Engineering": 0,
        "Consulting/Product": 0
    }

    # SDE logic
    scores["SDE"] += profile["dsa"] * 2
    scores["SDE"] += profile["os"]
    scores["SDE"] += profile["dbms"]

    # Data Science logic
    scores["Data Science"] += profile["python"] * 2
    scores["Data Science"] += profile["ml"] * 2
    scores["Data Science"] += profile["dsa"]

    # Core Engineering logic
    scores["Core Engineering"] += profile["os"] * 2
    scores["Core Engineering"] += profile["dbms"]

    # Consulting/Product logic
    scores["Consulting/Product"] += profile["cgpa"]
    scores["Consulting/Product"] += profile["web"]

    best_domain = max(scores, key=scores.get)

    roadmaps = {
        "SDE": [
            "Master Data Structures & Algorithms",
            "Practice LeetCode daily",
            "Revise OS, DBMS, OOPS",
            "Learn System Design basics",
            "Give mock interviews"
        ],
        "Data Science": [
            "Master Python & Pandas",
            "Study Statistics & Probability",
            "Build ML projects",
            "Practice SQL",
            "Prepare ML interview questions"
        ],
        "Core Engineering": [
            "Strengthen OS concepts",
            "Revise DBMS deeply",
            "Practice core subject MCQs",
            "Study networking basics",
            "Prepare for technical interviews"
        ],
        "Consulting/Product": [
            "Improve communication skills",
            "Practice aptitude & case studies",
            "Learn product thinking",
            "Work on analytics basics",
            "Prepare HR interview answers"
        ]
    }

    return {
        "recommended_domain": best_domain,
        "scores": scores,
        "roadmap": roadmaps[best_domain]
    }

def company_fit(domain):
    company_mapping = {
        "SDE": [
            "Amazon",
            "Google",
            "Microsoft",
            "Adobe",
            "Atlassian"
        ],
        "Data Science": [
            "Flipkart",
            "Zomato",
            "JPMorgan",
            "Swiggy",
            "Meesho"
        ],
        "Web Dev": [
            "Infosys",
            "TCS Digital",
            "Wipro",
            "Startups",
            "Zoho"
        ],
        "Core CS": [
            "Oracle",
            "Qualcomm",
            "Intel",
            "Nvidia",
            "Cisco"
        ]
    }

    return company_mapping.get(domain, [])
