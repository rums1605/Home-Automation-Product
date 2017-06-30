
import smtplib
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

 
fromaddr = "singhbiswajit79@gmail.com"
toaddr = "biswajitsingh27@yahoo.com"
 

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Image Transfer"
 
body = "list of pictures"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = ['ronaldo.jpg','big.jpg']
attachment = open("‪‪‪C:\\Users\\user\\Desktop\\ronaldo.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "biswajitsingh28")

text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()
