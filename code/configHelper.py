import pathlib
import os
import json
import loggerHelper

configDashCam = 'config.json'
absolutePath = str(pathlib.Path(__file__).parent.absolute()) + "/"

def fileExists():
    return os.path.isfile(absolutePath + configDashCam)

def getFile(mode):
    return open(absolutePath + configDashCam,mode)

def loadConfig():
    if fileExists():
        f = getFile('r')
        return json.load(f)

def getConfigSetting(key):
    config = loadConfig()
    #TODO:check for nullability of config.
    return config[key]

def setConfigSetting(key, value):
    config = loadConfig()
    #TODO:check for nullability of config.
    config[key] = value

    with getFile('w') as f:
        json.dump(config, f, sort_keys=True, indent=4)
        loggerHelper.log(key + ': ' + str(value) + ' saved in Json config file')

def getDefaultConfig():
    config = {}
    config['fileNumber'] =  1
    config['durationInMinutes'] = 1
    config['maxFiles'] =  99999
    config['spaceLimitInPercentage'] = 80
    config['deleteFiles'] = 10
    config['resolutionX'] = 1920
    config['resolutionY'] =  1000
    config['framerate'] =  30
    config['quality'] =  20
    config['piStartTimeDelay'] = 2
    config['piShutdownDelay'] = 5
    config['gpioPinNumber'] = 3

    return config

def createConfig():    
    config = getDefaultConfig()

    with getFile('w') as f:
            json.dump(config,f,sort_keys=True,indent=4)
            msg = 'Dash Cam Config is created' 
            print(msg)
            loggerHelper.log(msg)