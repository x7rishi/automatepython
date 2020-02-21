#! C:\Users\Rishi\AppData\Local\Programs\Python\Python37\python.exe
from tkinter import *
import tkinter.ttk, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



def start(srch, tm = 0):
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
    bsr.find_element_by_link_text("Download as PDF").click()
    bsr.find_element_by_xpath('//*[@id="mw-content-text"]/form/div/span/span/button/span[2]').click()
    bsr.back()
    for i in range(4):
        sleep(tm)
        bsr.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
    # use pyautogui command to take mouse location at
    # pyautogui.displayMousePosition()
    x = 88
    y = 705
    pyautogui.click(x, y, clicks=2, interval=0, button='left')
    bsr.close()


"""
def reset():
    search.set('')"""


def timevalue():
    ptime = StringVar()
    if ptime.get() == '5 second':
        return (5)
    elif ptime.get() == '2 minute':
        return(120)
    elif ptime.get() == '4 minute':
        return (240)
    elif ptime.get() == '6 minute':
        return (360)
    elif ptime.get() == '8 minute':
        return (480)
    elif ptime.get() == '10 minute':
        return (600)
    else:
        return (None)

def main():
    win = Tk()
    win.title("Python Web Automation Application")
    win.geometry("500x200")
    win.configure(bg='#ebedf4')

    top = Frame(win, bg='#ebedf4', bd=2)
    top.pack()

    middle = Frame(win, relief=RIDGE, bg='#ebedf4')
    middle.pack()

    bottom = Frame(win, relief=SUNKEN, bg='#ebedf4')
    bottom.pack()
    tm = 0
    reset = lambda: StringVar().set('')
    b = lambda: start((w.get()), timevalue())
    search = StringVar()
    ptime = StringVar()

    lab = Label(top, text="Wikipedia Automate", font=('Inconsolata', 20), bg='#ebedf4')
    lab.grid(column=1, row=0, padx=1, pady=1)

    fra1 = Frame(top, width=496, height=2, bd=4, relief=SUNKEN)
    fra1.grid(column=1, row=1, padx=2, pady=2)
    lab2 = Label(middle, text="Search Topic in Wikipedia\n(eg. Black hole, Big Data,etc.)", font='Inconsolata',
                 bg='#ebedf4')
    lab2.grid(column=1, row=3, padx=2, pady=2)
    lab3 = Label(middle, text='Time to Scroll Page', font='Inconsolata', bg='#ebedf4')
    lab3.grid(column=1, row=4, padx=2, pady=2)
    w = Entry(middle, textvariable=search, bd=4, width=25, font='Inconsolata')
    w.grid(column=2, row=3, padx=4, pady=4)

    combo = tkinter.ttk.Combobox(middle, textvariable=ptime)
    combo['values'] = (None, '5 second', '2 minute', '4 minute', '6 minute', '8 minute', '10 minute',)
    combo.current(0)
    combo.grid(column=2, row=4, padx=1, pady=4)

    resetbut = Button(bottom, text='RESET', bd=4, font='Inconsolata', command= lambda : StringVar().set(" "), bg='orange')
    resetbut.grid(column=1, row=2, padx=4, pady=4)

    but = Button(bottom, text='Start', activebackground='green', bd=4, font='Inconsolata', command=b, bg='orange')
    but.grid(column=2, row=2, padx=4, pady=4)

    win.mainloop()

if __name__ == '__main__':
    main()
