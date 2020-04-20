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

def parseinput(a=1):#1二级目录(adbmode) 2二级目录(othermode)
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
            adbcommand().shell('sh /data/data/me.piebridge.brevent/brevent.sh')
            parseinput(1)
            return
        if inputtext=='shizuku':
            adbcommand().shell('shizuku sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh')
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
            adbcommand().push(urlc=urlc,urlp=urlp)
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
            adbcommand().pull(urlp=urlp,urlc=urlc)
            parseinput(1)
            return
        if inputtext=='screencap':
            print('screencap:对手机执行截屏命令,并可选择是否传输至电脑并立即查看')
            h=input('传输至电脑并打开查看>>>[Y/N 默认N]')
            h=h.replace(" ", "")
            adbcommand().shell(command='screencap -p /sdcard/sc.png')
            if h=='y' or h=='Y':
                adbcommand().pull(urlp='/sdcard/sc.png',urlc='sc.png')
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
            adbcommand().adb_shell().shell_dumpsys()
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
            adbcommand().adb_shell().shell_setting(func=inputtext)
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
                adbcommand().adb_shell().shell_input_text(func=inputtext)
                parseinput(1)
                return
            if inputtext=='input_keyevent':
                inputtext=input('Keyevent>>>')
                adbcommand().adb_shell().shell_input_keyevent(func=inputtext)
                parseinput(1)
                return
            if inputtext=='input_tap':
                x=input('X>>>')
                y=input('Y>>>')
                adbcommand().adb_shell().shell_input_tap(x=x,y=y)
                parseinput(1)
                return
            if inputtext=='input_swipe':
                x1=input('X1>>>')
                y1=input('Y1>>>')
                x2=input('X2>>>')
                y2=input('Y2>>>')
                d =input('D>>>')
                adbcommand().adb_shell().shell_input_swipe(x1=x1,x2=x2,y1=y1,y2=y2,d=d)
                parseinput(1)
                return
            if inputtext=='':
                parseinput(1)
                return
        if inputtext=='windowmode':
            inputtext=input('欲查看或设置的信息>>>')
            inputtext=inputtext.replace(" ", "")
            if inputtext=='':
                adbcommand().adb_shell().shell_wm()
                parseinput(1)
                return
            if inputtext=='overscan':
                inputtext=input('...overscan>>>')
                if inputtext=='reset':
                    adbcommand().adb_shell().shell_wm_overscan('reset')
                    parseinput(1)
                    return
                if inputtext=='':
                    adbcommand().adb_shell().shell_wm_overscan()
                    parseinput(1)
                    return
                adbcommand().adb_shell().shell_wm_overscan(inputtext)
                parseinput(1)
                return
            if inputtext=='size':
                inputtext=input('...size>>>')
                inputtext=inputtext.replace(" ", "")
                if inputtext=='reset':
                    adbcommand().adb_shell().shell_wm_size(func='reset')
                    parseinput(1)
                    return
                if inputtext=='':
                    adbcommand().adb_shell().shell_wm_size()
                    parseinput(1)
                    return
                adbcommand().adb_shell().shell_wm_size(func=inputtext)
                parseinput(1)
                return
            if inputtext=='density':
                inputtext=input('...density>>>')
                inputtext=inputtext.replace(" ", "")
                if inputtext=='reset':
                    adbcommand().adb_shell().shell_wm_density(func='reset')
                    parseinput(1)
                    return
                if inputtext=='':
                    adbcommand().adb_shell().shell_wm_density()
                    parseinput(1)
                    return
                adbcommand().adb_shell().shell_wm_density(func=inputtext)
                parseinput(1)
                return
        if inputtext=='':
            parseinput(1)
            return
        if inputtext=='applist':
            args_=input('附加的参数>>>')
            args_=args_.replace(" ", "")
            if args_=='':
                adbcommand().adb_shell().shell_pm_list_package()
                parseinput(1)
                return
            adbcommand().adb_shell().shell_pm_list_package(args_)
            parseinput(1)
            return
        if inputtext=='clear':
            Package=input('欲清除数据的程序包名(使用applist查看)>>>')
            Package=Package.replace(" ", "")
            if Package=='':
                errexit(4)
                parseinput(1)
                return
            adbcommand().adb_shell().shell_pm_clear(Package)
            parseinput(1)
            return
        if inputtext=='enable':
            Package=input('欲启用的程序包名(使用applist查看)>>>')
            Package=Package.replace(" ", "")
            if Package=='':
                errexit(4)
                parseinput(1)
                return
            adbcommand().adb_shell().shell_pm_enable(Package)
            parseinput(1)
            return
        if inputtext=='disable':
            Package=input('欲禁用的程序包名(使用applist查看)>>>')
            Package=Package.replace(" ", "")
            if Package=='':
                errexit(4)
                parseinput(1)
                return
            adbcommand().adb_shell().shell_pm_disable_user(Package)
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
            adbcommand().adb_shell().shell_cmd_compile(method=mode,func=func,pkg=pkg)
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
                adbcommand().uninstall(apkfile)
                parseinput(1)
                return
            adbcommand().uninstall(apkfile,args_)
        if inputtext=='install':
            apkfile=input('欲安装的apk文件>>>')
            args_=input('欲附加的参数>>>')
            if apkfile=='':
                errexit(4)
                parseinput(1)
                return
            elif args_=='':
                adbcommand().install(apkfile=apkfile)
                parseinput(1)
                return
            adbcommand().install(apkfile,args_)
            parseinput(1)
            return
        if inputtext=='download':
            adbcommand().reboot(mode=5)
            parseinput(1)
            return
        if inputtext=='sideload':
            adbcommand().reboot(mode=4)
            parseinput(1)
            return
        if inputtext=='bl':
            adbcommand().reboot(mode=2)
            parseinput(1)
            return
        if inputtext=='rec':
            adbcommand().reboot(mode=3)
            parseinput(1)
            return
        if inputtext=='shutdown':
            adbcommand().reboot(mode=1)
            parseinput(1)
            return
        if inputtext=='reboot':#0 不带参数 1.-p 2.fastboot(bl) 3.recovery 4.sideload 5.挖煤
            adbcommand().reboot()
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
            adbcommand().devices()
            parseinput(1)
            return
        if inputtext=='kill_server':
            adbcommand().kill_server()
            parseinput(1)
            return
        if inputtext=='start_server':
            adbcommand().start_server()
            parseinput(1)
            return
        if inputtext=='root':
            adbcommand().root()
            parseinput(1)
            return
        if inputtext=='shell':
            adbcommand().shell()
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
        adbcommand().kill_server()
        errexit(2)
        sys.exit(0)
    if inputtext =='environment':
        print('Version:'+version+' BuildDate:'+builddate+' Platform:'+p+' UpdateAddress:'+github+' AdbBin:'+adbfile)
        parseinput(a)
        return
    print('W :未知指令')
    parseinput(a)
    return
    