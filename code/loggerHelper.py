import os
import pathlib
import logging

folderRoot = str(pathlib.Path(__file__).parent.absolute()) + "/"
logFile = folderRoot + "log.log"

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=logFile, 
    level=logging.DEBUG,
    datefmt='%m/%d/%Y %I:%M:%S %p')

def info(msg):
    logging.info(msg)

def debug(msg):
    logging.debug(msg)

def warning(msg):
    logging.warning(msg)

def error(msg):
    logging.error(msg)

def log(msg):
    fl = (logFile)
    if not os.path.exists(fl):
        fl = open(logFile,"x")
        fl.close

    fl = open(logFile,"a")
    fl.write(msg + "\n")
    fl.close