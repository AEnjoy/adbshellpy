#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_home.py
#       By : 神郭
#  Version : 0.6.2 
import sys,os,datetime
#Core Function
try:from adbshell import errexit,update,checkinternet,clear,ParseArguments,adbcommand,install,changes,github,version,builddate,who,nowdevice,shellex
except:from adbshell_alpha import errexit,update,checkinternet,clear,ParseArguments,adbcommand,install,changes,github,version,builddate,who,nowdevice,shellex
class adbshellpyinformation:
    p=sys.platform
    branch=None
    uselinuxpkgmanagertoinstalladb=None
    adbfile=None
    aapt=None
    def __init__(self):
        try:from adbshell_alpha import conf
        except:from adbshell import conf
        self.conf=conf
    Permissionshow=True
#HelperView
import adbshellpy_libhelper

def home():
    print('''
    **********************************Welcome*****************************************
    *                                ADBSystemTOOLBOX                                *
    *                       基于Python3&GoogleADB的安卓系统工具箱                    *
    *                     Develop:  CoolApkUser:白曦  Github:AEnjoy                  *
    *               如果你链接了多个设备,请先使用输入who命令再输入其它命令哦!        *
    **********************************Welcome*****************************************
    '''+'Version:'+version +'   buildDate:'+builddate)    
    print('''
     _____________________________ADBSystemTOOLBOX____________________________________
    ┃  工具箱指令:  ┃  help>  back   cls  set>  who>  home  exit    FixGithub       ┃
    ┃     re-install      update      environment      changes    clean-data        ┃
     ---------------------------------------------------------------------------------
    ┃  ADB指令集  : ┃ shell   root(√)                                              ┃
    ┃ 设备链接选项: ┃ start_server(√)  kill_server  devices tcpipconnect usb(√)   ┃
    ┃ 设备高级重启: ┃ reboot shutdown rec bl edl sideload download(SamsumgDevices)  ┃
     ---------------------------------------------------------------------------------
    ┃  应用  专区 : ┃ install> uninstall> disable> enable> clear> applist>          ┃    
    ┃  系统  优化 : ┃ 编译优化compile>                                              ┃
    ┃  文件  传输 : ┃ pull>        push>   screencap>                               ┃
    ┃  系统  调节 : ┃ windowmode>  input>  settings>  dumpsys>                      ┃
    ┃  应用  激活 : ┃ piebridge(黑域) shizuku  icebox(冰箱)   kfmark                ┃
    ┃  其它  功能 : ┃ APP安装关联:relatedapk                                        ┃
     ---------------------------------------------------------------------------------
    ┃  Magisk框架 : ┃                  <开发中,敬请期待>                            ┃
    ┃  ROOT  玩机 : ┃                  <开发中,敬请期待>                            ┃
    ┃  ROM   工具 : ┃                  <开发中,敬请期待>                            ┃    
     -------------------------------ADBSystemTOOLBOX----------------------------------
    ''')
    print('当前adbshellpy控制的设备:'+nowdevice+' \n 你可以使用who切换目标设备.(仅有一个设备时不会显示,但功能依然可用)')
class func_():
    def __init__(self):
        global nowdevice
        self.adb=adbcommand(nowdevice)
        global changes,github,version,builddate
        self.p=adbshellpyinformation.p
        self.adbfile=adbshellpyinformation.adbfile
        self.conf=adbshellpyinformation.conf
        self.changes=changes
    def kfmark(self):
        try:import adbshellpy_libroot
        except:    
            update().download_lib('adbshellpy_libroot')
            import adbshellpy_libroot
        adbshellpy_libroot.Activate_KFMark()
    def icebox(self):
        self.adb.shell('dpm set-device-owner com.catchingnow.icebox/.receiver.DPMReceiver')
    def relatedapk(self):
        import adbshellpy_libapkfile
        adbshellpy_libapkfile.relatedApkfile()
    def update(self):
        update().githubopen()
        update().updatecheck()
    def changes_(self):
        print(self.changes)
    def piebridge(self):
        self.adb.shell('sh /data/data/me.piebridge.brevent/brevent.sh')
    def shizuku(self):
        self.adb.shell('shizuku sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh')
    def push(self):
        print('push:从本地中复制一个文件(夹)至手机')
        urlp=input('远端路径>>>')
        if urlp=='':
            print('默认使用 /sdcard')
        urlc=input('本地文件或文件夹>>>')
        urlc=urlc.replace(" ", "")
        if urlc=='':
            print('本地文件或文件夹为空')
            errexit(4)
            return
        self.adb.push(urlc=urlc,urlp=urlp)
    def pull(self):
        print('pull:从手机中拉取一个文件(夹)至本地')
        urlp=input('远端路径>>>')
        urlp=urlp.replace(" ", "")
        if urlp=='':
            print('E:请输入有效远端路径')
            errexit(4)
            return
        urlc=input('本地路径>>>')
        if urlc=='':
            print('默认使用当前路径')
            urlc=os.getcwd()
        self.adb.pull(urlp=urlp,urlc=urlc)     
    def screencap(self):
        print('screencap:对手机执行截屏命令,并可选择是否传输至电脑并立即查看')
        h=input('传输至电脑并打开查看>>>[Y/N 默认N]')
        h=h.replace(" ", "")
        self.adb.shell(command='screencap -p /sdcard/sc.png')
        if h=='y' or h=='Y':
            self.adb.pull(urlp='/sdcard/sc.png',urlc='sc.png')
            if self.p == 'Windows':
                os.system('explorer sc.png')
            if self.p=='Linux':
                h=input('...LINUX查看?需要提前安装imagemagick>>>[Y/N 默认N]')
                if h=='y' or h=='Y':
                    os.system('display sc.png')
    def dumpsys(self):
        print('dumpsys:获取或设置一些调试信息(转储所有服务)。在adbmode→help→dumpsys查询命令列表')
        inputtext=input('dumpsys>>>')
        inputtext=inputtext.replace(" ", "")
        if inputtext=='' or inputtext=='back':
            return
        self.adb.adb_shell().shell_dumpsys()
        return
    def settings(self):
        print('通过ADB读取/更改系统设置 在adbmode→help→settings查询命令列表')
        print('''
        get [--user <USER_ID> | current] NAMESPACE KEY 设置键值
        ...检索KEY的当前值。
        put [--user <USER_ID> | current] NAMESPACE KEY VALUE [TAG] [default]
        ...将KEY的内容更改为VALUE
        ...设置为默认值，仅对全局/安全名称空间不区分大小写
        delete NAMESPACE KEY
        ...删除NAMESPACE KEY键值
        reset [--user <USER_ID> | current] NAMESPACE {PACKAGE_NAME | RESET_MODE}
        ...重置具有全局/安全模式的程序包的表。
        ...RESET_MODE:{untrusted_defaults，untrusted_clear，trusted_defaults}，不区分大小写
        list NAMESPACE
        ...列出所有设置的值 NAMESPACE:{system, secure, global}
        ''')
        inputtext=input('Command>>>')
        inputtext=inputtext.replace(" ", "")
        if inputtext=='' or inputtext=='back':
            return
        self.adb.adb_shell().shell_setting(func=inputtext)
    def input(self):
        print('''command:(Only Enter To Return)
        input_text:    向手机输入一串字符(不支持中文)
        input_keyevent:模拟输入内容(在adbshell→help→input中可查询指令)
        input_tap:     模拟点击屏幕上的一个像素点
        input_swipe:   模拟滑动屏幕(从一个像素点到另一像素点)
        ''')
        inputtext=input('command>>>')
        inputtext=inputtext.replace(" ", "")
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
        inputtext=input('欲查看或设置的信息>>>')
        inputtext=inputtext.replace(" ", "")
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
        args_=input('附加的参数>>>')
        args_=args_.replace(" ", "")
        if args_=='':
            self.adb.adb_shell().shell_pm_list_package()
            return
        self.adb.adb_shell().shell_pm_list_package(args_)
    def clear(self):
        Package=input('欲清除数据的程序包名>>>')
        Package=Package.replace(" ", "")
        if Package=='':
            errexit(4)
            return
        self.adb.adb_shell().shell_pm_clear(Package)
    def enable(self):
        Package=input('欲启用的程序包名>>>')
        Package=Package.replace(" ", "")
        if Package=='':
            errexit(4)
            return
        self.adb.adb_shell().shell_pm_enable(Package)
    def disable(self):
        Package=input('欲禁用的程序包名(使用applist查看)>>>')
        Package=Package.replace(" ", "")
        if Package=='':
            errexit(4)
            return
        self.adb.adb_shell().shell_pm_disable_user(Package)
    def compile(self):
        a=input('Compile:请选择compile功能模式: 1).传统  2).新版 :')
        if a=='1':
            mode=input('编译模式[默认-m speed]>>>')
            func=input('编译参数[默认 为空]>>>')
            pkg=input("编译对象[默认-a]>>>")
            func, pkg = func, pkg . replace(" ", "")
            if mode=='':
                mode='-m speed'
            if pkg=='':
                pkg='-a'
            print('执行该操作将消耗一定时间,请坐和放宽')
            start=datetime.datetime.now()
            print('当前时间: '+str(start))
            self.adb.adb_shell().shell_cmd_compile(method=mode,func=func,pkg=pkg)
            end=datetime.datetime.now()
            print('结束时间: '+str(end))
            print('执行用时: %s Seconds'%(end-start))
        if a=='2':
            print('''Compile :
            Compile New
            通过对AndroidN+的应用进行dexopt编译以提升性能
            注意:如果你使用的是Android Q 或更高版本,请谨慎对系统应用进行编译,特别是高危组件:
            com.android.systemui
            已知问题: 
            Android Q
            1.MIUI Android Q编译系统应用会导致严重掉帧
            2.Samsung OneUI 2.0+会出现开机无法进入桌面,系统全局黑屏的问题.
            3.LG UX 9 会在锁屏时死机重启
            4.com.android.systemui不支持通过手动安装还原!!!
            Android N / O
            1.编译不显示进度
            如果你是三星用户:推荐使用Galaxy Labs 的 App Booster,其原理为编译原理,且无安全风险
            性能:everything＞speed＞[默认]speed-profile＞quicken＞[不编译]
            编译耗时:everything＞speed
            空间占用:everything＞speed＞[默认]speed-profile＞quicken＞spacesave＞[不编译]
            **********************************Compile*****************************************
            *  (00).Back [Enter]                                                            *
            *  (01).使用everything模式编译所有应用[系统,用户] (强制)                           *
            *  (02).使用everything模式编译所有应用[系统,用户]                                  *
            *  (03).使用speed模式编译所有应用[系统,用户] (强制)                                *
            *  (04).使用speed模式编译所有应用[系统,用户]                                       *
            *       第一次编译优化,建议选择带有(强制)选项的方法                                 *
            *       对于小内存设备,低存储剩余的设备,emmc设备,推荐使用speed方法以减轻IO压力        *
            *       Android N O P 推荐以上选项(01-04),Android Q推荐以下选项(05-08)             *
            *  (05).使用everything模式编译所有应用[用户] (强制)                                *
            *  (06).使用everything模式编译所有应用[用户]                                       *
            *  (07).使用speed模式编译所有应用[用户] (强制)                                     *
            *  (08).使用speed模式编译所有应用[用户]                                            *
            *      急救功能                                                                  *
            *  (09).还原systemUI编译(quicken默认) ←推荐                                       *
            *  (10).还原systemUI编译(speed默认)                                               *
            *  (11).还原systemUI编译(清除编译)                                                *
            *  (12).清除第三方应用编译                                                        *
            *  (13).清除系统应用编译                                                          *
            *  (14).清除第三方应用编译[quicken]                                               *
            *  (15).清除系统应用编译[quicken]                                                 *            
            *  (16).清除所有编译[quicken]                                                    *
            *  (17).清除所有编译                                                             *
            *  Thanks: CoolApk User:后知                                                     *
            **********************************Compile*****************************************
            !:输入01 与 1 效果是一致的.
            ''')
            try:a=int(input('您的选择>>>'))
            except:a=0
            print('执行该操作将消耗一定时间,请坐和放宽')
            start=datetime.datetime.now()
            print('当前时间: '+str(start))
            self.adb.adb_shell().shell_cmd_compile(method=mode,func=func,pkg=pkg)      
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
            print('结束时间: '+str(end))
            print('执行用时: %s Seconds'%(end-start))
    def uninstall(self):
        apkfile=input('欲移除的程序包名(使用applist查看)>>>')
        args_=input('欲附加的参数>>>')
        if apkfile=='':
            errexit(4)
            return
        elif args_=='':
            self.adb.uninstall(apkfile)
            return
        self.adb.uninstall(apkfile,args_)
    def install(self):
        apkfile=input('欲安装的apk文件>>>')
        args_=input('欲附加的参数>>>')
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
    global nowdevice,f,shellex
    adb=adbcommand(nowdevice)
    inputtext=input('>>>')
    #inputtext=inputtext.replace(" ", "")
    global changes,github,version,builddate
    p=adbshellpyinformation.p
    adbfile=adbshellpyinformation.adbfile
    conf=adbshellpyinformation.conf
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
        print('''
        **********************************Setmode*****************************************
        *setting(default,Enter) 设置参数 cls 清屏 back 回到上一菜单 exit 退出            *
        *您也可以通过手动编辑adbshell.ini来修改设置                                      *
        **********************************Setmode*****************************************
        ''')
        return
    if inputtext =='exit':
        adb.kill_server()
        errexit(2)
        sys.exit(0)
    if inputtext =='environment':
        print('Version:'+version+' BuildDate:'+builddate+' Platform:'+p+' UpdateAddress:'+github+' AdbBin:'+adbfile)
        parseinput(a)
        return    
    if a==1:#2级目录(adbmode)
        if inputtext == '':
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
        if inputtext=='who':
            b=adb.s
            c=who()
            nowdevice=c
            adb=adbcommand(c)
            print('您当前的设备:'+b+'切换后的设备:'+c)
            parseinput(1)
            return
        if inputtext == 'back':
            print('E:您已处于主菜单!')
            parseinput(1)
            return
        if inputtext == 're-install':
            #重新安装
            install(p,2)
            parseinput(1)
            return
        if inputtext =='update':
            f.update()
            parseinput(0)
            return
        if inputtext =='changes':
            f.changes_()
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
            adbshellpy_libhelper.helper().usage()
            adbshellpy_libhelper.main()
            parseinput(1)
            return
        if inputtext=='clean-data':
            print('清除adbshellpy的数据,以恢复原始安装.输入yes继续.')
            if input('>>>')=='yes':
                adb.kill_server()
                os.rmdir('adb')
                os.rmdir('__pycache__')
                os.rmdir('build-tools')
                os.remove('adbshell.ini')
                print('操作执行完成,请重新运行实例以初始化')
                input()
                sys.exit()
        if shellex=='enable':
            adb.shell(inputtext)
            parseinput(1)
            return            
    if a==2:#2级目录(othermode)
            if inputtext =='back':
                parseinput(0)
                return
            if inputtext == 'setting' or inputtext == '':
                print('adbbin uselinuxpkgmanagertoinstalladb=enable [other]')
                print('[other]:'+str(conf.options('adbshell')))
                inputtext=input('欲设置的选项:>>>')
                if inputtext=='adbbin':
                    inputtext=input('ADBFile:>>>')
                    if os.path.exists(inputtext)== False:
                        print('E:指定的ADB File不存在,请检查Path!')
                        errexit(4)
                        parseinput(2)
                        return
                    h=input('您确定设置此项吗?Y/N>>><默认为Y>')
                    if h=='Y' or h=='y' or h=='':
                        conf.set("adbshell", "adbfile", inputtext)
                        conf.write(open("adbshell.ini", "w"))
                        parseinput(2)
                        return
                    print('W:放弃设置')
                    return
                if inputtext=='uselinuxpkgmanagertoinstalladb':
                    if p == "Windows":
                        print('E:该项仅对Linux生效')
                        errexit(4)
                        parseinput(2)
                        return
                    if p == "Linux":
                        inputtext=input('Set:>>>[默认enable]')
                    h=input('您确定设置此项吗?Y/N>>><默认为Y>')
                    if h=='Y' or h=='y' or h=='':
                        conf.set("adbshell", "uselinuxpkgmanagertoinstalladb", inputtext)
                        conf.write(open("adbshell.ini", "w"))
                        parseinput(2)
                        return
                    print('W:放弃设置')
                    return
                if inputtext=='':
                    parseinput(2)
                    return
                #otherSet
                inputtext_=input('SET:>>>')
                h=input('您确定设置此项吗?Y/N>>><默认为Y>')
                if h=='Y' or h=='y' or h=='':
                    conf.set("adbshell", inputtext, inputtext_)
                    conf.write(open("adbshell.ini", "w"))
                    parseinput(2)
                    return
                parseinput(0)
                return
            errexit(2)
    print('W :未知指令')
    parseinput(a)
    return
    