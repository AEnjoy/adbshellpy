#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_home.py
#       By : 神郭
#  Version : 0.7.3
import sys,os,datetime
#Core Function
try:from adbshell import errexit,update,checkinternet,clear,ParseArguments,adbcommand,install,changes,github,version,builddate,who,nowdevice,shellex,logging,Luan,adbfile
except:from adbshell_alpha import errexit,update,checkinternet,clear,ParseArguments,adbcommand,install,changes,github,version,builddate,who,nowdevice,shellex,logging,Luan,adbfile
class adbshellpyinformation:
    def __init__(self):
        try:from adbshell_alpha import conf
        except:from adbshell import conf
        '''
        try:from adbshell_alpha import adbfile
        except:from adbshell import adbfile    
        self.adbfile=adbfile
        '''
        self.conf=conf
    p=sys.platform
    branch=None
    uselinuxpkgmanagertoinstalladb=None
    aapt=None
    adbfile=''        
    Permissionshow=True
#HelperView
import adbshellpy_libhelper

def home():
    global Luan
    logging.info('Welcome to adbsystemtoolbox!')
    print(Luan.ltext3+'Version:'+version +'   buildDate:'+builddate)    
    print(Luan.ltext4)
    print(Luan.i7+nowdevice+Luan.i8)
class func_():
    global Luan
    def __init__(self):
        global nowdevice
        self.adb=adbcommand(nowdevice)
        global changes,github,version,builddate
        self.p=adbshellpyinformation.p
        self.adbfile=adbshellpyinformation.adbfile
        self.changes=changes
    def kfmark(self):
        logging.info('Func:kfmark')
        try:import adbshellpy_libroot
        except:    
            update().download_lib('adbshellpy_libroot')
            import adbshellpy_libroot
        adbshellpy_libroot.Activate_KFMark()
    def icebox(self):
        logging.info('Func:icebox')
        self.adb.shell('dpm set-device-owner com.catchingnow.icebox/.receiver.DPMReceiver')
    def relatedapk(self):
        logging.info('Func:relateapk')
        import adbshellpy_libapkfile
        adbshellpy_libapkfile.relatedApkfile()
    def update(self):
        logging.info('Func:update')
        update().githubopen()
        update().updatecheck()
    def changes_(self):
        print(self.changes)
    def piebridge(self):
        logging.info('Func:piebridge')
        self.adb.shell('sh /data/data/me.piebridge.brevent/brevent.sh')
    def shizuku(self):
        logging.info('Func:shizuku')
        self.adb.shell('shizuku sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh')
    def push(self):
        logging.info('Func:push')
        print(Luan.i9)
        urlp=input(Luan.i10)
        if urlp=='':
            print(Luan.i11)
        urlc=input(Luan.i12)
        urlc=urlc.replace(" ", "")
        if urlc=='':
            print(Luan.e10)
            errexit(4)
            return
        self.adb.push(urlc=urlc,urlp=urlp)
    def pull(self):
        logging.info('Func:pull')
        print(Luan.i13)
        urlp=input(Luan.i10)
        #urlp=urlp.replace(" ", "")
        logging.info('Func:pull p is:'+urlp)
        if urlp=='':
            print(Luan.e11)
            errexit(4)
            return
        urlc=input(Luan.i38)
        logging.info('Func:pull c is:'+urlc)
        if urlc=='':
            print(Luan.i14)
            urlc=os.getcwd()
        self.adb.pull(urlp=urlp,urlc=urlc)     
    def screencap(self):
        logging.info('Func:screencap')
        print(Luan.i15)
        h=input(Luan.a3)
        h=h.replace(" ", "")
        self.adb.shell(command='screencap -p /sdcard/sc.png')
        if h=='y' or h=='Y':
            self.adb.pull(urlp='/sdcard/sc.png',urlc='sc.png')
            if self.p == 'Windows':
                os.system('explorer sc.png')
            if self.p=='Linux':
                h=input(Luan.a4)
                if h=='y' or h=='Y':
                    os.system('display sc.png')
    def dumpsys(self):
        logging.info('Func:dumpsys')
        print(Luan.i16)
        inputtext=input('dumpsys>>>')
        logging.info('Func:dumpsysy input:'+inputtext)
        inputtext=inputtext.replace(" ", "")
        if inputtext=='' or inputtext=='back':
            return
        self.adb.adb_shell().shell_dumpsys()
        return
    def settings(self):
        logging.info('Func:settings')
        print(Luan.i17)
        print(Luan.ltext5)
        inputtext=input('Command>>>')
        logging.info('Func:settings input:'+inputtext)
        inputtext=inputtext.replace(" ", "")
        if inputtext=='' or inputtext=='back':
            return
        self.adb.adb_shell().shell_setting(func=inputtext)
    def input(self):
        logging.info('Func:input')
        print(Luan.ltext6)
        inputtext=input('command>>>')
        inputtext=inputtext.replace(" ", "")
        logging.info('Func:input input:'+inputtext)
        if inputtext=='input_text':
            inputtext=input('Text>>>')
            self.adb.adb_shell().shell_input_text(func=inputtext)
            return
        if inputtext=='input_keyevent':
            inputtext=input('Keyevent>>>')
            self.adb.adb_shell().shell_input_keyevent(func=inputtext)
            return
        if inputtext=='input_tap':
            x=input('X>>>')
            y=input('Y>>>')
            self.adb.adb_shell().shell_input_tap(x=x,y=y)
            return
        if inputtext=='input_swipe':
            x1=input('X1>>>')
            y1=input('Y1>>>')
            x2=input('X2>>>')
            y2=input('Y2>>>')
            d =input('D>>>')
            self.adb.adb_shell().shell_input_swipe(x1=x1,x2=x2,y1=y1,y2=y2,d=d)
            return
    def windowmode(self):
        logging.info('Func:windowmode')
        inputtext=input(Luan.i18)
        inputtext=inputtext.replace(" ", "")
        logging.info('Func:wm input:'+inputtext)
        if inputtext=='':
            self.adb.adb_shell().shell_wm()
            return
        if inputtext=='overscan':
            inputtext=input('...overscan>>>')
            if inputtext=='reset':
                self.adb.adb_shell().shell_wm_overscan('reset')
                return
            if inputtext=='':
                self.adb.adb_shell().shell_wm_overscan()
                return
            self.adb.adb_shell().shell_wm_overscan(inputtext)
            return
        if inputtext=='size':
            inputtext=input('...size>>>')
            inputtext=inputtext.replace(" ", "")
            if inputtext=='reset':
                self.adb.adb_shell().shell_wm_size(func='reset')
                return
            if inputtext=='':
                self.adb.adb_shell().shell_wm_size()
                return
            self.adb.adb_shell().shell_wm_size(func=inputtext)
            return
        if inputtext=='density':
            inputtext=input('...density>>>')
            inputtext=inputtext.replace(" ", "")
            if inputtext=='reset':
                self.adb.adb_shell().shell_wm_density(func='reset')
                return
            if inputtext=='':
                self.adb.adb_shell().shell_wm_density()
                return
            self.adb.adb_shell().shell_wm_density(func=inputtext)
            return
    def applist(self):
        logging.info('Func:applist')
        args_=input(Luan.i19)
        logging.info('Func:applist input:'+args_)
        args_=args_.replace(" ", "")
        if args_=='':
            self.adb.adb_shell().shell_pm_list_package()
            return
        self.adb.adb_shell().shell_pm_list_package(args_)
    def clear(self):
        logging.info('Func:clear')
        Package=input(Luan.i20)
        logging.info('Func:clear input:'+Package)
        Package=Package.replace(" ", "")
        if Package=='':
            errexit(4)
            return
        self.adb.adb_shell().shell_pm_clear(Package)
    def enable(self):
        logging.info('Func:enable')
        Package=input(Luan.i21)
        logging.info('Func:enable input:'+Package)
        Package=Package.replace(" ", "")
        if Package=='':
            errexit(4)
            return
        self.adb.adb_shell().shell_pm_enable(Package)
    def disable(self):
        logging.info('Func:disable')
        Package=input(Luan.i22)
        Package=Package.replace(" ", "")
        logging.info('Func:disable input:'+Package)
        if Package=='':
            errexit(4)
            return
        self.adb.adb_shell().shell_pm_disable_user(Package)
    def compile(self):
        logging.info('Func:compile')
        a=input(Luan.a5)
        logging.info('Func:mode input:'+a)
        if a=='1':
            logging.info('Func:compile mode is 1')
            mode=input(Luan.i23)
            func=input(Luan.i24)
            pkg=input(Luan.i25)
            logging.info("Func:compile input mode func pkg:'" +mode+"' '"+func+"' '"+pkg+"'")
            func, pkg = func, pkg . replace(" ", "")
            if mode=='':
                mode='-m speed'
            if pkg=='':
                pkg='-a'
            print(Luan.i26)
            start=datetime.datetime.now()
            print(Luan.i27+str(start))
            self.adb.adb_shell().shell_cmd_compile(method=mode,func=func,pkg=pkg)
            end=datetime.datetime.now()
            print(Luan.i28+str(end))
            print(Luan.i29%(end-start))
        if a=='2':
            logging.info('Func:compile mode is 2')
            print(Luan.ltext7)
            if os.path.exists('libshfile')==False:
                update().download_lib_shfile('compile-5.sh')
                update().download_lib_shfile('compile-6.sh')
                update().download_lib_shfile('compile-7.sh')
                update().download_lib_shfile('compile-8.sh')
                update().download_lib_shfile('compile-12.sh')
                update().download_lib_shfile('compile-13.sh')
                update().download_lib_shfile('compile-14.sh')
                update().download_lib_shfile('compile-15.sh')
            try:a=int(input(Luan.i30))
            except:a=0
            print(Luan.i26)
            logging.info('Func:compile mode:User Choose:'+str(a))
            start=datetime.datetime.now()
            print(Luan.i27+str(start))
            logging.info('Func:compile start time is:'+str(start))
            if a==1:self.adb.adb_shell().shell_cmd_compile('-m everything','-f','-a')
            if a==2:self.adb.adb_shell().shell_cmd_compile('-m everything','','-a')
            if a==3:self.adb.adb_shell().shell_cmd_compile('-m speed','-f','-a')
            if a==4:self.adb.adb_shell().shell_cmd_compile('-m speed','','-a')    
            if a==9:self.adb.adb_shell().shell_cmd_compile('-m quicken','-f','com.android.systemui')
            if a==10:self.adb.adb_shell().shell_cmd_compile('-m speed','-f','com.android.systemui')
            if a==11:self.adb.shell('cmd package compile --reset com.android.systemui')
            if a==16:self.adb.adb_shell().shell_cmd_compile('-m quicken','-f','-a')
            if a==17:self.adb.shell('cmd package compile --reset -a')
            if a==5:
                self.adb.push('libshfile/compile-5.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==6:
                self.adb.push('libshfile/compile-6.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==7:
                self.adb.push('libshfile/compile-7.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==8:
                self.adb.push('libshfile/compile-8.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==12:
                self.adb.push('libshfile/compile-12.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==13:
                self.adb.push('libshfile/compile-13.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==14:
                self.adb.push('libshfile/compile-14.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==15:
                self.adb.push('libshfile/compile-15.sh','/sdcard/temp.sh')
                self.adb.shell('su -c sh /sdcard/temp.sh')
                self.adb.shell('rm /sdcard/temp.sh')
            if a==0:return
            end=datetime.datetime.now()
            print(Luan.i28+str(end))
            logging.info('Func:compile end time is:'+str(end))
            logging.info('Func:compile time is: %s '%(end-start))
            print(Luan.i29%(end-start))
    def uninstall(self):
        logging.info('Func:uninstall')
        apkfile=input(Luan.i31)
        args_=input(Luan.i19)
        logging.info('Func:uninstall pak args_'+apkfile+' '+args_)
        if apkfile=='':
            errexit(4)
            return
        elif args_=='':
            self.adb.uninstall(apkfile)
            return
        self.adb.uninstall(apkfile,args_)
    def install(self):
        logging.info('Func:install')
        apkfile=input(Luan.i32)
        args_=input(Luan.i19)
        logging.info('Func:install apk_file args_'+apkfile+' '+args_)
        if apkfile=='':
            errexit(4)
            return
        elif args_=='':
            self.adb.install(apkfile=apkfile)
            return
        self.adb.install(apkfile,args_)
    def download(self):self.adb.reboot(5)
    def sideload(self):self.adb.reboot(4)
    def edl(self):self.adb.reboot(6)
    def rec(self):self.adb.reboot(3)
    def bl(self):self.adb.reboot(2)
    def shutdown(self):self.adb.reboot(1)
    def reboot(self):self.adb.reboot()
    def usb(self):self.adb.usb()
    def tcpipconnect(self):self.adb.tcpip()
    def devices(self):self.adb.devices()
    def kill_server(self):self.adb.kill_server()
    def start_server(self):self.adb.start_server()
    def root(self):self.adb.root()
    def shell(self):self.adb.shell()

f=func_()

def parseinput(a=1):#1二级目录(adbmode) 2二级目录(othermode)
    global nowdevice,f,shellex,Luan
    adb=adbcommand(nowdevice)
    inputtext=input('>>>')
    #inputtext=inputtext.replace(" ", "")
    global changes,github,version,builddate,adbfile
    p=adbshellpyinformation.p
    #adbfile=adbshellpyinformation.adbfile
    try:from adbshell_alpha import conf
    except:from adbshell import conf
    logging.info("Input is:'"+inputtext +"'  Device is:"+nowdevice)
    #通用指令
    if inputtext=='home':
        home()
        parseinput()
        return
    if inputtext == 'cls':
        clear()
        parseinput(a)
        return
    if inputtext == 'set':
        print(Luan.ltext1)
        parseinput(2)
        return
    if inputtext =='exit':
        adb.kill_server()
        errexit(2)
        sys.exit(0)
    if inputtext =='environment':
        print('Version:'+version+' BuildDate:'+builddate+' Platform:'+p+' UpdateAddress:'+github+' AdbBin:'+adbfile)
        parseinput(a)
        return
    if inputtext=='who':
        b=adb.s
        c=who()
        nowdevice=c
        adb=adbcommand(c)
        print(Luan.i33+b+Luan.i34+c)
        parseinput(1)
        return
    if inputtext == 're-install':
        #重新安装
        install(p,2)
        parseinput(1)
        return
    if inputtext =='update':
        f.update()
        parseinput(1)
        return
    if inputtext =='changes':
        f.changes_()
        parseinput(1)
        return        
    if a==1:#2级目录(adbmode)
        if inputtext == '':
            parseinput(1)
            return
        if inputtext == 'back':
            print(Luan.e12)
            parseinput(1)
            return            
        if inputtext=='kfmark':
            f.kfmark()
            parseinput(1)
            return            
        if inputtext == 'icebox':
            f.icebox()
            parseinput(1)
            return
        if inputtext == 'relatedapk':
            f.relatedapk()
            parseinput(1)
            return            
        if inputtext=='piebridge':
            f.piebridge()
            parseinput(1)
            return
        if inputtext=='shizuku':
            f.shizuku()
            parseinput(1)
            return
        if inputtext=='push':
            f.push()
            parseinput(1)
            return
        if inputtext=='pull':
            f.pull()
            parseinput(1)
            return
        if inputtext=='screencap':
            f.screencap()
            parseinput(1)
            return
        if inputtext=='dumpsys':
            f.dumpsys()
            parseinput(1)
            return
        if inputtext=='settings':
            f.settings()
            parseinput(1)
            return
        if inputtext=='input':
            f.input()
            parseinput(1)
            return
        if inputtext=='windowmode':
            f.windowmode()
            parseinput(1)
            return
        if inputtext=='':
            parseinput(1)
            return
        if inputtext=='applist':
            f.applist()
            parseinput(1)
            return
        if inputtext=='clear':
            f.clear()
            parseinput(1)
            return
        if inputtext=='enable':
            f.enable()
            parseinput(1)
            return
        if inputtext=='disable':
            f.disable()
            parseinput(1)
            return
        if inputtext=='compile':
            f.compile()
            parseinput(1)
            return
        if inputtext=='uninstall':
            f.uninstall()
            parseinput(1)
            return
        if inputtext=='install':
            f.install()
            parseinput(1)
            return
        if inputtext=='download':
            adb.reboot(mode=5)
            parseinput(1)
            return
        if inputtext=='sideload':
            adb.reboot(mode=4)
            parseinput(1)
            return
        if inputtext=='bl':
            adb.reboot(mode=2)
            parseinput(1)
            return
        if inputtext=='rec':
            adb.reboot(mode=3)
            parseinput(1)
            return
        if inputtext=='shutdown':
            adb.reboot(mode=1)
            parseinput(1)
            return
        if inputtext=='reboot':#0 不带参数 1.-p 2.fastboot(bl) 3.recovery 4.sideload 5.挖煤
            adb.reboot()
            parseinput(1)
            return
        if inputtext=='usb':
            adbcommand.usb()
            parseinput(1)
            return
        if inputtext=='tcpipconnect':
            adbcommand.tcpip()
            parseinput(1)
            return
        if inputtext=='devices':
            adb.devices()
            parseinput(1)
            return
        if inputtext=='kill_server':
            adb.kill_server()
            parseinput(1)
            return
        if inputtext=='start_server':
            adb.start_server()
            parseinput(1)
            return
        if inputtext=='root':
            adb.root()
            parseinput(1)
            return
        if inputtext=='shell':
            adb.shell()
            parseinput(1)
            return
        if inputtext.lower()=='fixgithub':
            update().fixgithub()
            parseinput(1)
            return            
        if inputtext=='back':
            parseinput(1)
            return
        if inputtext == 'help':
            logging.info('Into Helper View.')
            adbshellpy_libhelper.helper().usage()
            adbshellpy_libhelper.main()
            logging.info('Helper View Exit.')
            parseinput(1)
            return
        if inputtext=='clean-data':
            logging.info('Func:clean-data')
            print(Luan.a6)
            if input('>>>')=='yes':
                logging.info('Func:clean-data:input is yes,clean.')
                adb.kill_server()
                os.rmdir('adb')
                os.rmdir('__pycache__')
                os.rmdir('build-tools')
                os.remove('adbshell.ini')
                print(Luan.i35)
                logging.info('Func:Done. Exit.')
                input()
                sys.exit()
        if shellex=='enable':
            adb.shell(inputtext)
            parseinput(1)
            return            
    if a==2:#2级目录(othermode)
            logging.info('Now,you are in mode 2')
            if inputtext =='back':
                parseinput(1)
                return
            if inputtext == 'setting' or inputtext == '':
                logging.info('Func:mode2:setting')
                print('adbbin uselinuxpkgmanagertoinstalladb=enable [other]')
                print('[other]:'+str(conf.options('adbshell')))
                inputtext=input(Luan.i36)
                if inputtext=='adbbin':
                    inputtext=input('ADBFile:>>>')
                    if os.path.exists(inputtext)== False:
                        print(Luan.i37)
                        errexit(4)
                        parseinput(2)
                        return
                    h=input(Luan.a7)
                    if h=='Y' or h=='y' or h=='':
                        conf.set("adbshell", "adbfile", inputtext)
                        conf.write(open("adbshell.ini", "w"))
                        parseinput(2)
                        return
                    print(Luan.w5)
                    return
                if inputtext=='uselinuxpkgmanagertoinstalladb':
                    if p == "Windows":
                        print(Luan.e13)
                        errexit(4)
                        parseinput(2)
                        return
                    if p == "Linux":
                        inputtext=input('Set:>>>[默认enable]')
                    h=input(Luan.a7)
                    if h=='Y' or h=='y' or h=='':
                        conf.set("adbshell", "uselinuxpkgmanagertoinstalladb", inputtext)
                        conf.write(open("adbshell.ini", "w"))
                        parseinput(2)
                        return
                    print(Luan.w5)
                    return
                if inputtext=='':
                    parseinput(2)
                    return
                #otherSet
                inputtext_=input('SET:>>>')
                h=input(Luan.a7)
                if h=='Y' or h=='y' or h=='':
                    conf.set("adbshell", inputtext, inputtext_)
                    conf.write(open("adbshell.ini", "w"))
                    parseinput(2)
                    return
                parseinput(1)
                return
            errexit(2)
    print(Luan.w6)
    parseinput(a)
    return
    