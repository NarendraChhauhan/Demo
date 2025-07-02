from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.buddy4study.com/scholarships")
soup = BeautifulSoup(driver.page_source, 'lxml')
scholarship_card = soup.find_all('a', class_="Listing_categoriesBox__CiGvQ")
scholarship_name_sec = soup.find_all('h4',class_="Listing_scholarshipName__VLFMj")

for card in scholarship_card:
    url=card['href']
    scholarship_name_sec=card.find('h4',class_="Listing_scholarshipName__VLFMj")
    main_url = f'https://www.buddy4study.com/{url}'
    # driver.get(main_url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    eligibility = soup.find('div',class_="ScholarshipDetails_studyLine__ka4X2")

driver.quit()


    
 
 
 