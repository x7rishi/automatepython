import smtplib
from email.mime.text import MIMEText
# prerequistive install mime module from pip library

#smtp email server connection
s = smtplib.SMTP('smtp.gmail.com',587)
s.set_debuglevel(1) # red colour code generates ongoing processes
s.ehlo()
s.starttls()
s.login('======username=======','==========password==========')

#getting working multiple recipient

send_to=[(str(input("Enter the email address where to send :")))]
q='y'
while (q=='y'):
    q=str(input("Want to enter more Sender \n 1.yes to press y\n 2. No to press to n \n->"))
    if q == 'y':
        new_recip=str(input("Enter the email address where to send :"))
        send_to.append(new_recip)
        continue
    else :
        break
for i in send_to:
    print('recipient will be ->',i)

# getting subject and body of the messages


sub=str(input("Enter The Subject of the Email :\n"))
body=str(input("Enter the message body of Your Email :\n"))

msg = MIMEText(body)
sender = '==========username=========='
recipients =send_to
msg['Subject'] = sub
msg['From'] = sender
msg['To'] = ", ".join(recipients)

#message sending and attaching msg body.....
s.sendmail(sender, recipients, msg.as_string())
s.close()
print("Email sent successfully !!")
