#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_home.py
#       By : 神郭
#  Version : 1.0
import sys,os,datetime
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
    p=sys.platform
    branch=None
    uselinuxpkgmanagertoinstalladb=None
    adbfile=None
    aapt=None
    conf=None
    Permissionshow=True
try:
    import adbshellpy_libhelper
except:
    update().download_lib('adbshellpy_libhelper')
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
    ┃  工具箱指令:  ┃  help>  back   cls  set>  who>  home  exit                   ┃
    ┃           re-install      update      environment      changes                ┃
     ---------------------------------------------------------------------------------
    ┃  ADB指令集  : ┃ shell   root(√)                                             ┃
    ┃ 设备链接选项: ┃ start_server(√)  kill_server  devices tcpipconnect usb(√)  ┃
    ┃ 设备高级重启: ┃ reboot shutdown rec bl edl sideload download(SamsumgDevices) ┃
     ---------------------------------------------------------------------------------
    ┃  应用  专区 : ┃ install> uninstall> disable> enable> clear> applist>         ┃    
    ┃  系统  优化 : ┃ 编译优化compile>                                             ┃
    ┃  文件  传输 : ┃ pull>        push>   screencap>                              ┃
    ┃  系统  调节 : ┃ windowmode>  input>  settings>  dumpsys>                     ┃
    ┃  应用  激活 : ┃ piebridge(黑域) shizuku  icebox(冰箱)                        ┃
    ┃  其它  功能 : ┃ APP安装关联:relatedapk                                       ┃
     ---------------------------------------------------------------------------------
    ┃  Magisk框架 : ┃                  <开发中,敬请期待>                           ┃
    ┃  ROOT  玩机 : ┃                  <开发中,敬请期待>                           ┃
    ┃  ROM   工具 : ┃                  <开发中,敬请期待>                           ┃
     -------------------------------ADBSystemTOOLBOX----------------------------------
    ''')
    print('当前adbshellpy控制的设备:'+nowdevice+' \n 你可以使用who切换目标设备')

def parseinput(a=1):#1二级目录(adbmode) 2二级目录(othermode)
    global nowdevice
    adb=adbcommand(nowdevice)
    inputtext=input('>>>')
    inputtext=inputtext.replace(" ", "")
    global changes,github,version,builddate
    p=adbshellpyinformation.p
    adbfile=adbshellpyinformation.adbfile
    conf=adbshellpyinformation.conf
    if a==1:#2级目录(adbmode)
        if inputtext == '':
            parseinput(1)
            return
        if inputtext == 'icebox':
            adb.shell('dpm set-device-owner com.catchingnow.icebox/.receiver.DPMReceiver')
            parseinput(1)
            return
        if inputtext == 'relatedapk':
            import adbshellpy_libapkfile
            adbshellpy_libapkfile.relatedApkfile()
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
        if inputtext == 'help':
            adbshellpy_libhelper.helper().usage()
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
            import webbrowser
            webbrowser.open(github)
            parseinput(0)
            return
        if inputtext =='changes':
            print(changes)
            parseinput(1)
            return
        if inputtext=='piebridge':
            adb.shell('sh /data/data/me.piebridge.brevent/brevent.sh')
            parseinput(1)
            return
        if inputtext=='shizuku':
            adb.shell('shizuku sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh')
            parseinput(1)
            return
        if inputtext=='push':
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
            adb.push(urlc=urlc,urlp=urlp)
            parseinput(1)
            return
        if inputtext=='pull':
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
            adb.pull(urlp=urlp,urlc=urlc)
            parseinput(1)
            return
        if inputtext=='screencap':
            print('screencap:对手机执行截屏命令,并可选择是否传输至电脑并立即查看')
            h=input('传输至电脑并打开查看>>>[Y/N 默认N]')
            h=h.replace(" ", "")
            adb.shell(command='screencap -p /sdcard/sc.png')
            if h=='y' or h=='Y':
                adb.pull(urlp='/sdcard/sc.png',urlc='sc.png')
                if p == 'Windows':
                    os.system('explorer sc.png')
                if p=='Linux':
                    inputtext=input('...LINUX查看?需要提前安装imagemagick>>>[Y/N 默认N]')
                    if h=='y' or h=='Y':
                        os.system('display sc.png')
            parseinput(1)
            return
        if inputtext=='dumpsys':
            print('dumpsys:获取或设置一些调试信息(转储所有服务)。在adbmode→help→dumpsys查询命令列表')
            inputtext=input('dumpsys>>>')
            inputtext=inputtext.replace(" ", "")
            if inputtext=='' or inputtext=='back':
                parseinput(1)
                return
            adb.adb_shell().shell_dumpsys()
            parseinput(1)
            return
        if inputtext=='settings':
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
                parseinput(1)
                return
            adb.adb_shell().shell_setting(func=inputtext)
            parseinput(1)
            return
        if inputtext=='input':
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
                adb.adb_shell().shell_input_text(func=inputtext)
                parseinput(1)
                return
            if inputtext=='input_keyevent':
                inputtext=input('Keyevent>>>')
                adb.adb_shell().shell_input_keyevent(func=inputtext)
                parseinput(1)
                return
            if inputtext=='input_tap':
                x=input('X>>>')
                y=input('Y>>>')
                adb.adb_shell().shell_input_tap(x=x,y=y)
                parseinput(1)
                return
            if inputtext=='input_swipe':
                x1=input('X1>>>')
                y1=input('Y1>>>')
                x2=input('X2>>>')
                y2=input('Y2>>>')
                d =input('D>>>')
                adb.adb_shell().shell_input_swipe(x1=x1,x2=x2,y1=y1,y2=y2,d=d)
                parseinput(1)
                return
            if inputtext=='':
                parseinput(1)
                return
        if inputtext=='windowmode':
            inputtext=input('欲查看或设置的信息>>>')
            inputtext=inputtext.replace(" ", "")
            if inputtext=='':
                adb.adb_shell().shell_wm()
                parseinput(1)
                return
            if inputtext=='overscan':
                inputtext=input('...overscan>>>')
                if inputtext=='reset':
                    adb.adb_shell().shell_wm_overscan('reset')
                    parseinput(1)
                    return
                if inputtext=='':
                    adb.adb_shell().shell_wm_overscan()
                    parseinput(1)
                    return
                adb.adb_shell().shell_wm_overscan(inputtext)
                parseinput(1)
                return
            if inputtext=='size':
                inputtext=input('...size>>>')
                inputtext=inputtext.replace(" ", "")
                if inputtext=='reset':
                    adb.adb_shell().shell_wm_size(func='reset')
                    parseinput(1)
                    return
                if inputtext=='':
                    adb.adb_shell().shell_wm_size()
                    parseinput(1)
                    return
                adb.adb_shell().shell_wm_size(func=inputtext)
                parseinput(1)
                return
            if inputtext=='density':
                inputtext=input('...density>>>')
                inputtext=inputtext.replace(" ", "")
                if inputtext=='reset':
                    adb.adb_shell().shell_wm_density(func='reset')
                    parseinput(1)
                    return
                if inputtext=='':
                    adb.adb_shell().shell_wm_density()
                    parseinput(1)
                    return
                adb.adb_shell().shell_wm_density(func=inputtext)
                parseinput(1)
                return
        if inputtext=='':
            parseinput(1)
            return
        if inputtext=='applist':
            args_=input('附加的参数>>>')
            args_=args_.replace(" ", "")
            if args_=='':
                adb.adb_shell().shell_pm_list_package()
                parseinput(1)
                return
            adb.adb_shell().shell_pm_list_package(args_)
            parseinput(1)
            return
        if inputtext=='clear':
            Package=input('欲清除数据的程序包名(使用applist查看)>>>')
            Package=Package.replace(" ", "")
            if Package=='':
                errexit(4)
                parseinput(1)
                return
            adb.adb_shell().shell_pm_clear(Package)
            parseinput(1)
            return
        if inputtext=='enable':
            Package=input('欲启用的程序包名(使用applist查看)>>>')
            Package=Package.replace(" ", "")
            if Package=='':
                errexit(4)
                parseinput(1)
                return
            adb.adb_shell().shell_pm_enable(Package)
            parseinput(1)
            return
        if inputtext=='disable':
            Package=input('欲禁用的程序包名(使用applist查看)>>>')
            Package=Package.replace(" ", "")
            if Package=='':
                errexit(4)
                parseinput(1)
                return
            adb.adb_shell().shell_pm_disable_user(Package)
            parseinput(1)
            return
        if inputtext=='compile':
            mode=input('编译模式[默认-m speed]>>>')
            func=input('编译参数[默认 为空]>>>')
            pkg=input("编译对象[默认-a]>>>")
            func, pkg = func, pkg . replace(" ", "")
            if mode=='':
                mode='-m speed'
            '''if func =='':
                func='-f'''
            if pkg=='':
                pkg='-a'
            print('执行该操作将消耗一定时间,请坐和放宽')
            start=datetime.datetime.now()
            print('当前时间: '+str(start))
            adb.adb_shell().shell_cmd_compile(method=mode,func=func,pkg=pkg)
            end=datetime.datetime.now()
            print('结束时间: '+str(end))
            print('执行用时: %s Seconds'%(end-start))
            parseinput(1)
            return
        if inputtext=='uninstall':
            apkfile=input('欲移除的程序包名(使用applist查看)>>>')
            args_=input('欲附加的参数>>>')
            if apkfile=='':
                errexit(4)
                parseinput(1)
                return
            elif args_=='':
                adb.uninstall(apkfile)
                parseinput(1)
                return
            adb.uninstall(apkfile,args_)
        if inputtext=='install':
            apkfile=input('欲安装的apk文件>>>')
            args_=input('欲附加的参数>>>')
            if apkfile=='':
                errexit(4)
                parseinput(1)
                return
            elif args_=='':
                adb.install(apkfile=apkfile)
                parseinput(1)
                return
            adb.install(apkfile,args_)
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
        if inputtext=='back':
            parseinput(1)
            return
        if inputtext == 'help':
            adbshellpy_libhelper.main()
    if a==2:#2级目录(othermode)
            if inputtext =='back':
                parseinput(0)
                return
            if inputtext == 'setting' or inputtext == '':
                print('adbbin uselinuxpkgmanagertoinstalladb=enable [other]')
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
                #print('E:暂未开放setting,请手动编辑adbshell.ini')
            errexit(2)
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
    print('W :未知指令')
    parseinput(a)
    return
    