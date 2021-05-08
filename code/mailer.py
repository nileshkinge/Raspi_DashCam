import mail
import loggerHelper
from subprocess import check_output

def IsConnectionAvailable():
    wifi_ip = check_output(['hostname', '-I'])
    if wifi_ip is not None:
        loggerHelper.info("Connected to wi-fi, ip is : " + str(wifi_ip))

        return True

if IsConnectionAvailable():
    mail.init()
else:
    loggerHelper.info("No Internet connection available.")

