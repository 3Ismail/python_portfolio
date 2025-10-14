jobs = [
    {"title": "Python Developer", "company": "TechCorp", "location": "Remote"},
    {"title": "Data Analyst", "company": "DataVision", "location": "Casablanca"},
    {"title": "Backend Intern", "company": "SoftLink", "location": "Rabat"}
]

def show_jobs():
    print("\n=== Available Jobs ===")
    for job in jobs:
        print(f"{job['title']} at {job['company']} ({job['location']})")

if __name__ == "__main__":
    show_jobs()
