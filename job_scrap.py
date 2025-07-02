from bs4 import BeautifulSoup
import requests
import re
import time

print("Put some skills that you are not familiar with ")
unfamiliar_skills= input('>')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():

    html_text =requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=Python&txtKeywords=Python%2C&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")

    for index,job in enumerate(jobs):

        published_date = job.find('span' , class_='sim-posted').get_text(strip=True)

        if any(day in published_date for day in ['1 day', '2 days', '3 days']):

            company_name = job.find('h3',class_='joblist-comp-name').get_text(strip=True)
            skills = job.find('div',class_='more-skills-sections').get_text(strip=False)
            ## Replace multiple spaces/newlines with a comma (or any separator)
            skills = re.sub(r'\s+', ', ', skills).strip()
            more_info = job.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'job/jobs.txt','a') as f:
                    f.write(f'Company Name : {company_name} \n')
                    f.write(f'Required Skills : {skills} \n')
                    f.write(f'More Info : {more_info}\n')
    print(f'File saved ')

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes ...') 
        time.sleep(time_wait*60)


