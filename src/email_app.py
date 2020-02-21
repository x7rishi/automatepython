from tkinter import *
import tkinter.messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
"""this program will work with gmail account and microsoft account and tested ."""
# prerequisite  install mime module from pip library

def main()  :


# smtp email server connection


user="testrishi447@gmail.com"
# getting working multiple recipient

# ==================================GUI=========================================
root = Tk()
root.title("Email Sending Application")
root.geometry("690x710")
root.configure(bg='steel blue')
toptitle=Label(root,text="Quick Email Send",font=("Inconsolata", 24),bg='steel blue')
toptitle.pack()
topframe=LabelFrame(root,text=user,font=("Inconsolata"),relief=RIDGE)
topframe.pack(fill='x')
#bottom information frame >>>>>>
botfrm=Frame(root,relief=SUNKEN,bg='steel blue')
botfrm.pack(side=BOTTOM)


user="testrishi447@gmail.com"
upass = "Testing1234"
#sending process command function

def send(recipy, subject, msgbody):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.set_debuglevel(1) # red colour code generates ongoing processes
    s.ehlo()
    s.starttls()

    s.login(user, upass) #login changes should be made their
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = recipy
    # msg["Cc"] = "serenity@example.com,Koi_aur_email_id@example.com"
    body = MIMEText(msgbody)
    msg.attach(body)
    s.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
    s.close()

    label1 = Label(botfrm, text='Login successfully', bg='steel blue', fg='red')
    label1.grid(column=2, row=1)
    label2 = Label(botfrm, text="Email Sent successfully !!", bg='steel blue', fg='red')
    label2.grid(column=2, row=2)
    label3 = Label(botfrm, text="Log out and Server Closed succesfully", bg='steel blue', fg='red')
    label3.grid(column=2, row=3)


def retrieve_input():
    global sub, recipient, msg
    inputValue = textBox.get("1.0", 'end')
    send_to = inputValue.split()
    recipient = ", ".join(send_to)
    inputValue_sub = subj.get()
    sub = inputValue_sub
    inputValue_msg = msgbox.get("1.0", 'end')
    msg = inputValue_msg
    send(recipient, sub, msg)


def exit():
    exit = tkinter.messagebox.askyesno("Exit", "Do you want to exit the system")
    if exit > 0:
        root.destroy()
        return


def reset():
    subj.set("")
    msgbox.delete("1.0", "end")
    textBox.delete("1.0", "end")


subj = StringVar()


lab1 = Label(topframe, text="  Recipients ", fg="red",font=("Inconsolata", 14,'bold'))
lab1.grid(column=1, row=1, padx=2, pady=2)

textBox = Text(topframe, bd=5, height=7, width=30)
textBox.grid(column=2, row=1, padx=10, pady=10)



# getting subject and body of the messages

subtext = Label(topframe, text="Subject ",fg="red" ,font=("Inconsolata", 14,'bold'))
subtext.grid(column=1, row=4)
getsub = Entry(topframe, textvariable=subj, bg='white', bd=4, width=60)
getsub.grid(column=2, row=4, padx=2, pady=2)

msgtext = Label(topframe, text=" Message's Body ", fg="red",font=("Inconsolata", 14,'bold'))
msgtext.grid(column=1, row=5,)
msgbox = Text(topframe, bd=5,font=("Inconsolata", 12), height=15, width=45)
msgbox.grid(column=2, row=5, padx=10, pady=10)

sendbutton = Button(topframe, text="Send", font=("Inconsolata", 12, 'bold'), activebackground='Green', bd=5, height=1, width=10,
           command=retrieve_input)
sendbutton.grid(column=2, row=7, padx=2, pady=2)

exitbutton = Button(topframe, text='Exit', bd=5, font=('Inconsolata', 12, 'bold'), height=1, width=10, command=exit)
exitbutton.grid(column=3, row=7, padx=2, pady=2)

resetbutton = Button(topframe, text='RESET', font=('Inconsolata', 12, 'bold'), bd=5, height=1, width=10, command=reset)
resetbutton.grid(column=1, row=7, padx=2, pady=2)

root.mainloop()

# =============================================putting GUI above the email code===========





