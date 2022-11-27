#!/usr/bin/python

import mail
import os
import loggerHelper
import configHelper
from subprocess import check_output, call

def connectedToknownSSID():
    ssid = check_output(['iwgetid', '--raw']).decode("utf-8")
    ssids = ssid.split()
    knowns = configHelper.getConfigSetting('knownSSID')
    
    isConnected = False
    if(knowns.split(',').count(ssids[0]) > 0):
        isConnected = True

    return isConnected

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
if(connectedToknownSSID()):
    print('connected to "kinge"')
else:
    print('not connected to "kinge"')


#if IsConnectionAvailable():
#    mail.init()
#else:
#    loggerHelper.info("No Internet connection available.")

