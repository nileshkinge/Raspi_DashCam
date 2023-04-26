#!/usr/bin/python

import mail
import os
import loggerHelper
import configHelper
from subprocess import check_output, call, STDOUT, CalledProcessError

def connectedToknownSSID():
    isConnected = False
    try:
        ssid = check_output(['iwgetid --raw'], stderr=STDOUT, shell=True).decode("utf-8")
        ssids = ssid.split()
        knowns = configHelper.getConfigSetting('knownSSID')

        if(knowns.split(',').count(ssids[0]) > 0):
            isConnected = True
			
    except CalledProcessError as e:
        loggerHelper.info("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    loggerHelper.info(("Connected" if isConnected else 'Not connected' ) + " to wi-fi from knownSSID in config")
    return isConnected

def IsConnectionAvailable():
    try:
        wifi_ip = check_output(['hostname -I'], stderr=STDOUT, shell=True)
        if wifi_ip is not None:
            loggerHelper.info("Connected to wi-fi, ip is : " + str(wifi_ip))

        return True
    except CalledProcessError as e:
        loggerHelper.info("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    return False

# connectedToknownSSID()