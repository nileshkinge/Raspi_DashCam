import mail
import loggerHelper
from subprocess import check_output

def IsConnectionAvailable():
    wifi_ip = check_output(['hostname', '-I'])
    if wifi_ip is not None:
        logMessage = "Connected to wi-fi, ip is : " + str((wifi_ip) 
        print(logMessage)
        logMessage.log(logMessage)

        return True

if IsConnectionAvailable():
    mail.init()
else:
    logMessage.info("No Internet connection available.")

