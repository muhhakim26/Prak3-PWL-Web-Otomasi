from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

my_json = open('./testcase.json', 'r')
json_data = my_json.read()

obj = json.loads(json_data)

PATH = "B:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://localhost:3000/")

nama_input = driver.find_element_by_id('nama')
username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')
repassword_input = driver.find_element_by_id('repassword')
submit = driver.find_element_by_id('submit')

for i in obj:
    nama_input.clear()
    nama_input.send_keys(i['data']['nama'])
    time.sleep(1)
    username_input.clear()
    username_input.send_keys(i['data']['username'])
    time.sleep(1)
    password_input.clear()
    password_input.send_keys(i['data']['password'])
    time.sleep(1)
    repassword_input.clear()
    repassword_input.send_keys(i['data']['repassword'])
    time.sleep(1)
    submit.click()
    time.sleep(5)

driver.quit()
