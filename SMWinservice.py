import os
import socket
import win32serviceutil
import win32service
import win32event
import servicemanager
import logging


#  2SMWinservice
#  3by Davide Mastromatteo
#  4
#  5Base class to create winservice in Python
#  6-----------------------------------------
#  7
#  8Instructions:
#  9
# 101. Just create a new class that inherits from this base class
# 112. Define into the new class the variables
# 12   _svc_name_ = "nameOfWinservice"
# 13   _svc_display_name_ = "name of the Winservice that will be displayed in scm"
# 14   _svc_description_ = "description of the Winservice that will be displayed in scm"
# 153. Override the three main methods:
# 16    def start(self) : if you need to do something at the service initialization.
# 17                      A good idea is to put here the inizialization of the running condition
# 18    def stop(self)  : if you need to do something just before the service is stopped.
# 19                      A good idea is to put here the invalidation of the running condition
# 20    def main(self)  : your actual run loop. Just create a loop based on your running condition
# 214. Define the entry point of your module calling the method "parse_command_line" of the new class
# 225. Enjoy

class SMWinservice(win32serviceutil.ServiceFramework):
    '''Base class to create winservice in Python'''

    _svc_name_ = 'RedNotWake'
    _svc_display_name_ = 'RedNotWake'
    _svc_description_ = 'i just dont want to wake from my bed'

    @classmethod
    def parse_command_line(cls):
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        UDP_IP = "127.0.0.1"
        UDP_PORT = 28075
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        while True:
            data, addr = sock.recvfrom(1024)
            print("received message: %s" % data)

            if data == b'TurnOff':
                os.system("shutdown /s /t 1")


# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
    SMWinservice.parse_command_line()
