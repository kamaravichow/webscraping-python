from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver")

df = pd.DataFrame(columns=["Title","Location","Company","Salary","Sponsored","Description"])


driver.get("https://www.indeed.co.in/jobs?q=Android+Developer&l=India")
driver.implicitly_wait(4)

all_jobs = driver.find_element_by_class_name('result')

for job in all_jobs:

	result_html = job.get_attribute('innerHTML')
	soup = BeautifulSoup(result_html, 'html.parser')

	try:
		title = soup.find("a",class_="jobtitle").text.replace("\n","").strip()
			
	except:
		title = 'None'

	try:
		location = soup.find(class_="location").text
	except:
		location = 'None'

	try:
		company = soup.find(class_="company").text.replace("\n","").strip()
	except:
		company = 'None'

	try:
		salary = soup.find(class_="salary").text.replace("\n","").strip()
	except:
		salary = 'None'

	try:
		sponsored = soup.find(class_="sponsoredGray").text
		sponsored = "Sponsored"
	except:
		sponsored = "Organic"		



	sum_div = job.find_elements_by_class_name("summary")[0]
	sum_div.click()

	job_desc = driver.find_element_by_id('vjs-desc').text	

	df = df.append({'Title':title,'Location':location,"Company":company,"Salary":salary,
						"Sponsored":sponsored,"Description":job_desc},ignore_index=True)
	
	print("Got these many results:",df.shape)

df.to_csv("dataset.csv",index=False)	


























