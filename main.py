import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

# print(results.prettify())

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    pass
    # print(job_element, end="\n"*2)


for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # print(title_element)
    # print(company_element)
    # print(location_element)

python_jobs = results.find_all("h2", string="Python") # detect string Python in h2
# print(python_jobs)

# pass function to BS4

python_job = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
# print(len(python_job))

para = soup.find_all('p')[0].get_text()
# print(para)

css = soup.select("div p")
# print(css)


