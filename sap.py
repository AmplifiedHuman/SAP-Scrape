from bs4 import BeautifulSoup
import requests

# Requests job site
website_url = "https://jobs.sap.com/go/SAP-Jobs-in-Ireland/851301/?q=&q2=&alertId=&locationsearch=&title=&location=Dublin+IE"
res = requests.get(website_url)
res.raise_for_status()

# Parse data
soup = BeautifulSoup(res.text, "html.parser")
job_titles = soup.find_all("span", class_="jobTitle visible-phone")
internship_titles = []
star_titles = []

# All jobs
print(f"There are {len(job_titles)} jobs available:")
for link in job_titles:
    job_text = str(link.a.string.encode('utf-8'))[2:-1]
    print(job_text)
    if "intern" in job_text.lower():
        internship_titles.append(job_text)
    if "star" in job_text.lower():
        star_titles.append(job_text)

print('\n')

# Intern jobs
print(f"There are {len(internship_titles)} internship titles:")
for job in internship_titles:
    print(job)

print('\n')

# STAR JOBS
print(f"There are {len(star_titles)} star titles:")
for job in star_titles:
    print(job)
