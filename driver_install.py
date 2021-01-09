#! /usr/bin/env python3
import platform
import struct
import urllib.request
import zipfile as zip

import sys，os

if platform.system()=='Windows':
    from ctypes import *
else:
    print('E:Only Windows OS is supported! \r\n E:Your system is:'+platform.system()+'\r\n End.')
    exit(1)


def install():
    setupapi = cdll.LoadLibrary('setupapi')
    url='https://dl.google.com/android/repository/usb_driver_r12-windows.zip'
    if os.path.exist()==False:urllib.request.urlretrieve(url,'usb_driver_r12-windows.zip')
    else:
        z=zip.ZipFile('usb_driver_r12-windows.zip')
        z.extractall()
        z.close()
    if struct.calcsize("P") * 8==64:
        setupapi.InstallHinfSectionA(None,None,'Google.NTamd64 132 '+os.getcwd()+'\\usb_driver\\android_winusb.inf',0)
        #64bit
    elif struct.calcsize("P") * 8==32:
        setupapi.InstallHinfSectionA(None,None,'Google.NTx86 132 '+os.getcwd()+'\\usb_driver\\android_winusb.inf',0)
        #32bit
    pass
if if __name__ == "__main__":
    print('''
    Android WinUsb Driver Install:
    You may need to restart the computer after the driver installation is complete.
    If your device is not in the driver compatibility list, you may need to 
    manually install this universal driver for the device in the control panel.

    Operating procedures:
    My computer > Attributes > Device manager > Unknown device > Attributes >
    Update driver > Browse my computer to find the driver >
    Let me choose from the list of available drivers on my computer >
    Select manufacturer Google > Options containing Adb Interface characters.

    Press Enter to install.
    ''')
    input()
    install()
