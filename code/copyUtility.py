#!/usr/bin/python

import mail
import os
import loggerHelper
import configHelper
from subprocess import check_output, call

def archive_remote_is_reachable():
    if(verify_configuration()):
        remoteArchive = configHelper.getConfigSetting('remoteArchive')
        try:
            loggerHelper.info("rclone remote is not reachable.")
            return check_output(['ping',remoteArchive, '-q', '-w', '1', '-c', '1'])
        except:
            loggerHelper.warning('rclone remote is not reachable')
            #TODO: handle the exception better. was interrupting the flow
            return False
    
    return False

def verify_configuration():
    if(not os.path.exists('/home/pi/.config/rclone/rclone.conf')):
        loggerHelper.warning('rclone config was not found. did you configure rclone correctly?')
        return False

    copySourcePath = configHelper.getConfigSetting('copySourcePath')
    if(not os.path.exists(copySourcePath)):
        loggerHelper.warning('"' + copySourcePath + '" was not found.')
        return False
    
    try:
        rcloneRemoteName = configHelper.getConfigSetting('rcloneRemoteName')
        rcloneRemotePath = configHelper.getConfigSetting('rcloneRemotePath')
        check_output(['rclone', 'lsd', (rcloneRemoteName+rcloneRemotePath)])
    except:
        loggerHelper.warning('Could not find the rclone remote or remote path')
        return False

    return True


def copy_clips():
    if archive_remote_is_reachable():
        loggerHelper.info("Recordings are being moved.")
        try:
            rcloneRemoteName = configHelper.getConfigSetting('rcloneRemoteName')
            rcloneRemotePath = configHelper.getConfigSetting('rcloneRemotePath')
            copySourcePath = configHelper.getConfigSetting('copySourcePath')
            check_output(['rclone', 'move', copySourcePath , (rcloneRemoteName+rcloneRemotePath)])
        except:
            loggerHelper.error("There was an error moving recordings.")