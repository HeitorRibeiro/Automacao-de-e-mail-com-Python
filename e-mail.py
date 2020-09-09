#!/usr/bin/python
#-*- coding: utf-8 -*-
import os, sys
from email.mime.multipart  import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders
import smtplib

#seu e-mail e senha:
email_login = 'seuemail@gmail.com '
senha = 'senha'

#e-mail do destinatário:
send_mail_to = 'destinatario@gmail.com'

#caminho do arquivo:
caminho_arquivo = 'caminho-do-arquivi/anexo.pdf'

#servidor SMTP:
smtp_server = 'smtp.gmail.com'
smtp_server_port = '587'

#Assunto e corpo do email:
msg = MIMEMultipart()
msg['Subject'] = "Assunto"
body = '''
Corpo do texto
'''
msg.attach(MIMEText(body, 'plain'))

#Anexo do e-mail:
msg_file = MIMEBase('application', 'pdf')
msg_file.set_payload(file(caminho_arquivo).read())
Encoders.encode_base64(msg_file)
msg_file.add_header('Content-Disposition', 'attachment', filename='anexo.pdf')
msg.attach(msg_file)

#processo
mailer = smtplib.SMTP(smtp_server, smtp_server_port)
mailer.ehlo()
mailer.starttls()
mailer.login(email_login,senha)
mailer.sendmail(email_login, send_mail_to, msg.as_string())
print('E-mail enviado com sucesso !')
mailer.close()
