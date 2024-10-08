from selenium import webdriver;
from selenium.webdriver.common.by import By;
import time;

driver = webdriver.Edge();
driver.get("http://127.0.0.1:3000/CH02/html_code_02.html")

element = driver.find_element(By.PARTIAL_LINK_TEXT,"loginForm")

print(element)

time.sleep(4)

driver.close()