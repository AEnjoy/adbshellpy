#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshell_alpha.py
#        安卓玩机精灵
#          Core
#       By : 神郭
#  Version : 0.7.3(0.7 Alpha 5)
import sys , os , platform , getopt , shutil , datetime ,logging,time
import zipfile as zip
#默认设置BEGIN 可在adbshell.ini adbshell.py修改默认选项
version='0.7 Alpha 5'
builddate='2021-7-1 16:38:43'
run=0
p=platform.system()
checkflag=True
branch='dev'
qqgroup='https://jq.qq.com/?_wv=1027&k=5C85bvp' 
github='https://github.com/AEnjoy/adbshellpy/'#updateURL
uselinuxpkgmanagertoinstalladb='enable'
adbfile=str(os.environ.get('adbfile'))
fastbootfile=str(os.environ.get('fastbootfile'))
adbinit=0
shellex='enable'#在找不到命令时直接执行adb shell
showserverinfo='enable'
language='chn'

if os.path.exists('logs')==False:
    os.mkdir('logs')
logging.basicConfig(filename="logs/"+str(time.time())+'.log', filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
logging.info('Start Time:'+str(datetime.datetime.now()) + ' Python Ver:'+sys.version+' Prefix:'+sys.prefix+' Environment:'+sys.platform+' Version:'+version)
try:import configparser,urllib.request 
except Exception as e:logging.exception("Exception occurred")
if os.path.exists('adbshellpy_home.py') and os.path.exists('adbshellpy_libhelper.py') and os.path.exists('adbshellpy_libapkfile.py') ==False:
    print('''
    Error:Core library files are missing!(Or one of them is missing.)
    The files are :adbshellpy_home.py, adbshellpy_libhelper.py, adbshellpy_libapkfile.py and adbshell.py or adbshell_alpha.py.
    Please reinstall or download adbshllpy,then restart the program.
    Project address:https://github.com/AEnjoy/adbshellpy/
    ''')    
    logging.error('Core library files are missing!(Or one of them is missing.) Abort.')
    input('Press ENTER to exit...')    
    sys.exit(1)

logging.info('Config:')
if os.path.exists('adbshell.ini') ==False:
    logging.info('The first running.')
    logging.info('Write ini.')
    c=1
    if adbfile=='None':
        if p=='Windows':adbfile=r'adb\adb.exe'
        elif p=='Linux':adbfile='adb/adb'
    if fastbootfile=='None':
        if p=='Windows':fastbootfile=r'adb\fastboot.exe'
        elif p=='Linux':fastbootfile='adb/fastboot'          
    conf = configparser.ConfigParser()
    conf.add_section('adbshell')
    conf.set('adbshell', 'platform', p)
    conf.set('adbshell', 'adbfile', adbfile)
    conf.set('adbshell', 'fastbootfile', fastbootfile)
    conf.set('adbshell', 'checkflag', str(checkflag))
    conf.set('adbshell', 'uselinuxpkgmanagertoinstalladb', uselinuxpkgmanagertoinstalladb)
    conf.set('adbshell', 'adbinit', str(adbinit))
    conf.set('adbshell', 'shellex', shellex)
    conf.set('adbshell', 'showserverinfo', showserverinfo)
    conf.set('adbshell', 'language', language)
    with open('adbshell.ini', 'w') as ini:
        conf.write(ini)
else:
    logging.info('READING CONF')
    c=0
    conf = configparser.ConfigParser()
    conf.read('adbshell.ini')
    #旧版本升级上来
    if conf.has_option('adbshell','checkflag')==False:conf.set('adbshell', 'checkflag', str(checkflag))
    if conf.has_option('adbshell','shellex')==False:conf.set('adbshell', 'shellex', shellex)
    if conf.has_option('adbshell','showserverinfo')==False:conf.set('adbshell', 'showserverinfo', showserverinfo)
    if conf.has_option('adbshell','language')==False:conf.set('adbshell', 'language', language)
    if conf.has_option('adbshell','fastbootfile')==False:conf.set('adbshell', 'fastbootfile', fastbootfile)
    if conf.has_option('adbshell','adbinit')==False:conf.set('adbshell', 'adbinit', str(adbinit))    
    with open('adbshell.ini', 'w') as ini:
        conf.write(ini)
    #READ INFO
    uselinuxpkgmanagertoinstalladb=conf.get('adbshell', 'uselinuxpkgmanagertoinstalladb')
    adbfile=conf.get('adbshell', 'adbfile')
    checkflag=conf.get('adbshell','checkflag')
    fastbootfile=conf.get('adbshell', 'fastbootfile')
    shellex=conf.get('adbshell','shellex')
    language=conf.get('adbshell','language')
    showserverinfo=conf.get('adbshell','showserverinfo')
    adbinit=conf.getint('adbshell','adbinit')
    logging.info('uselinuxpkgmanagertoinstalladb:%s checkflag:%s shellex:%s language:%s showserverinfo:%s adbinit:%s fastbootfile:%s'%(uselinuxpkgmanagertoinstalladb,checkflag,shellex,language,showserverinfo,adbinit,fastbootfile))
    logging.info('READING CONF END')
#默认设置END

#language
logging.info('Load language mode...')
if c==1:
    print('Welcome to 安卓玩机精灵(adbshellpy)!Please choose your language.')
    a=input('chn:简体中文 eng:English Language:>>>[chn:default]')
    if a=='chn' or a=='':
        language='chn'
        conf.set('adbshell', 'language', language)
        conf.write(open('adbshell.ini', 'w'))
        from adbshell_language import chn
        Luan=chn()
    if a=='eng':
        language='eng'
        conf.set('adbshell', 'language', language)
        conf.write(open('adbshell.ini', 'w'))
        from adbshell_language import eng
        Luan=eng()
    else:
        print('Your language is not support! Use default.')
        conf.set('adbshell', 'language', language)
        conf.write(open('adbshell.ini', 'w'))
        from adbshell_language import chn
        Luan=chn()
elif c==0:
    if language=='chn':
        from adbshell_language import chn
        Luan=chn()
    if language=='eng':
        from adbshell_language import eng
        Luan=eng()
    else:
        print('Setting language is not support! Use default.')
        from adbshell_language import chn
        Luan=chn()        
logging.info('Load language mode End.')

#changes
try:
    f_=open("Changlog", "r",encoding='UTF-8')
    changes=f_.read()
    f_.close()
except Exception as e:
    logging.exception("Exception occurred")
    changes='E:更新日志文件"Changlog"不存在,无法查看更新记录!'
def errexit(arg): #异常信息
    '''
    0:#OS I/O Error
    1:#系统不受支持
    2:#常规信息
    3:#Python版本低
    4:#数值错误
    5:#网络异常
    6:#没有设备
    7:#仅Windows支持
    '''
    if arg == 0:#OS I/O Error
        adb.kill_server()
        logging.error('MKDIR Error.')
        print(Luan.e1)
        input(Luan.EXIT)
        sys.exit(1)
    if arg == 1:#系统不受支持
        logging.error('System is not supported.')
        print(Luan.e2)
        input(Luan.EXIT)
        sys.exit(1)
    if arg == 2:#常规信息
        logging.warning('Continue.')
        input(Luan.EXIT1)
        #sys.exit(0)
    if arg == 3:#Python版本低
        #adb.kill_server()
        logging.error('Python version is too old.')
        print("Built by Python 3.6, requires Python 3.6 or later")
        input('Press ENTER to exit...')
        sys.exit(1)
    if arg== 4:
        logging.warning('Invalid value.')
        print(Luan.e3)
        input(Luan.EXIT1)
    if arg==5:
        logging.error('Network anomaly.')
        print(Luan.e4)
    if arg==6:
        logging.warning('No available device found.')
        print(Luan.e5)
    if arg==7:
        logging.error('System is not supported.')
        print(Luan.e6)
        input(Luan.EXIT1)
if sys.hexversion < 0x03060000:
    errexit(3)

class update():#bra=branch
    def setgitrawhosts(self):
        logging.info('HOSTS SETTING.')
        hosts='199.232.68.133 raw.githubusercontent.com'
        if self.p=='Windows':
            try:f_=open(r'C:\Windows\System32\drivers\etc\hosts','a')
            except Exception as e:
                logging.error("Not enough permissions.", exc_info=True)
                print(Luan.e8)
                return
            f_.write(hosts)
            f_.close()
        if self.p=='Linux':
            try:f_=open('/etc/hosts','a')
            except Exception as e:
                logging.error("Not enough permissions.", exc_info=True)
                print(Luan.e8)
                return
            f_.write(hosts)
            f_.close()            
        logging.info('HOSTS SETTING END.')
    def download_update_full(self):
        logging.info('Download update.')
        url='https://hub.fastgit.org/AEnjoy/adbshellpy/archive/master.zip'
        try:urllib.request.urlretrieve(url,'master.zip')
        except:
            errexit(5)
            return False
        logging.info('Start upgrade.')
        z=zip.ZipFile('master.zip')
        z.extractall()
        z.close()
        try:shutil.copytree('adbshellpy-master',os.getcwd())
        except:pass
        logging.info('Finish upgrade.')
        print(Luan.i1)
        return True
    def isnewversionavailable(self,b=''):
        logging.info('Update Checke.')
        url='https://raw.fastgit.org/AEnjoy/adbshellpy/'+self.bra+'/version'
        try:urllib.request.urlretrieve(url,'version.txt')
        except:
            errexit(5)
            return True
        logging.info('READ VER FROM SERVER')
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
            logging.info('A update found.')
            a=input(Luan.a1)
            logging.info('Input:'+a)
            if a=='Y' or a=='y':
                self.download_update()
            return
        else:
            logging.info('No Upgrade.')
            print(Luan.i2)
            return
    def download_lib(self,libname): #No .py 后缀
        logging.info('Lib download:'+libname+'.py')
        url='https://raw.fastgit.org/AEnjoy/adbshellpy/'+self.bra+'/'+libname+'.py'
        try:
            urllib.request.urlretrieve(url,libname+'.py')
        except:
            errexit(5)
            print('Library :'+libname+Luan.e9)
            return 1
        logging.info('Lib download:'+libname+'.py END.')
        return 0
    def download_update(self):
        if self.bra=='master':
            self.download_lib('adbshell')
        if self.bra=='dev':
            self.download_lib('adbshell_alpha')
        print('Done')
    def download_lib_shfile(self,names=''):
        logging.info('Lib download:'+names)
        url='https://raw.fastgit.org/AEnjoy/adbshellpy/'+self.bra+'/libshfile/'+names
        if os.path.exists('libshfile'):
            os.chdir('libshfile')
        else:
            os.mkdir('libshfile')
            os.chdir('libshfile')
        try:
            if os.path.exists(names):
                print('LibFile:%s existsed. Pass.'%names)
            else:
                urllib.request.urlretrieve(url,names)
            os.chdir('..')
        except:
            errexit(5)
            print('Library :'+names+Luan.e9)
            return 1        
        print('LibFile:%s downloaded.'%names)        
    def qqgroupopen(self):
        logging.info('OPEN QQ GROUP LINK')
        import webbrowser
        webbrowser.open(qqgroup)
    def githubopen(self):
        logging.info('OPEN GITHUB LINK')
        import webbrowser
        webbrowser.open(github)
    def showinfofromserver(self):
        logging.info('Show info from the server:')
        url='https://hub.fastgit.org/AEnjoy/adbshellpy/raw/'+self.bra+'/info'
        if self.showserverinfo=='enable':
            try:urllib.request.urlretrieve(url,'info.txt')
            except:
                errexit(5)
                return
            f_=open("info.txt", "r",encoding='UTF-8')
            info=f_.read()
            f_.close()
            os.remove("info.txt")
            print(info)
        logging.info('Show info from the server End.')
    def __init__(self):
        global builddate,version,branch,qqgroup,github,p,showserverinfo
        self.vdata=builddate
        self.bra=branch
        self.showserverinfo=showserverinfo
        self.ver=version
deviceslist=[]
nowdevice=''
i=0
def who(mode=0):
    '''
    返回另一个设备标识符
    (如果只有一个 则返回一个)
    自动设置:nowdevice
    mode:[0]:adb [1]:fastboot
    '''
    logging.info('GET DEVICE:')
    global deviceslist ,nowdevice
    if mode==0:
        adb.devices() #First running,activing service.
        hand=os.popen(adbfile+' devices')
        hand.readline() #第一行需要跳过
    elif mode==1:
        adb.devices() #First running,activing service.
        hand=os.popen(adbfile+' devices') 
    clear()
    if len(deviceslist)==0: #第一次执行/没有设备/添加设备列表
        logging.info('First time execution/no device/add device list')
        for b in hand:
            try:
                if 'device' in b:
                    b=b.replace('\tdevice\n','')
                    logging.info('Devices Found:'+b)                    
                    print(Luan.i3+b)
                    print(Luan.i39+Luan.i40)
                    adbcommand(b).shell('getprop ro.product.build.version.release')
                    print(Luan.i41)
                    adbcommand(b).shell('getprop ro.product.build.fingerprint')
                    print(Luan.i42)
                    adbcommand(b).shell('getprop ro.vendor.build.security_patch')
                    print(Luan.i43)
                    adbcommand(b).shell('getprop ro.product.manufacturer')
                    print(Luan.i44)
                    adbcommand(b).shell('getprop ro.product.model')
                    print(Luan.i45)
                    adbcommand(b).shell('getprop ro.crypto.state')
                    deviceslist.append(b)
                    adbcommand(b).shell('getprop >>logs\\'+b+str(time.time())+'.log')
                if 'recovery' in b:
                    b=b.replace('\trecovery\n','')
                    logging.info('Devices Found:'+b)                    
                    print(Luan.i3+b)
                    deviceslist.append(b)
            except:
                if 'unauthorized' in b:
                    b=b.replace('\tunauthorized\n','')
                    logging.info('Devices Found, but Unauthorized :'+b)                    
                    print(Luan.w1%b)
                    print(Luan.i4%b)
            if r'\n' in deviceslist:
                deviceslist.pop(deviceslist.index('\n'))
        if len(deviceslist)==0: #没找到设备
            errexit(6)
            print(Luan.w2)
            logging.warning(Luan.e5)
            hand.close()
            return ''
        hand.close()
        return deviceslist[0]     
    else: #清单里有设备,不做任何list处理(还要做 如果有新设备添加)
        logging.info('Check New Devices')
        if nowdevice=='':
            try:
                nowdevice=deviceslist[0]
                return nowdevice
            except:pass #失败?
        #更新设备列表
        logging.info('Update Devices Lists')
        deviceslist=[]
        for b in hand:
            try:
                if 'device' in b:
                    b=b.replace('\tdevice\n','')
                    logging.info('Devices Found:'+b)
                    print(Luan.i3+b)
                    print(Luan.i39+Luan.i40)
                    adbcommand(b).shell('getprop ro.product.build.version.release')
                    print(Luan.i41)
                    adbcommand(b).shell('getprop ro.product.build.fingerprint')
                    print(Luan.i42)
                    adbcommand(b).shell('getprop ro.vendor.build.security_patch')
                    print(Luan.i43)
                    adbcommand(b).shell('getprop ro.product.manufacturer')
                    print(Luan.i44)
                    adbcommand(b).shell('getprop ro.product.model')
                    print(Luan.i45)
                    adbcommand(b).shell('getprop ro.crypto.state')                    
                    deviceslist.append(b)
                    adbcommand(b).shell('getprop >>logs\\'+b+str(time.time())+'.log')
                if 'recovery' in b:
                    b=b.replace('\trecovery\n','')
                    logging.info('Devices Found:'+b)                   
                    print(Luan.i3+b)
                    deviceslist.append(b)
            except:
                if 'unauthorized' in b:
                    b=b.replace('\tunauthorized\n','')
                    logging.info('Devices Found, but Unauthorized :'+b)                      
                    print(Luan.w1%b)
                    print(Luan.i4%b)
        deviceslist.pop() #√
        if len(deviceslist)==0: #没找到设备
            errexit(6)
            print(Luan.w2)
            hand.close()
            return ''
        logging.debug(str(deviceslist.index(nowdevice))+' '+str(len(deviceslist)-2)+str(deviceslist))
        if deviceslist.index(nowdevice)==len(deviceslist)-1:#已达到最后一个设备,从新开始 \ n 死活清不掉
            a=deviceslist[0]
        else:
            try:
                a=deviceslist[deviceslist.index(nowdevice)+1]
            except:
                a=deviceslist[deviceslist.index(nowdevice)-1]
        if a in nowdevice:
            logging.warning('The device identifier is found to be consistent')
            print(Luan.w3)
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
    fastboot=fastbootfile
    s=nowdevice#设备标识符 多设备时使用
    def _adbc(self,command):#######Core#######
        if self.s=='':
            logging.debug('Command:'+adbfile+' '+command)
            os.system(adbfile+' '+command)
        else:
            logging.debug('Command(With Device):'+adbfile+' -s '+self.s+' '+command)
            os.system(adbfile+' -s '+self.s+' '+command)
        logging.info('Command End.')
    def _fastbootc(self,command):
        if self.s=='':
            logging.debug('Command:'+self.fastboot+' '+command)
            os.system(self.fastboot+' '+command)
        else:
            logging.debug('Command(With Device):'+self.fastboot+' -s '+self.s+' '+command)
            os.system(self.fastboot+' -s '+self.s+' '+command)
        logging.info('Command End.')        
    def __init__(self,device=nowdevice,fastbootflag=0):
        logging.info('Core:Adb file:'+self.adb +' Device:'+device)
        if fastbootflag==0:
            if self.s=='':
                self.s=nowdevice
            if self.adb=='None':
                if os.path.exists(r'adb\adb.exe'):self.adb=r'adb\adb.exe'
                else:logging.debug('Needed restart daemon!')
        elif fastbootflag==1:
            if self.s=='':
                self.s=nowdevice
            if self.fastboot=='None':
                if os.path.exists(r'adb\fastboot.exe'):self.fastboot=r'adb\fastboot.exe'

    def start_server(self):
        logging.info('Core:Start-Server')
        self._adbc('start-server')
    def kill_server(self):
        logging.info('Core:Kill-Server')
        self._adbc('kill-server')
    def devices(self): # 后续将会添加取设备ID功能
        logging.info('Core:Devices')
        self._adbc('devices')
    def devices_nodisplay(self):
        logging.info('Core:Devices')
        os.popen(adbfile+' devices')
    def printdevices(self,name=''):
        self._adbc('-s '+name)
    def set_devices(self,name):#__init__()
        self.s=name
    #netmode
    def tcpip(self):
        logging.info('Core:tcpip')
        self._adbc('tcpip 5555')
    def connect(self,ip): #ip local ip
        logging.info('Core:connect')
        self._adbc('connect '+ip+':5555')
    def disconnect(self,ip):
        logging.info('Core:disconnect')
        self._adbc('disconnect '+ip+':5555')
    def usb(self):#默认usb模式
        self._adbc('usb')
    #netmode end
    def root(self):
        logging.info('Core:Use root')
        self._adbc('root')
    def reboot(self,mode=0):#0 不带参数 1.-p 2.fastboot(bl) 3.recovery 4.sideload 5.挖煤
        logging.info('Core:Reboot Device')
        if mode == 0:self._adbc('reboot')
        if mode == 1:self._adbc('reboot -p')
        if mode == 2:self._adbc('reboot bootloader')
        if mode == 3:self._adbc('reboot recovery')
        if mode == 4:self._adbc('reboot sideload')
        if mode == 5:self. _adbc('reboot download')
        if mode == 6:self._adbc('reboot edl')

    def install(self,apkfile,command='-g -d'):
        logging.info('Core:Install APK File.')
        self._adbc("install "+command+" "+'"'+apkfile+'"')
    def uninstall(self,packname,command=''):
        logging.info('Core:Uninstall apk.')
        self._adbc('unistall ' +packname +' '+command)

    def shell(self,command='',su=0):#_class adb_shell():
        if su==0:
            logging.info('Core:adb shell:')
            self._adbc('shell '+command)
        if su==1:
            logging.info('Core:adb shell(with SU):')
            self._adbc('shell su -c '+command)
    def busybox(self,command='',su=0):#busybox
        if su==0:
            self.shell('busybox '+command)
        if su==1:
            self.shell('su -c busybox '+command)
        
    class adb_shell():
        def shell_cmd(self,func=''):
            logging.info('Core:adb shell cmd')
            adbcommand().shell('cmd '+func)
        def shell_cmd_compile(self,method='-m speed',func=' ',pkg='-a'):
            adbcommand().adb_shell().shell_cmd('package compile '+method+' '+func+' '+pkg)
        def shell_pm(self,func=''):
            logging.info('Core:adb shell pm')
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
            logging.info('Core:adb shell wm')
            adbcommand().shell('wm '+func)
        def shell_wm_density(self,func=''):#'' 列出当前显示的DPI。 'xxx'设置dpi为xxx 'reset'恢复默认dpi
            adbcommand().adb_shell().shell_wm('density '+func)
        def shell_wm_size(self,func=''):#''列出当前显示的分辨率。 'axb'设置分辨率，注意手机的格式为“横向x纵向” 'reset'恢复默认
            adbcommand().adb_shell().shell_wm('size '+func)
        def shell_wm_overscan(self,a='',b='',c='',d=''):
            adbcommand().adb_shell().shell_wm('overscan '+ a + ',' + b + ',' + ',' + c + ',' + d)#adb shell wm overscan a,b,c,d
        def shell_input(self,func=''):
            logging.info('Core:adb shell input')
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
        logging.info('Core:adb push')
        self._adbc("push "+'"'+urlc+'" "'+urlp+'"')
    def pull(self,urlp,urlc):
        logging.info('Core:adb pull')
        self._adbc("pull "+'"'+urlp+'" "'+urlc+'"')

def checkinternet():
    logging.info('Check Internet')
    if p=='Windows':exit_code = os.system('ping www.baidu.com')
    elif p=='Linux':exit_code = os.system('ping -c 3 www.baidu.com')
    logging.info('Check Internet End.The result is:'+str(exit_code))
    if exit_code:
        return False
    else:
        return True
def clear():
    logging.info('Clean the display')
    if p == "Windows":
        os.system('cls')
    if p == "Linux":
        os.system('clear')
    logging.info('Finished Clean the display')

def setmode():#setmode parseinput(2)
    logging.info('Setmodel:')
    print(Luan.ltext1)
    import adbshellpy_home  
    adbshellpy_home.parseinput(2)

def Console():
    logging.info('Go Into Home.')
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
    print(Luan.ltext2)
    errexit(2)

def IsPassInstall():#检测adb安装
    logging.info('Pass or install !?')
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
    logging.info('APK Install:')
    if install==True:
        import adbshellpy_libapkfile
        adbshellpy_libapkfile.mainex(_Options.apkfile)
        return
    logging.info('No APK Installed.')

        
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
      'shizuku','driver-install','fastboot'
     ]#内置命令
  logging.info('Check command')
  if cmd in c:#开发计划3
      logging.info('Command found')
      import adbshellpy_home
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
      if cmd=='driver-install':fun.driver_install()
      if cmd=='fastboot':fun.fastbootmode()
      sys.exit(0)
  logging.info('No Command found.Pass')
  checkflag=opt.installcheck
  if sys.hexversion < 0x03060000:
      errexit(3)
  if opt.help == True:
      usage()
      sys.exit(0)
  if os.path.exists('adb') == False: #adb文件夹不存在
      logging.warning('No adb found.Start install.')
      install(p)
  logging.info('Conf parser → adbshell.ini.')
  conf = configparser.ConfigParser()
  conf.read('adbshell.ini')
  conf.set('adbshell', 'adbfile', adbfile)
  with open('adbshell.ini', 'w') as ini:
      conf.write(ini)
  logging.info('Conf Parser → adbshell.ini End.')
  apkinstallmode(opt.apkinstall)
  if p == "Windows" or p == "Linux":
      Console()
  else:
      errexit(1)

def install(p,check=0):
    global uselinuxpkgmanagertoinstalladb
    global adbfile,fastbootfile,adb
    global conf
    global checkflag
    logging.info('Installing adb file.')
    adbcommand().kill_server()
    if check==2:
        pass
    #Internet Check
    if checkinternet()==False:
        errexit(5)
        print(Luan.w4)
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
            print(str(errinform)+Luan.i5)
            adbfile_=r'platform-tools\adb.exe'
            adbfile=adbfile_
            fastbootfile=r'platform-tools\fastboot.exe'
            conf.set('adbshell', 'adbfile', adbfile_)
            conf.set('adbshell', 'fastbootfile', fastbootfile)
            with open('adbshell.ini', 'w') as ini:
                conf.write(ini)
            return
            #errexit(0)
        logging.info('Set adbfile/fastbootfile : adb/adb.exe adb/fastboot.exe')
        adbfile=r'adb\adb.exe'
        fastbootfile=r'adb\fastboot.exe'
        try:
            os.remove('adb.zip')
        except Exception as errinform:
            print(errinform)
    if p == 'Linux':
        
        if uselinuxpkgmanagertoinstalladb == 'enable':
            print(Luan.a2)
            print(Luan.i6)
            inputtext=input('>>>')
            logging.info('Linux Use Flag:'+inputtext)
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
                #install(p)
                #return
        
        if platform.machine()=='x86_64':#AMD64 linux x86 or x86_64
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
            adbfile='adb/adb'
            fastbootfile='adb/fastboot'
            os.system('chmod 777 adb/adb')
            os.system('chmod 777 adb/fastboot')
            try:
                os.remove('adb.zip')
            except Exception as errinform:
                print(errinform)
            return
        if platform.machine()=='aarch64':# or platform.machine()=='aarch' But,No 32bit EXEC!
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
            adbfile='adb/adb'
            fastbootfile='adb/fastboot'
            os.system('chmod 777 adb/adb')
            os.system('chmod 777 adb/fastboot')
            return
        return
    return
if not adbfile:#adb文件默认设置 默认adb,自动选择platform-tools或adb 可以在环境变量中设置
    #global conf
    #No Bin Files Found
    if p == "Windows":
        if os.path.exists('adb') == False:
            adbfile=r'platform-tools\adb.exe'
            fastbootfile=r'platform-tools\fastboot.exe'
        else:
            adbfile=r'adb\adb.exe'
            fastbootfile=r'adb\fastboot.exe'
    if p == "Linux":
        if os.path.exists('adb') == False:
            adbfile='platform-tools/adb'
            fastbootfile='platform-tools/fastboot'
        else:
            adbfile='adb/adb'
            fastbootfile='adb/fastboot.exe'
    install(p)
    if p == "Windows":
        adbfile=r'platform-tools\adb.exe'
        fastbootfile=r'platform-tools\fastboot.exe'
        conf.set("adbshell", "adbfile", adbfile)
        conf.set("adbshell", "fastbootfile", fastbootfile)
        conf.write(open("adbshell.ini", "w"))
adb=adbcommand(nowdevice)
if __name__ == '__main__':
    main(sys.argv[1:])