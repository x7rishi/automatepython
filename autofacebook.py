from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome()
browser.get("http://google.com")
browser.find_element_by_name("q").send_keys("facebook")
browser.find_element_by_name("q").send_keys(Keys.ENTER)
#browser.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
browser.find_element_by_class_name("LC20lb").click()
#time.sleep(2)
browser.maximize_window()
browser.find_element_by_name("email").send_keys("x7rishi@gmail.com")
time.sleep(2)
browser.find_element_by_name("pass").send_keys("qwert1234`")
time.sleep(3)
browser.find_element_by_xpath("//*[@id='u_0_8']").send_keys(Keys.ENTER)
#is it working
def push():
    var=324
    print ("test successful")