import os
import pathlib

folderRoot = str(pathlib.Path(__file__).parent.absolute()) + "/"
logFile = folderRoot + "dashcamlogs.txt"

def log(msg):
    fl = (logFile)
    if not os.path.exists(fl):
        fl = open(logFile,"x")
        fl.close

    fl = open(logFile,"a")
    fl.write(msg + "\n")
    fl.close