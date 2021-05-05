import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

time
pd
requests
BeautifulSoup


def extract(page):
    # f in front of the string makes it the string literal, without the f there would be no page variable
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/90.0.4430.93 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=data+scientist&l=Denver%2C+CO&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
time = 20


def transform(soup):
    divs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='company').text.strip()
        try:
            salary = item.find('span', class_='salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', class_='summary').text.strip().replace('\n', ' ')

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return

joblist = []

for i in range(0, 40, 10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)
print(len(joblist))

df = pd.DataFrame(joblist)
print(df.head())
'''df.to_csv('job.csv')'''