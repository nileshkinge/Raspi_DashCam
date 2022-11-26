# Import libraries
import picamera
import os
import psutil
import serial
#import pynmea2
import pathlib
import time
import json
import itertools
import RPi.GPIO as GPIO
from picamera import Color
import datetime as dt
import subprocess

import loggerHelper
import configHelper
import connectionUtility

#Global Variable declaration

absolute_path = str(pathlib.Path(__file__).parent.absolute()) + "/"
Folder_Root = absolute_path
Videos_Folder = absolute_path + "videos/"
Log_File = Folder_Root + "dashcamlogs.txt"

SWITCH_PIN = 3
POWER_PIN = 27

file_number = 0
port = "/dev/serial0"
timeout = 0.5
#serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
# GPIO.setup(POWER_PIN, GPIO.OUT)
# GPIO.output(POWER_PIN, GPIO.LOW)

# GPIO.setup(LED_PIN, GPIO.OUT)
# GPIO.output(LED_PIN, GPIO.LOW)

# Create root folder ("dashcam")
if not os.path.exists(Folder_Root):
    os.makedirs(Folder_Root)
    loggerHelper.info('Config file created')

# Create videos folder.
if not os.path.exists(Videos_Folder):
    os.makedirs(Videos_Folder)
    loggerHelper.info('videos folder created')

def getFileName(increment):
    return Videos_Folder + "video%05d.h264" % increment

# Function to delete files (per number from Json config file) if disk space is more than threshold (from condig file)
def clearSpace():
    loggerHelper.info('Creating disk space by deleting old recorded files.')    
    i = 0
    filesDeleted = 0
    maxFiles = configHelper.getConfigSetting('maxFiles')
    deleteFiles = configHelper.getConfigSetting('deleteFiles')

    while i < maxFiles:
        delFilePath = getFileName(i)
        i = i + 1
        if os.path.exists(delFilePath):
            os.remove(delFilePath)
            loggerHelper.info('Deleted file ' + delFilePath)
            filesDeleted = filesDeleted + 1
        if(filesDeleted >= deleteFiles):
            break

# Function to check available disk space. If disk space is above threshold mentioned in the Json config file then call clear_space
def checkSpace():
    loggerHelper.info('Checking disk Space...')
    spaceLimitInPercentage = configHelper.getConfigSetting('spaceLimitInPercentage')
    diskUsage = psutil.disk_usage(".").percent
    print('Disk usage: %s' % diskUsage)
    print('Usage limit: %s' % spaceLimitInPercentage)
    print('Need cleanup: %s' % (diskUsage > spaceLimitInPercentage))
    if(diskUsage > spaceLimitInPercentage):        
        clearSpace()

def setGPIOForShutdown():
    try:
        gpioPinNumber = configHelper.getConfigSetting('gpioPinNumber')
        SWITCH_PIN = gpioPinNumber
        GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    except:
        loggerHelper.error('Could not set GPIO for Shutdown.')
        raise

def handleShutdown(camera):
    cntr = 0
    start_time = time.time()
    shutdown = False
    gpioPinNumber = configHelper.getConfigSetting('gpioPinNumber') 
    if GPIO.input(gpioPinNumber) == False:
        time.sleep(1)
        cntr = cntr +1
        start_time = time.time()
        print(cntr)
        
        piShutdownDelay = configHelper.getConfigSetting('piShutdownDelay')
        if cntr > piShutdownDelay:
            shutdown = True
            loggerHelper.info('Shutting down RASPI, please wait...')
            camera.stop_recording()
            configHelper.setConfigSetting('fileNumber', fileNumber)
            #WriteFileNumberToConfigFile(fileName)
            time.sleep(3)
            loggerHelper.info('Bye Bye')
            os.system("sudo shutdown -h now")
            #subprocess.call("/sbin/shutdown -h now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        cntr = 0

def startDashCam():
    loggerHelper.info("Dash Cam Started.")
    if not configHelper.fileExists():
        configHelper.createConfig()

    setGPIOForShutdown()
    fileNumber = configHelper.getConfigSetting('fileNumber')
    fileName = Videos_Folder + "Video" + str(fileNumber).zfill(5) + "." + "h264"
    print(fileName)
    
    try:
        startRecording()
    except:
        loggerHelper.error('Recording could not be started or could have been halted.')
        raise

#Function that actually start recording based on either default or config file parameter values
# Execution Steps are 
# 1 Set values from Json config
# 2 Start recoding with a loop for max number of files.
# 3 Format file name and start recording
# 4 Print annotate having date time 
# 5 Stop Recording
# 6 Write last successful recorded file number to Jason config file.
# 7 Start recording with the next file number / Name
# 8 In between, if Shutdown switch is pressed and hold for 5 seconds, then shut down Raspi safely/softly

def startRecording():
    cntr = 0
    with picamera.PiCamera() as camera:
        # resolutionX = getConfigSetting('resolutionX')
        # resolutionY = getConfigSetting('resolutionY')
        # camera.resolution = (cnf_ResolutionX,cnf_ResolutionY)
        # framerate = getConfigSetting('framerate')
        # camera.framerate = framerate
        fileNumber = configHelper.getConfigSetting('fileNumber')         
        maxFiles = configHelper.getConfigSetting('maxFiles')

        while fileNumber < maxFiles:

            camera.resolution = (configHelper.getConfigSetting('resolutionX'),configHelper.getConfigSetting('resolutionY'))
            camera.framerate = configHelper.getConfigSetting('framerate')
            camera.rotation = configHelper.getConfigSetting('rotationAngle')
            
            fileName = getFileName(fileNumber)

            if(os.path.exists(fileName)):
                print('file exists: %s' % fileName)
                fileNumber = fileNumber+1
                fileName = getFileName(fileNumber)

            configHelper.setConfigSetting('fileNumber', fileNumber)
            loggerHelper.info('Recording to next file %s' % str(fileName))
            
            durationInMinutes = configHelper.getConfigSetting('durationInMinutes')
            durationInMinutes = durationInMinutes * 60
            timeout = time.time() + durationInMinutes
            quality = configHelper.getConfigSetting('quality')
            camera.start_recording(fileName, quality = quality)
            start = dt.datetime.now()
        
            while (dt.datetime.now() - start).seconds < durationInMinutes:
                camera.annotate_background = Color('black')
                camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %a %H:%M:%S')
                camera.wait_recording(0.1)
                                
                #handleShutdown(camera)

            loggerHelper.info("Recording saved to file " + str(fileNumber))                   
            checkSpace()
            time.sleep(0.02)            
        
            camera.stop_recording()
            loggerHelper.info("Recording successful for file " + str(fileNumber))
            fileNumber = fileNumber +1

if not connectionUtility.connectedToknownSSID():
    startDashCam()
else:
    loggerHelper.info("Connected to KnownSSID from config, recording is being skipped.")
