from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
import time
import os


from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#setup webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#url for scraping
url = "https://www.linkedin.com/jobs/search/?keywords=Data%20Analysis&location=Philippines&locationId=&geoId=103121230&f_TPR=r2592000&f_WT=2&position=1&pageNum=0"
#initiate webdriver and url fetch
driver.get(url)
driver.implicitly_wait(10)
#get number of jobs
n = driver.find_elements(By.CLASS_NAME, "results-context-header__job-count")[0].text
n = pd.to_numeric(n)
print(n)

#saving the scraped data
companyname: list = []

#infinite scrolling 
scroll_limit: int= 20
i=1
while i<=20:
  driver.implicitly_wait(5)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  i+=1
  try:  
    send=driver.find_element(By.XPATH, "//button[@aria-label='Load more results']")
    driver.execute_script("arguments[0].click();", send)   
    time.sleep(3)
    
  except:
    pass
    time.sleep(5)

#looping for scraping
for j in range(n):
  try:
    company = driver.find_elements(By.TAG_NAME, "li")[j].text
    companyname.append(company)

  except IndexError:
    print("no")


    
len(companyname)

