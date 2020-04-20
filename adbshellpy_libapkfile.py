#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_libbrotli.py
#       By : 神郭
#  Version : 1.0
#  release
import sys,os
import zipfile as zip
try:
    from adbshell import errexit
    from adbshell import update
    from adbshell import checkinternet
    from adbshell import clear
    from adbshell import adbcommand
    from adbshell import install
    from adbshell import changes
    from adbshell import github
    from adbshell import version
    from adbshell import builddate
    from adbshell import p
    from adbshell import adbfile
    from adbshell import conf   
except:
    from adbshell_alpha import errexit
    from adbshell_alpha import update
    from adbshell_alpha import checkinternet
    from adbshell_alpha import clear
    from adbshell_alpha import adbcommand
    from adbshell_alpha import install
    from adbshell_alpha import changes
    from adbshell_alpha import github
    from adbshell_alpha import version
    from adbshell_alpha import builddate
    from adbshell_alpha import p
    from adbshell_alpha import adbfile
    from adbshell_alpha import conf
class adbshellpyinformation:
    global conf
    p=None
    branch=None
    uselinuxpkgmanagertoinstalladb=None
    adbfile=None
    try:
        aapt=conf.get('adbshell', 'aaptfile')
    except:
        aapt=r'build-tools\android-10\aapt.exe' #windows
        #aapt=r'build-tools/android-10/aapt' #Linux
        #从旧版升级
    Permissionshow=True
class apk:
    pakname=None
    permissions=None
    minsdk=None
    targetsdk=None
    appname=None
    apkinstall= False #开发计划2
    apkfile=[]#开发计划2

aapt=adbshellpyinformation.aapt
Permissionshow=adbshellpyinformation.Permissionshow

def permissions(file):
    global aapt
    r=os.popen(aapt+' d permissions "'+file+'"')
    t=r.read()
    r.close()
    return t
    
def installaapt():
    global p ,conf ,aapt
    import urllib.request
    if p=='Linux':
        url='https://dl.google.com/android/repository/build-tools_r29.0.3-linux.zip'
        urllib.request.urlretrieve(url,'build-tools.zip') 
        z=zip.ZipFile('build-tools.zip','r')
        z.extractall(path='build-tools')
        z.close()
        aapt=r'build-tools/android-10/aapt'
        conf.set("adbshell", "aaptfile", aapt)
        conf.write(open("adbshell.ini", "w"))
    if p=='Windows':
        url='https://dl.google.com/android/repository/build-tools_r29.0.3-windows.zip'
        urllib.request.urlretrieve(url,'build-tools.zip')
        z=zip.ZipFile('build-tools.zip','r')
        z.extractall(path='build-tools')
        z.close()
        aapt=r'build-tools\android-10\aapt.exe'
        conf.set("adbshell", "aaptfile", aapt)
        conf.write(open("adbshell.ini", "w"))
    os.remove('build-tools.zip')
def apkinstallmode(install=False,file=[]):#开发计划2
    global p ,conf ,aapt ,Permissionshow ,adbfile
    if install==True:#apk安装模式
        '''
        if os.path.exists(str(aapt))==False:
            installaapt()
        '''
        if os.path.exists('build-tools')==False or os.path.exists(aapt)==False:
            installaapt()
        #开始apk安装
        print('您将要安装Android应用程序,个数:'+str(len(file))+' 您确定要安装吗?y/n')
        a=input('>>>')
        if a=='n' or a=='N':
            return
        for i in range(len(file)):
            nowfile=file[i]
            print('正在安装的程序:'+str(i)+'/'+str(len(file))+' 文件:'+nowfile)
            if Permissionshow:
                print(' 程序权限:'+permissions(nowfile))
            adbcommand().install(nowfile)
        print('安装完成!')
        sys.exit(0)
    if install==False:
        print('没有安装包需要安装.')
        input('按任意键继续')
        sys.exit(0)
def ParseArguments(args): #解析参数
    apkfile=[]
    apkinstall=False
    if len(args)==0:
        print('''adbshellpy_libapkfile.py [apkfile(s)]
        [apkfile(s)]       欲安装的apk文件 支持多个文件
        ''')
        return apkfile,apkinstall
    if os.path.exists(args[0]):#-1
        apkinstall=True
        for i in range(len(args)):
            if os.path.exists(args[i]):
                apkfile.append(args[i])
            else:
                break
        #apk file End
    return apkfile,apkinstall
def main(args):
    apkfile,apkinstall=ParseArguments(args)
    apk.apkfile=apkfile
    apk.apkinstall=apkinstall
    apkinstallmode(apk.apkinstall,apk.apkfile)
def mainex(list):
    apkinstallmode(True,list) 
if __name__ == '__main__':
    main(sys.argv[1:])