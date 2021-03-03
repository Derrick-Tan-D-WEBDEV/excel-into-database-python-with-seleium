import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time
import pandas as pd
downloads_path = str(Path.home() / "Downloads")

def insert_employee(params):
    mycursor = mydb.cursor()
    sql = "INSERT INTO employee (name, address) VALUES (%s, %s)"
    mycursor.execute(sql, params)
    mydb.commit()

def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

#selenium
PATH = "D:\Youtube\Python Projects\WebScrapingProjects\ScrapingWeather\chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(PATH,options=options)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-xls-download/")
driver.find_element_by_xpath('/html/body/div[1]/main/section/div/div[2]/div/div/table/tbody/tr[1]/td[5]/a[1]').click()

#selenium working on chrome downloads to get file name
driver.get("chrome://downloads")
time.sleep(5)
manager = driver.find_element_by_css_selector('downloads-manager')
manager = expand_shadow_element(manager)
item = manager.find_element_by_css_selector('downloads-item')
item = expand_shadow_element(item)
content = item.find_element_by_css_selector('#content')
file_name = content.find_element_by_css_selector('#file-link').get_attribute("innerHTML")
full_path = downloads_path+'\\'+file_name

df = pd.read_excel (full_path)
print (df)

#process the data
#WRITE YOUR CODE HERE FOR PROCESSING DATA

#mysql config
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_db_greatech"
)
#insert data
#WRITE YOUR CODE HERE FOR INSERTING DATA