from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome()
browser.get("http://google.com")
browser.find_element_by_name('q').send_keys("google news")
browser.maximize_window()
time.sleep(4)
browser.find_element_by_name("q").send_keys(Keys.ENTER)
browser.find_element_by_class_name("LC20lb").click()
#browser.find_element_by_xpath("//*[@id='yDmH0d]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[2]/div/article/a").click()
browser.find_element_by_class_name("VDXfz").click()
print("Test successful")
