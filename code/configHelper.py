import pathlib
import os
import json
import loggerHelper

configDashCam = 'config.json'
absolutePath = str(pathlib.Path(__file__).parent.absolute()) + "/"

def fileExists():
    try:
        return os.path.isfile(absolutePath + configDashCam)
    except:
        loggerHelper.error('Encountered issue while checking for file: "' + absolutePath + configDashCam +'"')
        raise

def getFile(mode):
    try:
        return open(absolutePath + configDashCam,mode)
    except:
        loggerHelper.error('Could not get file: "' + absolutePath + configDashCam +'"')
        raise

def loadConfig():
    try:
        if fileExists():
            f = getFile('r')
            return json.load(f)
    except:
        loggerHelper.error('Could not load Config.json')
        raise

def getConfigSetting(key):
    try:
        config = loadConfig()
        #TODO:check for nullability of config.
        return config[key]
    except:
        loggerHelper.error('Could not get value for key: "' + key + '"')
        raise

def setConfigSetting(key, value):
    try:
        config = loadConfig()
        
        #TODO:check for nullability of config.
        if config is None:
            createConfig()
            config = loadConfig()

        config[key] = value

        with getFile('w') as f: 
            json.dump(config, f, sort_keys=True, indent=4)
            loggerHelper.info(key + ': ' + str(value) + ' saved in Json config file')
    except:
        loggerHelper.error('Could not set value: "'+ value + '" for key: "' + key + '"')
        raise

def getDefaultConfig():
    config = {}
    config['fileNumber'] =  1
    config['durationInMinutes'] = 1
    config['maxFiles'] =  99999
    config['spaceLimitInPercentage'] = 80
    config['deleteFiles'] = 5
    config['resolutionX'] = 1920
    config['resolutionY'] =  1000
    config['framerate'] =  30
    config['quality'] =  20
    config['piStartTimeDelay'] = 2
    config['piShutdownDelay'] = 5
    config['gpioPinNumber'] = 3
    config['rotationAngle'] = 90
    config['knownSSID'] = 'kinge'

    return config

def createConfig():
    try:    
        config = getDefaultConfig()

        with getFile('w') as f:
                json.dump(config,f,sort_keys=True,indent=4)
                msg = 'Dash Cam Config is created' 
                print(msg)
                loggerHelper.info(msg)
    except:
        loggerHelper.error('Could not create config.json file')
        raise