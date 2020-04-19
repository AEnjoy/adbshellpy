#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_libbrotli.py
#       By : 神郭
#  Version : 1.0
import sys,os
import zipfile as zip
class adbshellpyinformation:
    p=None
    branch=None
    uselinuxpkgmanagertoinstalladb=None
    adbfile=None
    aapt=None
    conf=None
    Permissionshow=True
class apk:
    pakname=None
    permissions=None
    minsdk=None
    targetsdk=None
    appname=None
    apkinstall= False #开发计划2
    apkfile=[]#开发计划2
p=adbshellpyinformation.p
adbfile=adbshellpyinformation.adbfile
aapt=adbshellpyinformation.aapt
Permissionshow=adbshellpyinformation.Permissionshow
conf=adbshellpyinformation.conf
def permissions(file):
    global aapt
    return os.popen(aapt+' d permissions "'+file+'"') 
    
def installaapt():
    global p ,conf ,aapt
    import urllib.request
    if p=='Linux':
        url='https://dl.google.com/android/repository/build-tools_r29.0.3-linux.zip'
        urllib.request.urlretrieve(url,'build-tools.zip') 
        z=zip.ZipFile('build-tools.zip','r')
        z.extractall(path='build-tools')
        z.close()
        aapt='build-tools/aapt'
        conf.set("adbshell", "aaptfile", aapt)
        conf.write(open("adbshell.ini", "w"))
    if p=='Windows':
        url='https://dl.google.com/android/repository/build-tools_r29.0.3-windows.zip'
        urllib.request.urlretrieve(url,'build-tools.zip')
        z=zip.ZipFile('build-tools.zip','r')
        z.extractall(path='build-tools')
        z.close()
        aapt='build-tools\aapt.exe'
        conf.set("adbshell", "aaptfile", aapt)
        conf.write(open("adbshell.ini", "w"))
        
def apkinstallmode(install=False,file=[]):#开发计划2
    global p ,conf ,aapt ,Permissionshow ,adbfile
    if install==True:#apk安装模式
        if os.path.exists(aapt)==False:
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
            os.system(adbfile+' install '+'"'+nowfile+'"' + ' -g -d')
        print('安装完成!')
        sys.exit(0)
    if install==True:
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
    if os.path.exists(args[1]):
        #文件输入 for处理apk文件,加入清单
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
    
if __name__ == '__main__':
    main(sys.argv[1:])