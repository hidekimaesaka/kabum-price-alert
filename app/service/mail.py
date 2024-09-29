from os import getenv

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'lucasmsk11@gmail.com'
passw = getenv('APP_MAIL_PASSW')
port = 587
smtp_server = 'smtp.gmail.com'


def send_email(mail_to, msg):

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = mail_to
    message['Subject'] = 'Kabum Price Alert'

    mail = MIMEText(msg, 'plain')
    message.attach(mail)


    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender, passw)
        server.sendmail(sender, mail_to, message.as_string())
