#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_libroot
#       By : 神郭
#  Version : 1.0
# Do not try to import this file in Python! 
import sys,os,zipfile,urllib.request
try:
    from adbshell import errexit
    from adbshell import update
    from adbshell import checkinternet
    from adbshell import clear
    from adbshell import ParseArguments
    from adbshell import adbcommand
    from adbshell import install
    from adbshell import changes
    from adbshell import github
    from adbshell import version
    from adbshell import builddate
    from adbshell import nowdevice
except:
    from adbshell_alpha import errexit
    from adbshell_alpha import update
    from adbshell_alpha import checkinternet
    from adbshell_alpha import clear
    from adbshell_alpha import ParseArguments
    from adbshell_alpha import adbcommand
    from adbshell_alpha import install
    from adbshell_alpha import changes
    from adbshell_alpha import github
    from adbshell_alpha import version
    from adbshell_alpha import builddate
    from adbshell_alpha import who
    from adbshell_alpha import nowdevice
class adbshellpyinformation:
    branch=None
    try:from adbshell_alpha import adbfile
    except:from adbshell import adbfile
    uselinuxpkgmanagertoinstalladb=None
    aapt=None

adb=adbcommand(nowdevice)  
def busyboxcheck():
    if os.system(adbshellpyinformation.adbfile+' shell busybox')==0:return True
    else:return False
def isroot():
    if os.system(adbshellpyinformation.adbfile+' shell su')==0:return True
    else:return False
def ismagiskinstelled():
    if os.system(adbshellpyinformation.adbfile+' shell magisk')==0:return True
    else:return False
def istaichimagiskinstelled():
    if os.system(adbshellpyinformation.adbfile+' shell find -type f /system/lib/libjit.so')==0:return True
    else:return False
'''     
def isriruinstelled():
    if os.system(adbshellpyinformation.adbfile+' shell find ')==0:return True
    else:return False        
'''    
def fixtaobao():
    '''
    修复淘宝/京东/优酷闪退
    '''
    adb.shell('rm -rf /data/data/com.youku.phone/files/storage & rm -rf /data/data/com.youku.phone/files/bundleBaseline',1)#youku
    adb.shell('rm -rf /data/data/com.taobao.taobao/files/storage & rm -rf /data/data/com.taobao.taobao/files/bundleBaseline',1)#taobao
    adb.shell('mkdir -p /data/data/com.jingdong.app.mall/files/start_image & chmod 500 /data/data/com.jingdong.app.mall/files/start_image & chown 0:0 /data/data/com.jingdong.app.mall/files/start_image',1)
    adb.shell('mkdir -p /data/data/com.jingdong.app.mall/files/hotfix & chmod 500 /data/data/com.jingdong.app.mall/files/hotfix & chown 0:0 /data/data/com.jingdong.app.mall/files/hotfix',1)
    #jingdong
def clenvmcache():
    '''
    硬核删除编译缓存
    '''
    adb.shell('su & find /data  -name *.odex  |xargs rm -rf')
    adb.shell('su & find /data  -name *.vdex  |xargs rm -rf')
def Activate_KFMark():
    '快否激活'
    url='https://github.com/aifou-kfmark/KFMARK/releases/download/1.5/daemon'
    if os.path.exists('daemon')==False:
        print('未检测到快否启动实例:daemon,正在为您下载中...')
        try:urllib.request.urlretrieve(url,'daemon')
        except:
            print('E:下载失败!')
            return
    adb.push('daemon','/data/local/tmp')
    adb.shell('chmod 777 /data/local/tmp/daemon')
    adb.shell('"./data/local/tmp/daemon &"')
def remove_xiaomi_browser_blacklist():
    '小米黑名单移除'
    adb.shell('rm -rf /data/data/com.android.browser/files/data/caclist/*',1)
    adb.shell('chmod 000 /data/data/com.android.browser/files/data/caclist 2>/dev/null',1)
    adb.shell('rm -rf /data/media/0/browser/MediaCache/*',1)
    adb.shell('chmod 000 /data/media/0/browser/MediaCache 2>/dev/null',1)
    adb.shell('echo Done')
def Brush_writing_Rec():
    '防止滚回官方rec'
    adb.shell('busybox mount -o remount,rw /system & mv -f /system/recovery-from-boot.p /system/recovery-from-boot.bak',1)
def apptosystem(func,flag=1):
    'func package name or address'
    pass
def getdeskinfo(flag=0,f=0):
    'flag if return f=1 only package'
    if flag==0:
        adb.shell('pm resolve-activity --brief -c android.intent.category.HOME -a android.intent.action.MAIN | grep /')
    if flag==1:
        a=os.popen(adbshellpyinformation.adbfile+' shell pm resolve-activity --brief -c android.intent.category.HOME -a android.intent.action.MAIN | grep /')
        if f==1:
            l=a.readline().split('/')
            return l[0]
        else:return a.readline()
        
def home():
    print('''
     ___________________________ADBSystemROOTTOOLBOX__________________________________
                                   ROOT玩机专区   
     ___________________________ADBSystemROOTTOOLBOX__________________________________
    ''')
