import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

import configHelper
import loggerHelper

def initValues(toMail, fromMail, password):
    configHelper.setConfigSetting('toMail', toMail)
    configHelper.setConfigSetting('fromMail', fromMail)
    configHelper.setConfigSetting('password', password)

def setupSMTPServer():
    gmail_user = configHelper.getConfigSetting('fromMail')
    gmail_password = configHelper.getConfigSetting('password')

    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)

    return smtpserver

def getIp():
    return (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]

def getIp_old():
    arg='ip route list'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    print(data)
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1]

    return ipaddr    

def buildMessage():
    ipValue = getIp()
    print(ipValue)
    today = datetime.date.today()
    gmail_user = configHelper.getConfigSetting('fromMail')
    to = configHelper.getConfigSetting('toMail')

    my_ip = 'Dash Cam ip is %s' %  ipValue
    msg = MIMEText(my_ip)
    msg['Subject'] = 'IP For Dash Cam on %s' % today.strftime('%b %d %Y')
    msg['From'] = gmail_user
    msg['To'] = to

    return msg

def sendMessage():
    msg = buildMessage()
    smtpserver = setupSMTPServer()
    gmail_user = configHelper.getConfigSetting('fromMail')
    to = configHelper.getConfigSetting('toMail')

    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()

def init():
    sendMessage()

init()
