# not working for multiple recipeints ...
import smtplib
#Connecting smtp server of gmail
gmail=smtplib.SMTP("smtp.gmail.com",587)
gmail.ehlo()
gmail.starttls() # starts TLS

#user login part

gmail.login('======email======','====pass=======')
# getting list of recipient

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

to_recipient=", ".join(send_to)

sub=str(input("Enter The Subject of the Email :\n"))
body=str(input("Enter the message body of Your Email :\n"))

# Method 1 to get seperated subject and body

message1='Subject: '+ sub+'\n\n'+body

# Method 2 to get seperated subject and body by using format method

message2= 'Subject: {}\n\n{}'.format(sub, body)

# Message Send

gmail.sendmail('=====email=======',to_recipient,message1)
gmail.close()
print("Message send successfully !")
#gmail message sent





