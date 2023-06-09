from bs4 import BeautifulSoup
import requests
import time
print('Put some skills that u are not familiar with')

unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills} ')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text , 'lxml')
    jobs = soup.find_all('li' , class_='clearfix job-bx wht-shd-bx')
    for index , job in enumerate (jobs):
        published_date = job.find('span' , class_='sim-posted').span.text  
        if 'few' not in published_date:
            company_name = job.find('h3' , class_='joblist-comp-name').text.replace(" " ,"")
        

            skills = job.find('span' , class_='srp-skills').text.replace("  ","")
            
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'post/{index}.txt' ,'w') as f:
                    f.write(f'company name :{company_name.strip()}')
                    f.write(f'skills required :{skills.strip()}')
                    f.write(f'published date :{published_date.strip()}')
                    f.write(f'More Info:{more_info}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait = 10 
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)  