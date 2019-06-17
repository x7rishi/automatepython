from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *
bsr=webdriver.Chrome()
bsr.get("https://www.google.com")
bsr.find_element_by_name("q").send_keys("Wikipedia")
bsr.send
bsr.find_element_by_class_name("LC201b").click()

