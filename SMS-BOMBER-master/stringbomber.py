## String_Bomber ##
## made by String ##
import time
import smtplib

#CONFIG. You can change any of the values on the right.
email_provider = 'smtp-mail.outlook.com' #server for your email- see ReadMe on github
email_address = "gonz0@outlook.com" #your email
email_port = 587 #port for email server- see ReadMe on github
password = "Asdjabsdjk982bd8bsss" #your email password
msg = "test" #your txt message
text_amount = 1 #amount sent
target_email = "5188328280@vtext.com" #target number. must be in email form- see ReadMe on github
wait = 1 #seconds in between messages

server = smtplib.SMTP(email_provider, email_port)
server.starttls()
server.login(email_address, password)
for _ in range(0,text_amount):
    server.sendmail(email_address,target_email,msg)
    print("sent")
    time.sleep(wait)
print("{} texts were sent.".format(text_amount))
server.quit()
