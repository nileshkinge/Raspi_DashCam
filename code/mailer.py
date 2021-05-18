#!/usr/bin/python

import mail
import loggerHelper
from subprocess import check_output, call

def IsConnectionAvailable():
    wifi_ip = check_output(['hostname', '-I'])
    if wifi_ip is not None:
        loggerHelper.info("Connected to wi-fi, ip is : " + str(wifi_ip))

        return True

def startNodeServer():
    loggerHelper.info("starting node app server.")
    call(["node", "/home/pi/Raspi_DashCam/code/web/app.js"]) 
    loggerHelper.info("node app server has been started.")

# startNodeServer()

if IsConnectionAvailable():
    mail.init()
else:
    loggerHelper.info("No Internet connection available.")

