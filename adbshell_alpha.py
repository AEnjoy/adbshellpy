#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys , os , platform , getopt , shutil , datetime
import zipfile as zip
try:
    import configparser
except:pass
try:
    import urllib.request 
except: pass

try:
    import adbshellpy_home
    import adbshellpy_libhelper
except:
    update().download_lib('adbshellpy_home')
    update().download_lib('adbshellpy_libhelper')
    import adbshellpy_home
    import adbshellpy_libhelper

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
version='0.6alpha'
builddate='2020-3-30 00:09:41'
run=0
p=platform.system()
checkflag=True
branch='dev'
qqgroup='https://jq.qq.com/?_wv=1027&k=5C85bvp' 
github='https://github.com/AEnjoy/adbshellpy/'#updateURL
uselinuxpkgmanagertoinstalladb='enable'
adbfile=str(os.environ.get('adbfile'))
changes='''
0.5.2Beta→0.5.3Beta 2020-4-14 20:57:52
1.应用程序编译默认不载带-f参数

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
        def shell_cmd_compile(self,method='-m speed',func=' ',pkg='-a'):
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
class update():
    global builddate,version,branch,qqgroup,github
    ver=version
    bra=branch
    vdate=builddate
    def isnewversionavailable(self,b=''):
        url='https://github.com/AEnjoy/adbshellpy/raw/'+self.bra+'/version'
        try:
            urllib.request.urlretrieve(url,'version.txt')
        except:
            print('网络错误!')
            return True
        f=open('version.txt')
        if f.read()==self.ver:
            f.close()
            os.remove('version.txt')
            return False
        else: 
            f.close()
            os.remove('version.txt')
            return True
    def updatecheck(self):
        if self.isnewversionavailable():
            a=input('您当前使用的adbshellpy存在新版本,是否更新?y/n')
            return
        else:
            print('您当前使用的adbshellpy为最新版本,无需更新.')
            return
    def download_lib(self,libname): #No .py 后缀
        url='https://github.com/AEnjoy/adbshellpy/raw/'+self.bra+'/'+libname+'.py'
        try:
            urllib.request.urlretrieve(url,libname+'.py')
        except:
            print('Library :'+libname+' 加载失败!')
            return 1
        return 0
    def download_update(self):
        if self.bra=='master':
            self.download_lib('adbshell')
        if self.bra=='dev':
            self.download_lib('adbshell_alpha')
        print('Done')
    def qqgroupopen(self):
        import webbrowser
        webbrowser.open(qqgroup)
    def githubopen(self):
        import webbrowser
        webbrowser.open(github)
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
    adbshellpy_home.parseinput(1)

def setmode():#setmode parseinput(2)
    print('''
    **********************************Setmode*****************************************
    *setting(default,Enter) 设置参数 cls 清屏 back 回到上一菜单 exit 退出            *
    *您也可以通过手动编辑adbshell.ini来修改设置                                      *
    **********************************Setmode*****************************************
    ''')
    adbshellpy_home.parseinput(2)

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