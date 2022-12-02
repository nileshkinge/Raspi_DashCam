#!/usr/bin/python

import mail
import os
import loggerHelper
import configHelper
from subprocess import check_output, call

def startNodeServer():
    loggerHelper.info("starting node app server.")
    call(["node", "/home/pi/dashcam/code/web/app.js"]) 
    loggerHelper.info("node app server has been started.")

#if IsConnectionAvailable():
#    mail.init()
#else:
#    loggerHelper.info("No Internet connection available.")

