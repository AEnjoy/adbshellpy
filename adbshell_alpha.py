#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshell_alpha.py
#          Core
#       By : 神郭
#  Version : 0.6.2 
import sys , os , platform , getopt , shutil , datetime
import zipfile as zip
if os.path.exists('adbshellpy_home.py') and os.path.exists('adbshellpy_libhelper.py') and os.path.exists('adbshellpy_libapkfile.py') ==False:
    print('''
    Error:Core library files are missing!(Or one of them is missing.)
    The files are :adbshellpy_home.py, adbshellpy_libhelper.py, adbshellpy_libapkfile.py and adbshell.py or adbshell_alpha.py.
    Please reinstall or download adbshllpy,then restart the program.
    Project address:https://github.com/AEnjoy/adbshellpy/
    ''')
    sys.exit(1)
try:import configparser,urllib.request 
except: pass
def errexit(arg): #异常信息
    if arg == 0:#OS I/O Error
        adb.kill_server()
        print('文件夹创建失败!')
        input('按 ENTER 退出...')
        sys.exit(1)
    if arg == 1:#系统不受支持
        print('仅支持Linux Windows 暂未添加其它平台功能支持')
        input('按 ENTER 退出...')
        sys.exit(1)
    if arg == 2:#常规信息
        input('按 ENTER 继续或退出...')
        #sys.exit(0)
    if arg == 3 :#Python版本低
        #adb.kill_server()
        print("Built by Python 3.6, requires Python 3.6 or later")
        input('Press ENTER to exit...')
        sys.exit(1)
    if arg== 4:
        print('请输入有效数据!')
        input('按 ENTER 继续')
    if arg==5:
        print('E:网络出现问题,请检查网络!')
    if arg==6:
        print('E:未找到可用设备!\nadbshellpy可能不会正常工作.')
    if arg==7:
        print('E:仅支持Windows 暂未添加其它平台功能支持')
        input('按 ENTER 继续...')
        
if sys.hexversion < 0x03060000:
    errexit(3)
#else

#默认设置BEGIN 可在adbshell.ini adbshell.py修改默认选项
version='0.6.2'
builddate='2020-8-1 14:50:09'
run=0
p=platform.system()
checkflag=True
branch='dev'
qqgroup='https://jq.qq.com/?_wv=1027&k=5C85bvp' 
github='https://github.com/AEnjoy/adbshellpy/'#updateURL
uselinuxpkgmanagertoinstalladb='enable'
adbfile=str(os.environ.get('adbfile'))
adbinit=0
shellex='enable'#在找不到命令时直接执行adb shell
showserverinfo='enable'

#changes
try:
    f_=open("Changlog", "r",encoding='UTF-8')
    changes=f_.read()
    f_.close()
except:changes='E:更新日志文件"Changlog"不存在,无法查看更新记录!'

if os.path.exists('adbshell.ini') ==False:
    conf = configparser.ConfigParser()
    conf.add_section('adbshell')
    conf.set('adbshell', 'platform', p)
    conf.set('adbshell', 'adbfile', adbfile)
    conf.set('adbshell', 'checkflag', str(checkflag))
    conf.set('adbshell', 'uselinuxpkgmanagertoinstalladb', uselinuxpkgmanagertoinstalladb)
    conf.set('adbshell', 'adbinit', str(adbinit))
    conf.set('adbshell', 'shellex', shellex)
    conf.set('adbshell', 'showserverinfo', showserverinfo)
    with open('adbshell.ini', 'w') as ini:
        conf.write(ini)
else:
    conf = configparser.ConfigParser()
    conf.read('adbshell.ini')
    #旧版本升级上来
    if conf.has_option('adbshell','checkflag')==False:conf.set('adbshell', 'checkflag', str(checkflag))
    if conf.has_option('adbshell','adbinit')==False:conf.set('adbshell', 'adbinit', str(adbinit))
    if conf.has_option('adbshell','shellex')==False:conf.set('adbshell', 'shellex', shellex)
    if conf.has_option('adbshell','showserverinfo')==False:conf.set('adbshell', 'showserverinfo', showserverinfo)
    with open('adbshell.ini', 'w') as ini:
        conf.write(ini)
    uselinuxpkgmanagertoinstalladb=conf.get('adbshell', 'uselinuxpkgmanagertoinstalladb')
    adbfile=conf.get('adbshell', 'adbfile')
#默认设置END
class update():#bra=branch
    global builddate,version,branch,qqgroup,github,p,showserverinfo
    ver=version
    bra='dev'
    vdate=builddate
    def setgitrawhosts(self):
        hosts='199.232.68.133 raw.githubusercontent.com'
        if self.p=='Windows':
            try:f_=open(r'C:\Windows\System32\drivers\etc\hosts','a')
            except:
                print('E:权限不足!')
                return
            f_.write(hosts)
            f_.close()
        if self.p=='Linux':
            try:f_=open('/etc/hosts','a')
            except:
                print('E:权限不足!')
                return
            f_.write(hosts)
            f_.close()            
    def download_update_full(self):
        url='https://hub.fastgit.org/AEnjoy/adbshellpy/archive/master.zip'
        try:
            urllib.request.urlretrieve(url,'master.zip')
        except:
            print('网络错误!')
            return False
        z=zip.ZipFile('master.zip')
        z.extractall()
        z.close()
        try:shutil.copytree('adbshellpy-master',os.getcwd())
        except:pass
        print('完整包升级完成,请重启 adbshellpy实例')
        return True
    def isnewversionavailable(self,b=''):
        url='https://hub.fastgit.org/AEnjoy/adbshellpy/raw/'+self.bra+'/version'
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
            if a=='Y' or a=='y':
                self.download_update()
            return
        else:
            print('您当前使用的adbshellpy为最新版本,无需更新.')
            return
    def download_lib(self,libname): #No .py 后缀
        url='https://hub.fastgit.org/AEnjoy/adbshellpy/raw/'+self.bra+'/'+libname+'.py'
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
    def showinfofromserver(self):
        url='https://hub.fastgit.org/AEnjoy/adbshellpy/raw/'+self.bra+'/info'
        if self.showinfofromserver=='enable':
            try:urllib.request.urlretrieve(url,'info.txt')
            except:
                print('网络错误!')
                return
            f_=open("info.txt", "r",encoding='UTF-8')
            info=f_.read()
            f_.close()
            os.remove("info.txt")
            print(info)

deviceslist=[]
nowdevice=''
i=0
def who():
    '''
    返回另一个设备标识符
    (如果只有一个 则返回一个)
    自动设置:nowdevice
    '''
    global deviceslist ,nowdevice
    adb.devices() #First running,activing service.
    hand=os.popen(adbfile+' devices')
    hand.readline() #第一行需要跳过
    clear()
    if len(deviceslist)==0: #第一次执行/没有设备/添加设备列表
        for b in hand:
            try:
                if 'device' in b:
                    b=b.replace('\tdevice\n','')
                    print('检测到的设备:'+b)
                    deviceslist.append(b)
                if 'recovery' in b:
                    b=b.replace('\trecovery\n','')
                    print('检测到的设备:'+b)
                    deviceslist.append(b)
            except:
                if 'unauthorized' in b:
                    b=b.replace('\tunauthorized\n','')
                    print('W:未授权的设备: %s 找到,请在手机上允许USB调试(一律)'%b)
                    print('跳过该设备: %s '%b)
            if r'\n' in deviceslist:
                deviceslist.pop(deviceslist.index('\n'))
        if len(deviceslist)==0: #没找到设备
            errexit(6)
            print('W:adbshellpy who 可能不会工作!')
            hand.close()
            return ''
        hand.close()
        return deviceslist[0]     
    else: #清单里有设备,不做任何list处理(还要做 如果有新设备添加)
        if nowdevice=='':
            try:
                nowdevice=deviceslist[0]
                return nowdevice
            except:pass #失败?
        #更新设备列表
        deviceslist=[]
        for b in hand:
            try:
                if 'device' in b:
                    b=b.replace('\tdevice\n','')
                    print('检测到的设备:'+b)
                    deviceslist.append(b)
                if 'recovery' in b:
                    b=b.replace('\trecovery\n','')
                    print('检测到的设备:'+b)
                    deviceslist.append(b)
            except:
                if 'unauthorized' in b:
                    b=b.replace('\tunauthorized\n','')
                    print('W:未授权的设备: %s 找到,请在手机上允许USB调试(一律)'%b)
                    print('跳过该设备: %s '%b)
        deviceslist.pop() #√
        if len(deviceslist)==0: #没找到设备
            errexit(6)
            print('W:adbshellpy who 可能不会工作!')
            hand.close()
            return ''
        print('Debug: '+str(deviceslist.index(nowdevice))+' '+str(len(deviceslist)-2)+str(deviceslist))
        if deviceslist.index(nowdevice)==len(deviceslist)-1:#已达到最后一个设备,从新开始 \ n 死活清不掉
            a=deviceslist[0]
        else:
            try:
                a=deviceslist[deviceslist.index(nowdevice)+1]
            except:
                a=deviceslist[deviceslist.index(nowdevice)-1]
        if a in nowdevice:
            print('W:设备标识符一致?')
            return nowdevice
        else:
            hand.close()
            return a
    hand.close()         
    return nowdevice
#function 
class adbcommand():
    global nowdevice
    '''
    adbshellpy Core Code
    '''
    hel=''
    adb=adbfile
    s=nowdevice#设备标识符 多设备时使用
    def _adbc(self,command):#######Core#######
        if self.s=='':
            os.system(adbfile+' '+command)
        else:
            os.system(adbfile+' -s '+self.s+' '+command)
    def __init__(self,device=nowdevice):
        self.s=device
        if self.s=='':
            self.s=nowdevice
    def start_server(self):
        self._adbc('start-server')
    def kill_server(self):
        self._adbc('kill-server')
    def devices(self): # 后续将会添加取设备ID功能
        self._adbc('devices')
    def devices_nodisplay(self):
        os.popen(adbfile+' devices')
    def printdevices(self,name=''):
        self._adbc('-s '+name)
    def set_devices(self,name):#__init__()
        self.s=name
    #netmode
    def tcpip(self):
        self._adbc('tcpip 5555')
    def connect(self,ip): #ip local ip
        self._adbc('connect '+ip+':5555')
    def disconnect(self,ip):
        self._adbc('disconnect '+ip+':5555')
    def usb(self):#默认usb模式
        self._adbc('usb')
    #netmode end
    def root(self):
        self._adbc('root')
    def reboot(self,mode=0):#0 不带参数 1.-p 2.fastboot(bl) 3.recovery 4.sideload 5.挖煤
        if mode == 0:self._adbc('reboot')
        if mode == 1:self._adbc('reboot -p')
        if mode == 2:self._adbc('reboot bootloader')
        if mode == 3:self._adbc('reboot recovery')
        if mode == 4:self._adbc('reboot sideload')
        if mode == 5:self. _adbc('reboot download')
        if mode == 6:self._adbc('reboot edl')

    def install(self,apkfile,command='-g -d'):
        self._adbc("install "+command+" "+'"'+apkfile+'"')
    def uninstall(self,packname,command=''):
        self._adbc('unistall ' +packname +' '+command)

    def shell(self,command='',su=0):#_class adb_shell():
        if su==0:
            self._adbc('shell '+command)
        if su==1:
            self._adbc('shell su -c '+command)
    def busybox(self,command='',su=0):#busybox
        if su==0:
            self.shell('busybox '+command)
        if su==1:
            self.shell('su & busybox '+command)
        
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
        def shell_wm_overscan(self,a='',b='',c='',d=''):
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
            '''
            func值
            空:列出电池状态 set level x:修改电池百分比为x reset:恢复真实百分比
            '''
            adbcommand().adb_shell().shell_dumpsys('battery '+func)
    def push(self,urlc,urlp='/sdcard/'):
        self._adbc("push "+'"'+urlc+'" "'+urlp+'"')
    def pull(self,urlp,urlc):
        self._adbc("pull "+'"'+urlp+'" "'+urlc+'"')

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

def setmode():#setmode parseinput(2)
    print('''
    **********************************Setmode*****************************************
    *setting(default,Enter) 设置参数 cls 清屏 back 回到上一菜单 exit 退出            *
    *您也可以通过手动编辑adbshell.ini来修改设置                                      *
    **********************************Setmode*****************************************
    ''')
    import adbshellpy_home  
    adbshellpy_home.parseinput(2)

def Console():
    global run,adbinit
    if run == 0:
        if adbinit==0:adb.kill_server()#跳过运行时kill adb服务
        who()
        run=1
    import adbshellpy_home      
    update().showinfofromserver()
    adbshellpy_home.home()
    adbshellpy_home.parseinput(1)

class _Options(object):
  help = False
  installcheck = False
  command= None #开发计划3
  apkfile=[] #开发计划2
  apkinstall= False #开发计划2

def usage():
    print("""
    用法:adbshell.py [apkfile(s)] [args or Console] [-MORE] 
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
    [-MORE]        程序内部的各种功能
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
        import adbshellpy_libapkfile
        adbshellpy_libapkfile.mainex(_Options.apkfile)
        
def main(args):
  global checkflag,branch,uselinuxpkgmanagertoinstalladb,adbfile,conf
  try:
    import adbshellpy_libapkfile
    #aapt=adbshellpy_libapkfile.aapt
  except:aapt=''
  cmd, opt, args = ParseArguments(args)
  c=['shutdown','rec','bl','edl','sideload','download','install','uninstall','compile',
      'shell','root','start_server','kill_server','devices','tcpipconnect','usb','reboot',
      'disable','enable','clear','applist','pull','push','windowmode','input','settings',
      'dumpsys','screencap','relatedapk','who','kfmark','icebox','update','changes','piebridge',
      'shizuku'
     ]#内置命令
  if cmd in c:#开发计划3
      adbshellpy_home
      fun=adbshellpy_home.func_()
      if cmd=='shutdown':fun.shutdown()
      if cmd=='kfmark':fun.kfmark()
      if cmd=='rec':fun.rec()
      if cmd=='bl':fun.bl()
      if cmd=='edl':fun.edl()
      if cmd=='sideload':fun.sideload()
      if cmd=='download':fun.download()
      if cmd=='install':fun.install()
      if cmd=='uninstall':fun.uninstall()
      if cmd=='compile':fun.compile()
      if cmd=='shell':fun.shell()
      if cmd=='reboot':fun.reboot()
      if cmd=='disable':fun.disable()
      if cmd=='enable':fun.enable()
      if cmd=='clear':fun.clear()
      if cmd=='applist':fun.applist()
      if cmd=='pull':fun.pull()
      if cmd=='push':fun.push()
      if cmd=='windowmode':fun.windowmode()
      if cmd=='input':fun.input()
      if cmd=='dumpsys':fun.dumpsys()
      if cmd=='screencap':fun.screencap()
      if cmd=='relatedapk':fun.relatedapk()
      if cmd=='icebox':fun.icebox()
      if cmd=='update':fun.update()
      if cmd=='changes':fun.changes_()
      if cmd=='piebridge':fun.piebridge()
      if cmd=='shizuku':fun.shizuku()
      sys.exit(0)
  checkflag=opt.installcheck
  if sys.hexversion < 0x03060000:
      errexit(3)
  if opt.help == True:
      usage()
      sys.exit(0)
  if os.path.exists('adb') == False: #adb文件夹不存在
      install(p)
  conf = configparser.ConfigParser()
  conf.read('adbshell.ini')
  conf.set('adbshell', 'adbfile', adbfile)
  with open('adbshell.ini', 'w') as ini:
      conf.write(ini)
  apkinstallmode(opt.apkinstall)
  #adbshellpy_home.adbshellpyinformation().set_(branch,uselinuxpkgmanagertoinstalladb,aapt,conf)
  if p == "Windows":
      Console()
  if p == "Linux":
      Console()
  else:
      errexit(1)

def install(p,check=0):
    global uselinuxpkgmanagertoinstalladb
    global adbfile
    global conf
    global checkflag
    adb.kill_server()
    if check==2:
        pass
    #Internet Check
    if checkinternet()==False:
        errexit(5)
        print('W:您的网络似乎出现了故障,adb将不会安装.这有可能导致工具箱无法使用,您可能需要手动设置adb文件.')
        return
    #install or re-install
    print('ADB正在安装中:')
    if p=='':
        p=platform.system
    if p == 'Windows':
        url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
        urllib.request.urlretrieve(url,'adb.zip') #兼容性强
        z=zip.ZipFile('adb.zip','r')
        z.extractall()
        z.close()
        try:
            os.rename('platform-tools','adb')
        except Exception as errinform:
            print(errinform+'改为默认platform-tools')
            adbfile_=r'platform-tools\adb.exe'
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
                conf.set('adbshell', 'adbfile', adbfile)
                with open('adbshell.ini', 'w') as ini:
                    conf.write(ini)
                return
            if inputtext=='n' or inputtext=='N':
                print('Donot Use Linux Pkg Manager To Install Adb files.')
                uselinuxpkgmanagertoinstalladb='disable'
                conf.set('adbshell', 'uselinuxpkgmanagertoinstalladb', uselinuxpkgmanagertoinstalladb)
                with open('adbshell.ini', 'w') as ini:
                    conf.write(ini)
                install(p)
                return
        if platform.machine()=='AMD64':#AMD64 linux x86 or x86_64
            url = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip'
            urllib.request.urlretrieve(url,'adb.zip')
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
            url = 'https://hub.fastgit.org/Magisk-Modules-Repo/adb-ndk/archive/master.zip'
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
adb=adbcommand(nowdevice)
if __name__ == '__main__':
    main(sys.argv[1:])