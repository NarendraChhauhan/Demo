from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.buddy4study.com/scholarships")
soup = BeautifulSoup(driver.page_source, 'lxml')
scholarship_card = soup.find('div', class_="Listing_categoriesCard___CHju")
scholarship_url = scholarship_card.find('a', class_="Listing_categoriesBox__CiGvQ")
scholarship_name_sec = scholarship_card.find('h4',class_="Listing_scholarshipName__VLFMj")
print(scholarship_name_sec)
scholarship_name_sec = soup.find('h4',class_="Listing_scholarshipName__VLFMj")


driver.quit()


    
 
 
 