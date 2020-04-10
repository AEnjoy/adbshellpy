#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys , os , platform , getopt , shutil , datetime
import zipfile as zip
try:
    import configparser
except:
    pass
try:
    import urllib.request 
except:
    pass
def errexit(arg): #异常信息
    if arg == 0:#OS I/O Error
        adbcommand().kill_server()
        print('文件夹创建失败!')
        a=input('按 ENTER 退出...')
        sys.exit(1)
    if arg == 1:#系统不受支持
        print('仅支持Linux Windows 暂未添加其它平台功能支持')
        a=input('按 ENTER 退出...')
        sys.exit(1)
    if arg == 2:#常规信息
        a=input('按 ENTER 继续或退出...')
        #sys.exit(0)
    if arg == 3 :#Python版本低
        #adbcommand().kill_server()
        print("Built by Python 3.6, requires Python 3.6 or later")
        a=input('Press ENTER to exit...')
        sys.exit(1)
    if arg== 4:
        print('请输入有效数据!')
        a=input('按 ENTER 继续')
if sys.hexversion < 0x03060000:
    errexit(3)
#else

#默认设置BEGIN 可在adbshell.ini adbshell.py修改默认选项
version='0.5.2Beta'
builddate='2020-4-10 23:06:45'
run=0
p=platform.system()
checkflag=True
branch='beta'
qqgroup='https://jq.qq.com/?_wv=1027&k=5C85bvp' 
github='https://github.com/AEnjoy/adbshellpy/'#updateURL
uselinuxpkgmanagertoinstalladb='enable'
adbfile=str(os.environ.get('adbfile'))
changes='''
0.5.1Beta→0.5.2Beta 2020-4-10 23:06:45
1.添加功能:黑域,shizuku 激活

0.5Beta→0.5.1Beta   2020-3-29 15:46:54
1.修复了强制检测adb是否安装的bug
2.优化了部分输出内容
3.adb在下载前将会进行网络连通检测
4.默认直接进入主界面
5.添加了程序版本分支标记

0.4.2Beta→0.5Beta   2020-3-18 23:36:49
1.Bug修复
2.功能可用:pull/push
3.更新了QQ群加群链接
4.ReleaseToGitHub

0.4.1Beta→0.4.2Beta 2020-3-17 23:27:06
1.Bug修复
2.compile指令支持显示执行用时

0.4Beta→0.4.1Beta  2020-3-15 23:55:09 
1.使用exit退出时将自动清理adb服务
2.优化了help显示
3.命令行功能将暂不可用
4.更新链接替换至QQ群
5.支持显示changes
6.SET视图可用
7.UI部分优化(By:莫白)
8.screencap屏幕截图功能可用

0.3Alpha→0.4Beta   2020-3-13 00:25:33
1.帮助help更新
2.功能可用:dumpsys
3.修复了文件夹重命名失败导致安装失败的bug(玄学,修到一半自己好了TAT浪费感情(估计是权限问题),不过还是添加了相关代码)
4.修复了一处崩溃

0.2Alpha→0.3Alpha 2020年3月11日23:29:11
1.修复了一些导致崩溃的bug
2.帮助help更新
3.功能可用:settings

0.1Alpha→0.2Alpha 2020-3-11 
1.修复了一些导致崩溃的bug
2.修复了一些无关紧要的bug
3.功能可用:windowmode  input

0.1Alpha----
程序发布
'''
if os.path.exists('adbshell.ini') ==False:
    conf = configparser.ConfigParser()
    conf.add_section('adbshell')
    conf.set('adbshell', 'platform', p)
    conf.set('adbshell', 'adbfile', adbfile)
    conf.set('adbshell', 'checkflag', str(checkflag))
    conf.set('adbshell', 'uselinuxpkgmanagertoinstalladb', uselinuxpkgmanagertoinstalladb)
    with open('adbshell.ini', 'w') as ini:
        conf.write(ini)
else:
    conf = configparser.ConfigParser()
    conf.read('adbshell.ini')
    #getboolean
    try:
        checkflag=conf.getboolean('adbshell','checkflag')
    except:
        #旧版本升级上来
        conf.set('adbshell', 'checkflag', str(checkflag))
        with open('adbshell.ini', 'w') as ini:
            conf.write(ini)
    uselinuxpkgmanagertoinstalladb=conf.get('adbshell', 'uselinuxpkgmanagertoinstalladb')
    adbfile=conf.get('adbshell', 'adbfile')

#默认设置END
#function 
class adbcommand:
    hel=''
    '''def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    '''
    def _adbc(self,command):
        os.system(adbfile+' '+command)
    def start_server(self):
        adbcommand()._adbc('start-server')
    def kill_server(self):
        adbcommand()._adbc('kill-server')
    def devices(self): # 后续将会添加取设备ID功能
        adbcommand()._adbc('devices')
    def printdevices(self,name=''):
        adbcommand()._adbc('-s '+name)

    #netmode
    def tcpip(self):
        adbcommand()._adbc('tcpip 5555')
    def connect(self,ip): #ip local ip
        adbcommand()._adbc('connect '+ip+':5555')
    def disconnect(self,ip):
        adbcommand()._adbc('disconnect '+ip+':5555')
    def usb(self):#默认usb模式
        adbcommand()._adbc('usb')

    #netmode end
    def root(self):
        adbcommand()._adbc('root')
    def reboot(self,mode=0):#0 不带参数 1.-p 2.fastboot(bl) 3.recovery 4.sideload 5.挖煤
        if mode == 0:
            adbcommand()._adbc('reboot')
        if mode == 1:
            adbcommand()._adbc('reboot -p')
        if mode == 2:
            adbcommand()._adbc('reboot bootloader')
        if mode == 3:
            adbcommand()._adbc('reboot recovery')
        if mode == 4:
            adbcommand()._adbc('reboot sideload')
        if mode == 5:
           adbcommand(). _adbc('reboot download')

    def install(self,apkfile,command='-g -d'):
        adbcommand()._adbc("install "+command+" "+'"'+apkfile+'"')
    def uninstall(self,packname,command=''):
        adbcommand()._adbc('unistall ' +packname +' '+command)

    def shell(self,command=''):#_class adb_shell():
        adbcommand()._adbc('shell '+command)

    class adb_shell():
        def shell_cmd(self,func=''):
            adbcommand().shell('cmd '+func)
        def shell_cmd_compile(self,method='-m speed',func='-f',pkg='-a'):
            adbcommand().adb_shell().shell_cmd('package compile '+method+' '+func+' '+pkg)
        def shell_pm(self,func=''):
            adbcommand().shell('pm '+func)
        def shell_pm_disable_user(self,pkg):
            adbcommand().adb_shell().shell_pm('disable-user '+pkg)
        def shell_pm_enable(self,pkg):
            adbcommand().adb_shell().shell_pm('enable '+pkg)
        def shell_pm_install(self,urlp):
            adbcommand().adb_shell().shell_pm('install '+urlp)
        def shell_pm_uninstall(self,pkg,func=''):#--user 0 可隐藏系统app
            adbcommand().adb_shell().shell_pm('uninstall '+pkg+' '+func)
        def shell_pm_clear(self,pkg):
            adbcommand().adb_shell().shell_pm('clear  '+pkg)
        def shell_pm_list_package(self,func='-i'):#-f -d -e -s -3 -i -u
            adbcommand().adb_shell().shell_pm('list package '+func)
        def shell_wm(self,func=''):#私有
            adbcommand().shell('wm '+func)
        def shell_wm_density(self,func=''):#'' 列出当前显示的DPI。 'xxx'设置dpi为xxx 'reset'恢复默认dpi
            adbcommand().adb_shell().shell_wm('density '+func)
        def shell_wm_size(self,func=''):#''列出当前显示的分辨率。 'axb'设置分辨率，注意手机的格式为“横向x纵向” 'reset'恢复默认
            adbcommand().adb_shell().shell_wm('size '+func)
        def shell_wm_overscan(self,a,b,c,d):
            adbcommand().adb_shell().shell_wm('overscan '+ a + ',' + b + ',' + ',' + c + ',' + d)#adb shell wm overscan a,b,c,d
        def shell_input(self,func=''):
            adbcommand().shell('input '+func)
        def shell_input_text(self,func):
            adbcommand().adb_shell().shell_input("text "+func)#向设备输入xxx字符(不支持中文
        def shell_input_keyevent(self,func=''):
            adbcommand().adb_shell().shell_input('keyevent '+func)
        def shell_input_tap(self,x,y):
            adbcommand().adb_shell().shell_input('tap '+x+' '+y)
        def shell_input_swipe(self,x1,y1,x2,y2,d):
            adbcommand().adb_shell().shell_input('swipe '+x1+' '+y1+' '+x2+' '+y2+' '+d)
        def shell_setting(self,func=''):#adb shell settings help
            adbcommand().shell('settings '+func)
        def shell_dumpsys(self,func=''):
            adbcommand().shell('dumpsys '+func)
        def shell_dumpsys_battery(self,func=''):
            adbcommand().adb_shell().shell_dumpsys('battery '+func)
            hel_='''
            func值
            空:列出电池状态 set level x:修改电池百分比为x reset:恢复真实百分比
            '''
            hel=hel_
    def push(self,urlc,urlp='/sdcard/'):
        adbcommand()._adbc("push "+'"'+urlc+'" "'+urlp+'"')
    def pull(self,urlp,urlc):
        adbcommand()._adbc("pull "+'"'+urlp+'" "'+urlc+'"')

def checkinternet():
    exit_code = os.system('ping www.baidu.com')
    if exit_code:
        return False
    else:
        return True
def clear():
    if p == "Windows":
        os.system('cls')
    if p == "Linux":
        os.system('clear')

def parseinput(a=1):#0 一级目录 1二级目录(adbmode) 2二级目录(othermode)
    inputtext=input('>>>')
    inputtext=inputtext.replace(" ", "")
    global run , p ,github,adbfile , conf ,changes
    if a==0: #1级目录 已弃用
        pass
    if a==1:#2级目录(adbmode)
        if inputtext == '':
            parseinput(1)
            return
        if inputtext == 'adbmode': #已弃用
            adbmode()
            return
        if inputtext == 'help':
            usage()
            Console()
            return
        if inputtext == 'back':
            print('E:您已处于主菜单!')
            parseinput(1)
            return
        if inputtext == 're-install':
            #重新安装
            install(p,2)
            run=0
            Console()
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
                    adbcommand().adb_shell().shell_wm_overscan(func='reset')
                    parseinput(1)
                    return
                if inputtext=='':
                    adbcommand().adb_shell().shell_wm_overscan()
                    parseinput(1)
                    return
                adbcommand().adb_shell().shell_wm_overscan(func=inputtext)
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
            func=input('编译参数[默认-f]>>>')
            pkg=input("编译对象[默认-a]>>>")
            func, pkg = func, pkg . replace(" ", "")
            if mode=='':
                mode='-m speed'
            if func =='':
                func='-f'
            if pkg=='':
                pkg='-a'
            '''
            if mode=='':#func pkg
                if func=='':#pkg
                    if pkg=='':
                        adbcommand().adb_shell().shell_cmd_compile()
                        parseinput(1)
                        return
                    #onlly pkg
                    adbcommand().adb_shell().shell_cmd_compile(pkg=pkg)
                    parseinput(1)
                    return
                if pkg=='':
                    if func=='':
                        adbcommand().adb_shell().shell_cmd_compile()
                        parseinput(1)
                        return
                    adbcommand().adb_shell().shell_cmd_compile(func=func)
                    parseinput(1)
                    return
                adbcommand().adb_shell().shell_cmd_compile(func=func,pkg=pkg)
                parseinput(1)
                return
            elif func=='':
                if pkg=='':
                    adbcommand().adb_shell().shell_cmd_compile(method=mode)
                    parseinput(1)
                    return
                adbcommand().adb_shell().shell_cmd_compile(pkg=pkg)
                parseinput(1)
                return
            else:
                adbcommand().adb_shell().shell_cmd_compile(mode,func,pkg)
                parseinput(1)
                return
            '''
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
            print('''>表示此指令内还有其它页面 √表示默认启用
            ****************************ADBSystemTOOLBOXHELP**********************************
            help:显示此帮助 
            back:回到上一级页面 
            cls:清屏 
            set:设置 
            exit:退出工具 
            shell:启动shell内置提示符(需要连接设备) 
            start_server:启动ADB服务 
            kill_server:关闭设备服务 
            devices:列出设备  
            tcpipconnect:使用网络模式设置并连接 
            usb:使用usb连接模式 reboot:重启手机
            shutdown:关闭手机(某些手机此命令可能无效) 
            recovery:将手机重启至recovery恢复模式(某些手机可能会直接触发清除数据,恢复出厂设置操作) 
            sideload:重启至侧刷sideload模式 
            download:三星手机重启至挖煤模式
            bl:重启手机至fastboot线刷模式(部分机型可能无法进入该模式)
            edl:进入高通9008下载模式(部分机型可能无法进入该模式)
            install:应用安装命令集 
            uninstall:应用卸载命令集 
            compile:编译系统,优化系统/应用运行速度
            disable:禁用app 
            enable:启用app 
            clear:清除应用数据 
            applist:列出应用 
            windowmode:分辨率,DPI,屏幕边角等设置 
            input:模拟输入/触屏/按按键等 
            settings:系统高级设置命令集 <ADB玩机精髓>
            dumpsys:系统监控指令集
            screencap:手机截屏
            push:从本地中复制一个文件(夹)至手机
            pull:从手机中拉取一个文件(夹)至本地
            ****************************ADBSystemTOOLBOXHELP**********************************
            输入欲查询的指令(仅>的受支持)或back,Enter返回:''')
            inputtext=input('>>>')
            inputtext=inputtext.replace(" ", "")
            #screencap
            if inputtext=='push':
                print('''push:从本地中复制一个文件(夹)至手机
                远端路径>>>[/sdcard/]手机端的文件或文件夹可空,默认为/sdcard
                本地文件或文件夹>>>本地文件或文件夹所在路径
                    ''')
                parseinput(1)
                return
            if inputtext=='pull':
                print('''pull:从手机中拉取一个文件(夹)至本地
                远端路径>>>手机端的文件
                本地路径>>>[local]可空,默认为脚本执行路径
                    ''')
                parseinput(1)
                return
            if inputtext=='screencap':
                print('''screencap:对手机执行截屏命令,并可选择是否传输至电脑并立即查看
                传输至电脑并打开查看>>>[Y/N 默认N]
                ...LINUX查看?需要提前安装display>>>[Y/N 默认N]
                    ''')
                parseinput(1)
                return
            if inputtext=='dumpsys':
                print('''dumpsys:获取或设置一些调试信息(转储所有服务)。
                dumpsys>>>[-t TIMEOUT] [--priority LEVEL] [--help | -l | --skip SERVICES | SERVICE [ARGS]]
                --help：显示此帮助
                -l：仅列出服务，不转储它们
                -t TIMEOUT_SEC：设置超时(单位s,默认10)
                -T TIMEOUT_MS:  设置超时(单位ms,默认10)
                --proto：筛选器服务，支持以proto格式转储数据。 转储将采用原始格式。
                --priority LEVEL：根据指定的优先级过滤服务 LEVEL：CRITICAL | HIGH | NORMAL
                --skip SERVICES：转储除SERVICES（逗号分隔列表）以外的所有服务
                SERVICE [ARGS]：仅转储服务SERVICE，可以赋予参数ARGS
                SERVICE支持获取以下信息(后续会根据更新): 后面可带-h查看详细帮助,set 设置指定内容
                (中文标记部分常用选项)
                DmAgent
                DockObserver
                GuiExtService
                IIccPhoneBookMz
                NvRAMAgent
                PPLAgent
                SurfaceFlinger
                access_control
                accessibility
                account
                activity       查看当前与用户交互的activity
                alarm          唤醒的应用信息
                alphame_server 唤醒的应用服务信息
                android.security.keystore
                anrmanager
                appops        应用权限信息
                appwidget
                audio         获取媒体音频等信息
                backup        
                battery       获取当前电池信息
                batteryproperties
                batterystats  获取电池stats
                bluetooth_manager获取蓝牙信息
                clipboard
                commontime_management
                connectivity
                consumer_ir
                content
                country_detector
                cpuinfo        获取手机CPU信息
                dbinfo
                device_control
                device_policy
                device_states
                devicestoragemonitor
                diskstats     获取手机Disk信息
                display       获取手机显示屏信息
                dreams
                drm.drmManager
                dropbox
                entropy
                fingerprint   获取手机指纹信息
                fingerprints_service
                gesture_manager
                gfxinfo       获取手机GPU图形信息
                hardware      获取手机硬件信息
                hips_service
                imms          获取手机imms信息(高版本Android无效)
                input         获取手机输入信息
                input_method  获取手机输入方式
                iphonesubinfo
                isms
                isub
                jobscheduler
                launcherapps  获取手机启动器(桌面)信息
                location      获取手机定位信息
                lock_settings 读取手机锁定设置
                media.audio_flinger
                media.audio_policy
                media.camera  读取手机相机信息
                media.mmsdk
                media.player
                media.sound_trigger_hw
                media_projection
                media_router
                media_session
                meminfo       获取手机运存信息
                memory_dumper
                mobile
                mount
                move_window
                mtk-perfservice
                mtk.codecservice
                netpolicy     获取当前网络策略
                netstats      获取当前网络信息
                network_management
                network_score
                networkmanagement_service_flyme
                notification  获取当前手机通知信息
                package       获取手机应用程序包信息
                permission    获取手机权限信息
                phone
                phoneEx
                phone_ext
                power         获取手机电源信息
                pppoe
                print
                procstats
                program_binary
                recovery
                restrictions
                rttmanager
                samba_client
                samba_server
                samplingprofiler
                scheduling_policy
                search       
                search_engine获取手机搜索引擎
                sensorservice
                serial
                servicediscovery
                simphonebook
                sip
                statusbar
                telecom
                telephony.registry
                textservices
                trust
                uimode
                updatelock
                usagestats
                usb         获取手机USB信息
                user        获取手机用户信息
                vibrator
                voiceinteraction
                wallpaper   获取手机壁纸相关信息
                webviewupdate
                wifi        获取WiFi信息
                wifip2p
                wifiscanner
                window
                ''')
                parseinput(1)
                return
            if inputtext=='settings':
                print('''settings:通过adb设置系统选项
                通过ADB读取/更改系统设置
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
                eg:注意:部分机型可能没效果
                get 获取信息 put 设置参数 可以互相调用
                get secure default_input_method                             获取系统默认输入法
                put global policy_control immersive.full=*                  全屏沉浸
                put global adb_enabled 0                                    开关USB调试 0关 1开
                put secure install_non_market_apps1                         允许安装位置来源应用
                settings put system screen_brightness 150                   更改亮度值为150（亮度值在0—255之间）
                get system screen_brightness                                获取当前亮度值
                get secure enabled_accessibility_services                   获取当前服务
                get global auto_time                                        是否自动刷新时间(0/1)
                get secure android_id                                       获取android设备id
                get system screen_off_timeout                               获取屏幕休眠时间(单位ms)
                put system screen_off_timeout 600000                        设置屏幕休眠时间(单位ms)
                get system screen_brightness_mode                           获取亮度是否为自动获取
                put global window_animation_scale 1.25                      修改窗口动画速度为1.25
                put global transition_animation_scale 1.32                  修改过渡动画速度为 1.32
                put global animator_duration_scale 1.55                     修改程序动画速度为 1.55
                put system font_scale 1.02                                  修改全局字体缩放为1.02，1为默认
                put global policy_control immersive.status=*                隐藏状态栏，上滑可出
                put global policy_control immersive.navigation=*            隐藏导航栏，上滑可出
                put secure icon_blacklist rotate，volume                    隐藏状态栏的旋转和音量图标。
                See:https://forum.xda-developers.com/huawei-p20-pro/how-to/guide-hiding-status-bar-icons-t3853258
                put secure sysui_qqs_count 8                                修改状态栏一级下拉图标数量为8个
                put secure sysui_rounded_content_padding 2                  修改状态栏两侧的置顶间距位2(仅限
                Pie及以上系统使用，非圆角屏建议调成0)
                put global captive_portal_https_url See:http://connect.rom.miui.com/generate_204
                更多settings指令可使用adb shell settings查看，充分利用help命令，包括打印系统自带的system,
                secure, global列表，学会了settings才算真正的掌握了ADB玩机的精髓。以上命令想恢复默认只需删
                掉最后的参数
                更多设置选项可以百度或Google获取
                ''')
                parseinput(1)
                return
            if inputtext=='applist':
                print('''applist:
                附加的参数>>>[<arg[s]>]
                -f列出apk的安装位置与对应包名 
                -d列出禁用的包名，仅限系统应用 
                -e列出启用的包名，仅限系统应用 
                -s列出所有系统应用包名
                -3列出第三方应用包名
                -i列出软件对应的安装来源的包名 
                -u 列出被卸载过的软件的包名
                ''')
                parseinput(1)
                return
            if inputtext=='input':
                print('''input:
                command:(Only Enter To Return)
                input_text:    向手机输入一串字符(不支持中文)
                input_keyevent:模拟输入内容(在adbshell→help→input中可查询指令)
                input_tap:     模拟点击屏幕上的一个像素点
                input_swipe:   模拟滑动屏幕(从一个像素点到另一像素点)
                ...Text>>><text>欲向系统发送的文本
                ...Keyevent>>><x>欲向系统发送的指令
                ...X>>>&...Y>>><FOR> 欲点击的手机屏幕位置
                ...X1>>>&...Y1>>>&...X2>>>&...Y2>>>[&...D>>>]欲从x1,y1滑动到x2,y2
                Keyevent>>><x>值
                x代表keycode。左边的数字就是keycode，这里只列举一些常用的，完整版的可以自己查。
                3.Home 4.Return 5.PhoneApp 6.turn off Phone 24 vol+ 25 vol- 26.powerbutton 27.photo
                64.Browser 82.Menu 85.pause/continue 86.StopMusic 87.NextMusic 88.PreviousMusic 122.Move
                MouseToTOL/LOT 133.MoveMouseToEOL/EOC 164.Mute 176.SettingApp 187.SwitchAPP 207.OpenContacts
                208.OpenCalendar 209.OpenMusicAPP 210.OpenCalculatorAPP 220.ReduceScreenBrightness
                221.With220.OnTheContrary 223.SystemDormancy 224.LightUpTheScreen 231.OpenVoiceAssistant
                SeeCSDN:https://blog.csdn.net/chen825919148/article/details/18732041                
                    ''')
                parseinput(1)
                return
            if inputtext=='back':
                parseinput(1)
                return
            if inputtext=='install':
                print('''install:
                欲安装的apk文件>>><apkfile>  欲安装的apk文件路径(支持绝对路径,本地路径)
                欲附加的参数>>>[<args>default=-d -g] -l锁定应用程序 -t允许测试包 -d允许降级覆盖安装 -p部分应用安装  -g为应用程序授予所有运行时的权限 所有指令之间保留空格
                    ''')
                errexit(2)
                parseinput(1)
                return
            if inputtext=='uninstall':
                print('''unistall:
                欲移除的程序包名(使用applist查看)>>><Package>
                欲附加的参数>>>[<args>] -k 保留应用数据
                ''')
                errexit(2)
                parseinput(1)
                return
            if inputtext=='compile':
                print('''compile:AndroidART运行时编译,通过编译应用以提升应用执行时的性能
                compile [-m MODE | -r REASON] [-f] [-c] [--split SPLIT_NAME]
                [--reset] [--check-prof (true | false)] (-a | TARGET-PACKAGE)
                Trigger compilation of TARGET-PACKAGE or all packages if "-a".  Options are:
                -a: compile all packages 编译所有程序包
                -c: clear profile data before compiling 在编译前清理配置文件
                -f: force compilation even if not needed 强制编译甚至不需要的程序
                -m: select compilation mode 选择编译模块
                MODE is one of the dex2oat compiler filters: 模块
                assume-verified
                extract
                verify
                quicken
                space-profile
                space
                speed-profile
                speed
                everything
                -r: select compilation reason 选择编译对象
                REASON is one of:
                first-boot
                boot
                install
                bg-dexopt
                ab-ota
                inactive
                shared
                --reset: restore package to its post-install state 重置编译
                --check-prof (true | false): look at profiles when doing dexopt?在进行dexopt时查看配置文件
                --secondary-dex: compile app secondary dex files编译应用程序辅助dex文件
                --split SPLIT: compile only the given split name
                See:https://source.android.google.cn/devices/tech/dalvik/jit-compiler
                编译模式>>>[<mode>default=-m speed or --reset]-m mode:算法,支持assume-verified,extract,verify,quicken,space-profile,space,speed-profile,speed,everything模式,-r REASON:编译的对象,支持first-boot,boot,install,bg-dexopt,ab-ota,inactive,shared
                编译参数>>>[<func>default=-f] -f强制编译甚至是不需要的程序 --check-prof (true | false)在进行dexopt时查看配置文件 --split SPLIT: compile only the given split name
                编译对象>>>[<pkg>default=-a] -a 所有程序包 pkg:指定的一个程序包
                ''')
                errexit(2)
                parseinput(1)
                return
            if inputtext=='disable':
                print('''disable:
                欲禁用的程序包名(使用applist查看)>>><Package>
                ''')
                errexit(2)
                parseinput(1)
                return
            if inputtext=='enable':
                print('''enable:
                欲启用的程序包名(使用applist查看)>>><Package>
                ''')
                errexit(2)
                parseinput(1)
                return
            if inputtext=='clear':
                print('''clear:
                欲清除数据的程序包名(使用applist查看)>>><Package>
                ''')
                errexit(2)
                parseinput(1)
                return
            if inputtext=='windowmode':
                print('''windowmode:
                欲查看或设置的信息>>>[density,size,overscan,reset,default=''(Enter)] density像素密度有关信息,size屏幕分辨率有关信息,overscan屏幕四角信息,reset重置选项
                ...density>>>[density:int,reset,default=''→print_densityInfo]设置像素密度,如果为空则为显示像素密度信息DPI
                ...size>>>[size:axb,reset,default=''→print_sizeInfo]设置屏幕分辨率为axb,如1920x1080,横向x纵向
                ...overscan>>>[a,b,c,d,-d,reset,default=''→print_overscanInfo]
                ......a>>>,......b>>>,......c>>>,......d>>>,......-d>>>[],
                设置、重置屏幕的显示区域。abcd四个参数为整数，分别是显示边缘距左、上、右、下的像素数，正里负外。听不懂没关系，记住它
                有一个很重要的用途就是永久隐藏导航栏，使用命令wm overscan 0,0,0,-d，其中d为导航栏的像素高度。关于wm命令多说一句：就算
                有root了也建议在电脑改以上信息，不会因为手残多输了一位数字让当前界面严重变形，想恢复却找不到输入框。特别是遇到MIUI这种
                默认有最高限制的，root强行改不好就会卡米！
                ''')
                errexit(2)
                parseinput(1)
                return
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
        setmode()
        return
    if inputtext =='exit':
        adbcommand().kill_server()
        errexit(2)
        sys.exit(0)
    if inputtext =='environment':
        print('Version:'+version+' BuildDate:'+builddate+' Run:'+str(run)+' Platform:'+p+' UpdateAddress:'+github+' AdbBin:'+adbfile)
        parseinput(a)
        return
    print('W :未知指令')
    parseinput(a)
    return
    
def adbmode():#adbmode parseinput(1)
    print('''
     _____________________________ADBSystemTOOLBOX____________________________________
    ┃  工具箱指令:  ┃  help>  back   cls  set>   exit                              ┃
    ┃           re-install      update      environment      changes                ┃
     ---------------------------------------------------------------------------------
    ┃  ADB指令集  : ┃ shell   root(√)                                             ┃
    ┃ 设备链接指令: ┃ start_server(√)  kill_server  devices tcpipconnect usb(√)  ┃
    ┃ 设备重启指令: ┃ reboot shutdown rec bl edl sideload download(SamsumgDevices) ┃
    ┃ 应用高级指令: ┃ install> uninstall> compile> disable> enable> clear> applist>┃
    ┃ 文件传输指令: ┃ pull        push                                             ┃
    ┃    System   : ┃ windowmode>  input>  settings>  dumpsys>  screencap>         ┃
    ┃   Activate  : ┃ piebridge(黑域) shizuku                                      ┃
     -------------------------------ADBSystemTOOLBOX----------------------------------
    ''')
    parseinput(1)

def setmode():#setmode parseinput(2)
    print('''
    **********************************Setmode*****************************************
    *setting(default,Enter) 设置参数 cls 清屏 back 回到上一菜单 exit 退出            *
    *您也可以通过手动编辑adbshell.ini来修改设置                                      *
    **********************************Setmode*****************************************
    ''')
    parseinput(2)

def Console():
    clear()
    global run
    if run == 0:
        adbcommand().kill_server()
        adbcommand().devices()
        run=1
    print('''
    **********************************Welcome*****************************************
    *                                ADBSystemTOOLBOX                                *
    *                       基于Python3&GoogleADB的安卓系统工具箱                    *
    *                     Develop:  CoolApkUser:白曦  Github:AEnjoy                  *
    *                           Inspired by CoolApkUser: 晨钟酱                      *
    **********************************Welcome*****************************************
    '''+'Version:'+version +'   buildDate:'+builddate+'\r\n')
    '''print:
    **********************************Console*****************************************
    *command:         输入命令后按Enter继续 直接按Enter进入adb工具箱                 *
    *       adbmode back help re-install cls set update environment changes exit     *
    **********************************Console*****************************************
    '''
    adbmode()
    #parseinput(1)
    #parseinput(0) #默认不再处理0 而是直接进入1处理

class _Options(object):
  help = False
  installcheck = False
  command= None #开发计划3
  apkfile=[] #开发计划2
  apkinstall= False #开发计划2

def usage():
    print("""
    用法:adbshell.py [apkfile(s)] [args or Console -MORE] 
    [apkfile(s)] [开发中]
    安装apk文件至手机 支持多个文件
    [args]
    -nc --ncheck 跳过adb安装检测 
    -h --help help 显示帮助
    [Console][已弃用]
    -adbmode      进入ADBSystemTOOLBOX主界面,内含多种工具
    back         返回至上一级界面[不可用]
    help         console内显示该帮助,console内不支持-h -nc等
    re-install   重新安装adbfiles依赖(升级adbfills)
    cls          清空输出的内容
    set          进入ADBSystemTOOLBOX设置界面
    update       升级ADBSystemTOOLBOX程序,将访问GitHub获取升级
    environment  显示程序运行环境变量的设置及其它信息
    exit         退出程序
    -MORE        程序内部的各种功能
    """)
    errexit(2)

def IsPassInstall():#检测adb安装
    options , args = getopt.getopt(sys.argv[1:], 'nc')
    for name, value in options:
        if name in ('-nc','--ncheck'):
            return True
        else:
            return False

def ParseArguments(args): #解析参数
    cmd = None
    opt = _Options()
    arg = []
    check = None
    if len(args)==0:
        return cmd, opt, arg
    if os.path.exists(args[1]):
        #文件输入 for处理apk文件,加入清单
        opt.apkinstall=True
        for i in range(len(args)):
            if os.path.exists(args[i]):
                opt.apkfile.append(args[i])
            else:
                break
        #apk file End
    for i in range(len(args)):
        a = args[i]
        if a == '-h' or a == '--help':
            opt.help = True
        if a == '-nc'or a == '--ncheck':
            opt.installcheck = False
        elif not a.startswith('-'):
            cmd = a
            arg = args[i + 1:]
            break
    return cmd, opt, arg

def apkinstallmode(install=False):#开发计划2
    if install==True:
        pass

def main(args):
  global checkflag
  cmd, opt, args = ParseArguments(args)
  c=['shutdown','rec','bl','edl','sideload','download','install','uninstall','compile',
      'shell','root','start_server','kill_server','devices','tcpipconnect','usb','reboot',
      'disable','enable','clear','applist','pull','push','windowmode','input','settings',
      'dumpsys','screencap'
     ]#内置命令
  if cmd in c:#开发计划3
      pass
  checkflag=opt.installcheck
  if sys.hexversion < 0x03060000:
      errexit(3)
  if opt.help == True:
      usage()
      sys.exit(0)
  if os.path.exists('adb') == False: #adb文件夹不存在
      install(p)
  '''
  if IsPassInstall()==False: #判断是否跳过adb安装检测(一般用于test,需要脚本目录下有adb文件夹)
      if os.path.exists('adb') == False:
          install(p)
  '''
  conf = configparser.ConfigParser()
  conf.read('adbshell.ini')
  conf.set('adbshell', 'adbfile', adbfile)
  with open('adbshell.ini', 'w') as ini:
      conf.write(ini)
  apkinstallmode(opt.apkinstall)
  if p == "Windows":
      main_windows()
  if p == "Linux":
      main_linux()
  else:
      errexit(1)

def main_linux():
    #install
    Console()#一级菜单
    #二级菜单
    #print('debug')

def main_windows():
    #install
    Console()#一级菜单
    #二级菜单
    #print('debug')

def install(p,check=0):
    global uselinuxpkgmanagertoinstalladb
    global adbfile
    global conf
    global checkflag
    adbcommand().kill_server()
    '''
    try:
        os.rmdir('adb')
        os.rmdir('platform-tools')
    '''
    if check==1 or checkflag==False:
        #Pass Adb Installed Check
        return
    if check==0 and checkflag==True and os.path.exists(adbfile)==True:
        #文件存在
        return

    if check==2:
        pass
    #Internet Check
    if checkinternet()==False:
        print('W:您的网络似乎出现了故障,adb将不会安装.这有可能导致工具箱无法使用,您可能需要手动设置adb文件.')
        return
    #install or re-install
    print('ADB正在安装中:')
    if p == 'Windows':
        url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
        #r = requests.get(url,)
        #with open("adb.zip", "wb") as code:
        #     code.write(r.content)
        urllib.request.urlretrieve(url,'adb.zip') #兼容性强
        z=zip.ZipFile('adb.zip','r')
        z.extractall()
        z.close()
        try:
            os.rename('platform-tools','adb')
        except Exception as errinform:
            print(errinform+'改为默认platform-tools')
            adbfile_=r'platform-tools\adb.exe'
            #conf = configparser.ConfigParser()
            #conf.read('adbshell.ini')
            conf.set('adbshell', 'adbfile', adbfile_)
            with open('adbshell.ini', 'w') as ini:
                conf.write(ini)
            return
            #errexit(0)
        adbfile=r'adb\adb.exe'
        try:
            os.remove('adb.zip')
        except Exception as errinform:
            print(errinform)
    if p == 'Linux':
        if uselinuxpkgmanagertoinstalladb == 'enable':
            print('正在使用系统软件包管理器安装adb,需要请求sudo,若不想使用此请求,输入n,默认y')
            print('Y 使用系统软件包(default,Enter) N 不使用系统软件包管理器')
            inputtext=input('>>>')
            if inputtext=='y' or inputtext=='Y':
                print('Use Linux Pkg Manager To Install Adb files.')
                print('Try:apt-get , pacman or yum')
                os.system('sudo apt-get install -y adb')
                os.system('sudo pacman -s adb')
                os.system('sudo yum install -y adb')
                adbfile='adb'
                #conf = configparser.ConfigParser()
                #conf.read('adbshell.ini')
                conf.set('adbshell', 'adbfile', adbfile)
                with open('adbshell.ini', 'w') as ini:
                    conf.write(ini)
                return
            if inputtext=='n' or inputtext=='N':
                print('Donot Use Linux Pkg Manager To Install Adb files.')
                uselinuxpkgmanagertoinstalladb='disable'
                #conf = configparser.ConfigParser()
                #conf.read('adbshell.ini')
                conf.set('adbshell', 'uselinuxpkgmanagertoinstalladb', uselinuxpkgmanagertoinstalladb)
                with open('adbshell.ini', 'w') as ini:
                    conf.write(ini)
                install(p)
                return
        if platform.machine()=='AMD64':#AMD64 linux x86 or x86_64
            url = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip'
            urllib.request.urlretrieve(url,'adb.zip')
            #r = requests.get(url)
            #with open("adb.zip", "wb") as code:
            #     code.write(r.content)
            z=zip.ZipFile('adb.zip','r')
            z.extractall()
            z.close()
            try:
                os.rename('platform-tools','adb')
            except Exception as errinform:
                print(errinform)
                errexit(0)
            adbfile=r'adb/adb'
            try:
                os.remove('adb.zip')
            except Exception as errinform:
                print(errinform)
            return
        if platform.machine()=='aarch64' or platform.machine()=='aarch':
            url = 'https://github.com/Magisk-Modules-Repo/adb-ndk/archive/master.zip'
            #linux arm or arm64
            #armeabi USE Android NDK
            urllib.request.urlretrieve(url,'adb.zip')
            z=zip.ZipFile('adb.zip','r')
            z.extractall()
            z.close()
            try:
                os.mkdir('adb')
                #os.rename('adb-ndk-master','adb')
                shutil.move('adb-ndk-master/bin','adb')
                os.remove('adb/adb')
                os.rename('adb/adb.bin','adb/adb')
            except Exception as errinform:
                print(errinform)
                errexit(0)
            adbfile=r'adb/adb'
            return
        return
    return
if not adbfile:#adb文件默认设置 默认adb,自动选择platform-tools或adb 可以在环境变量中设置
    #global conf
    #No Bin Files Found
    if p == "Windows":
        if os.path.exists('adb') == False:
            adbfile=r'platform-tools\adb.exe'
        else:
            adbfile=r'adb\adb.exe'
    if p == "Linux":
        if os.path.exists('adb') == False:
            adbfile=r'platform-tools/adb'
        else:
            adbfile=r'adb/adb'
    install(p)
    if p == "Windows":
        adbfile=r'platform-tools\adb.exe'
        conf.set("adbshell", "adbfile", adbfile)
        conf.write(open("adbshell.ini", "w"))
if __name__ == '__main__':
    main(sys.argv[1:])
    #main(sys.argv[0:])