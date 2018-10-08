# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:57:40 2018

@author: Lester
"""

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_address = "lnmanuel@mymail.mapua.edu.ph"
sender_email_pass = "Lnmxnuel8"
receiver_email_address = "vhdgaba@mymail.mapua.edu.ph"

email_subject_line = "Sample Python Email"

msg = MIMEMultipart()
msg['From'] = sender_email_address
msg['To'] = receiver_email_address
msg['Subject'] = email_subject_line

email_body = 'hello world'
msg.attach(MIMEText(email_body, 'plain'))

email_content = msg.as_string()
server = smtplib.SMTP('smtp-mail.outlook.com:587')

server.starttls()
server.login(sender_email_address, sender_email_pass)

server.sendmail(sender_email_address, receiver_email_address, email_content)
server.quit()