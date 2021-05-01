import mail
import loggerHelper

def IsConnectionAvailable():
    wifi_ip = check_output(['hostname', '-I'])
    if wifi_ip is not None:
        logMessage = "Connected to wi-fi, ip is : " + wifi_ip 
        print(logMessage)
        logMessage.log(logMessage)

        return True

if IsConnectionAvailable():
    mail.init()
else:
    logMessage.info("No Internet connection available.")

