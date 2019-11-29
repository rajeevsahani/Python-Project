import smtplib
import email.mime.multipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#Create Email details
msgMultipart=email.mime.multipart.MIMEMultipart()
msgMultipart["Subject"]="Test Mail"
msgMultipart["From"]="classeshcst@gmail.com"
msgMultipart["To"]="anushka@gmail.com"
#create body may be in Plain or html
body="<h1>This is Test Mail Only</h1>"
msgMultipart.attach(MIMEText(body,'html'))
smtpobj=smtplib.SMTP(host="smtp.gmail.com",port="587")
smtpobj.starttls()
smtpobj.login("classeshcst@gmail.com","password")
smtpobj.sendmail("classeshcstn@gmail.com","anushka@gmail.com",msgMultipart.as_string())
print("Message Sent Successfully.")