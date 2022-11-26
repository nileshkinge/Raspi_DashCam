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

    loggerHelper.info(("Connected" if isConnected else 'Not connected' ) + " to wi-fi from knownSSID in config")
    return isConnected

def IsConnectionAvailable():
    wifi_ip = check_output(['hostname', '-I'])
    if wifi_ip is not None:
        loggerHelper.info("Connected to wi-fi, ip is : " + str(wifi_ip))

        return True
