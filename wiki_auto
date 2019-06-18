from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *
from tkinter import *


def wikisrch(srch):
    bsr = webdriver.Chrome()
    bsr.maximize_window()
    sleep(1)
    bsr.get("https://www.google.com")
    sleep(1)
    bsr.find_element_by_name("q").send_keys("Wikipedia")
    sleep(1)
    bsr.find_element_by_name("q").send_keys(Keys.ENTER)
    sleep(1)
    bsr.find_element_by_class_name("LC20lb").click()
    sleep(1)
    bsr.find_element_by_name('search').send_keys(srch)

    bsr.find_element_by_name('search').send_keys(Keys.ENTER)
    for i in range(100):
        sleep(4)
        bsr.find_element_by_tag_name("html").send_keys(Keys.ARROW_DOWN)


#===========gui-==================


from tkinter import *

win=Tk()
win.title("Python WEB automation")
win.geometry("254x184")
lab=Label(text="Wikipedia Automate",font=('Inconsolata',20))
lab.grid(padx=1,pady=1)
lab2=Label(text="Enter to search in Wikipedia ",font='Inconsolata')
lab2.grid(padx=9,pady=1)


w=Entry(win,bd=4)
w.grid(padx=10,pady=3)
b=lambda : wikisrch(w.get())
but=Button(win,text="Press To Start !",activebackground='green',bd=4,command=b)
but.grid(padx=11,pady=5)


win.mainloop()
