#!/usr/bin/python

import mail
import os
import loggerHelper
import configHelper
from subprocess import check_output, call

def connectedToknownSSID():
    try:
        ssid = check_output(['iwgetid --raw'], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
    except subprocess.CalledProcessError as e:
        loggerHelper.info("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    
    ssids = ssid.split()
    knowns = configHelper.getConfigSetting('knownSSID')

    isConnected = False
    if(knowns.split(',').count(ssids[0]) > 0):
        isConnected = True

    loggerHelper.info(("Connected" if isConnected else 'Not connected' ) + " to wi-fi from knownSSID in config")
    return isConnected

def IsConnectionAvailable():
    try:
        wifi_ip = check_output(['hostname -I'], stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        loggerHelper.info("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    if wifi_ip is not None:
        loggerHelper.info("Connected to wi-fi, ip is : " + str(wifi_ip))

        return True

# connectedToknownSSID()