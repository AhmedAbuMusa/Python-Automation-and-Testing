from selenium import webdriver;
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.common.by import By;
from time import time;


driver = webdriver.Edge();


driver.get("https://www.python.org");

select = Select();