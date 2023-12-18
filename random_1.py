from selenium import webdriver
import time
import random
driver = webdriver.Chrome()

url = "https://docs.google.com/forms/d/e/1FAIpQLSegxy2KCWKhlQECEnqhAq9ZDtYSbNsCkDhwhvwexpEjKMHgsw/viewform"
driver.get(url)
template_question = f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div"
r = driver.find_element("xpath", template_question)
a = driver.find_element("xpath", "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[5]/div/span/div/div/div[1]/input")
r.click()
a.send_keys("1egejioeioje")

time.sleep(10)