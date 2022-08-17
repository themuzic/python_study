import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a')

    spans = []
    for link in links[:-1]:
        spans.append(int(link.find("span").string))
    """
    spans[0:-1] : spans 배열에서 뒤에서 첫번째 요소를 제외하고 나머지를 호출한다. 
                0번 인덱스부터 시작할 경우 0 생략 가능
    spans[0:5] : spans 배열에서 0번 index부터 5개 요소들을 호출한다.
    """
    max_page = spans[-1]    # spans 배열에서 가장 큰 숫자 -> 가장 마지막 인덱스에 있는 숫자 
    
    return max_page

def extract_job(html):
    title = html.find("div",{"class":"title"}).find("a")["title"]
    company = html.find("span",{"class":"company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return{
        "title": title,
        "company": company,
        "location": location, 
        "link": f"https://kr.indeed.com/viewjob?jk={job_id}"
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(2)
    return jobs