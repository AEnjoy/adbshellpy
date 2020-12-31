#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_libroot
#       By : 神郭
#  Version : 0.6.0 Stable
import sys,os,zipfile,urllib.request
try:from adbshell import errexit,update,checkinternet,clear,ParseArguments,adbcommand,install,changes,github,version,builddate,who,nowdevice
except:from adbshell_alpha import errexit,update,checkinternet,clear,ParseArguments,adbcommand,install,changes,github,version,builddate,who,nowdevice
class adbshellpyinformation:
    branch=None
    try:from adbshell_alpha import adbfile
    except:from adbshell import adbfile
    uselinuxpkgmanagertoinstalladb=None
    aapt=None
adb=adbcommand(nowdevice)  
def Activate_KFMark():
    '快否激活'
    url='https://hub.fastgit.org/aifou-kfmark/KFMARK/releases/download/1.5/daemon'
    if os.path.exists('daemon')==False:
        print('未检测到快否启动实例:daemon,正在为您下载中...')
        try:urllib.request.urlretrieve(url,'daemon')
        except:
            print('E:下载失败!')
            return
    adb.push('daemon','/data/local/tmp')
    adb.shell('chmod 777 /data/local/tmp/daemon')
    adb.shell('"./data/local/tmp/daemon &"')
def home():
    print('''
     ___________________________ADBSystemROOTTOOLBOX__________________________________
                                   ROOT玩机专区   
     ___________________________ADBSystemROOTTOOLBOX__________________________________
    ''')
