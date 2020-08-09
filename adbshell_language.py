#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshell_language.py
#      language mode
#       By : 神郭
#  Version : 0.7
'''
This is the language setting of Adbshellpy
Each language is contained in a class
Now,we support English and Simplified-Chinese
Welcome to contribute your language so that more international friends can use it.
How to do it?
Just submit it on GitHub of this project!
Some character meanings:
N:number
eN:Error message.
aN:Ask message.
iN:General message.
wN:Warning message.
ltextN:Long text message
'''
class chn():
    EXIT='按 ENTER 退出...'
    EXIT1='按 ENTER 继续或退出...'
    e1='文件夹创建失败!'
    e2='仅支持Linux Windows 暂未添加其它平台功能支持'
    e3='请输入有效数据!'
    e4='E:网络出现问题,请检查网络!'
    e5='E:未找到可用设备!\nadbshellpy可能不会正常工作.'
    e6='E:仅支持Windows 暂未添加其它平台功能支持'
    e7='E:更新日志文件"Changlog"不存在,无法查看更新记录!'
    e8='E:权限不足!'
    e9=' 加载失败!'
    e10='本地文件或文件夹为空'
    e11='E:请输入有效远端路径'
    e12='E:您已处于主菜单!'
    e13='E:该项仅对Linux生效'
    
    a1='您当前使用的adbshellpy存在新版本,是否更新?y/n'
    a2='正在使用系统软件包管理器安装adb,需要请求sudo,若不想使用此请求,输入n,默认y'
    a3='传输至电脑并打开查看>>>[Y/N 默认N]'
    a4='...LINUX查看?需要提前安装imagemagick>>>[Y/N 默认N]'
    a5='Compile:请选择compile功能模式: 1).传统  2).新版 :'
    a6='清除adbshellpy的数据,以恢复原始安装.输入yes继续.'
    a7='您确定设置此项吗?Y/N>>><默认为Y>'
        
    w1='W:未授权的设备: %s 找到,请在手机上允许USB调试(一律)'
    w2='W:adbshellpy who 可能不会工作!'
    w3='W:设备标识符一致?'
    w4='W:您的网络似乎出现了故障,adb将不会安装.这有可能导致工具箱无法使用,您可能需要手动设置adb文件.'
    w5='W:放弃设置'
    w6='W :未知指令'
    
    i1='完整包升级完成,请重启 adbshellpy实例'
    i2='您当前使用的adbshellpy为最新版本,无需更新.'
    i3='检测到的设备:'
    i4='跳过该设备: %s '
    i5='改为默认platform-tools'
    i6='Y 使用系统软件包(default,Enter) N 不使用系统软件包管理器'
    i7='当前adbshellpy控制的设备:'
    i8=' \n 你可以使用who切换目标设备.(仅有一个设备时不会显示,但功能依然可用)'
    i9='push:从本地中复制一个文件(夹)至手机'
    i10='远端路径>>>'
    i11='默认使用 /sdcard'
    i12='本地文件或文件夹>>>'
    i13='pull:从手机中拉取一个文件(夹)至本地'
    i14='默认使用当前路径'
    i15='screencap:对手机执行截屏命令,并可选择是否传输至电脑并立即查看'
    i16='dumpsys:获取或设置一些调试信息(转储所有服务)。在adbmode→help→dumpsys查询命令列表'
    i17='通过ADB读取/更改系统设置 在adbmode→help→settings查询命令列表'
    i18='欲查看或设置的信息>>>'
    i19='附加的参数>>>'
    i20='欲清除数据的程序包名>>>'
    i21='欲启用的程序包名>>>'
    i22='欲禁用的程序包名(使用applist查看)>>>'
    i23='编译模式[默认-m speed]>>>'
    i24='编译参数[默认 为空]>>>'
    i25="编译对象[默认-a]>>>"
    i26='执行该操作将消耗一定时间,请坐和放宽'
    i27='当前时间: '
    i28='结束时间: '
    i29='执行用时: %s Seconds'
    i30='您的选择>>>'
    i31='欲移除的程序包名(使用applist查看)>>>'
    i32='欲安装的apk文件>>>'
    i33='您当前的设备:'
    i34='切换后的设备:'
    i35='操作执行完成,请重新运行实例以初始化'
    i36='欲设置的选项:[回车退出设置]>>>'
    i37='E:指定的ADB File不存在,请检查Path!'
    i38='本地路径>>>'
    
    ltext1='''
    **********************************Setmode*****************************************
    *setting(default,Enter) 设置参数 cls 清屏 back 回到上一菜单 exit 退出            *
    *您也可以通过手动编辑adbshell.ini来修改设置                                      *
    **********************************Setmode*****************************************
    '''
    ltext2="""
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
    """
    ltext3='''
    **********************************Welcome*****************************************
    *                                ADBSystemTOOLBOX                                *
    *                       基于Python3&GoogleADB的安卓系统工具箱                    *
    *                     Develop:  CoolApkUser:白曦  Github:AEnjoy                  *
    *               如果你链接了多个设备,请先使用输入who命令再输入其它命令哦!        *
    **********************************Welcome*****************************************
    '''
    ltext4='''
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
     -------------------------------ADBSystemTOOLBOX----------------------------------
    '''
    ltext5='''
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
    '''
    ltext6='''
    command:(Only Enter To Return)
    input_text:    向手机输入一串字符(不支持中文)
    input_keyevent:模拟输入内容(在adbshell→help→input中可查询指令)
    input_tap:     模拟点击屏幕上的一个像素点
    input_swipe:   模拟滑动屏幕(从一个像素点到另一像素点)
    '''
    ltext7='''
    Compile :
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
    '''
class eng():
    EXIT='Press ENTER to exit...'
    EXIT1='Press ENTER to continue or exit...'
    e1='Folder creation failed!'
    e2='Only supports Linux and Windows. No other platform function support has been added yet'
    e3='Please enter valid data!'
    e4='E: There is a problem with the network, please check the network!'
    e5='E: No available device found! \nadbshellpy may not work properly.'
    e6='E: Only support Windows, no other platform function support has been added yet'
    e7='E: The update log file "Changlog" does not exist, and the update record cannot be viewed!'
    e8='E: Insufficient permissions!'
    e9=' Failed to load!'
    e10='The local file or folder is empty'
    e11='E: Please enter a valid remote path'
    e12='E: You are already in the main menu!'
    e13='E: This item is only valid for Linux'
    
    a1='There is a new version of adbshellpy you are currently using, is it updated? y/n'
    a2="You are using the system package manager to install adb, you need to request sudo, if you don't want to use this request, enter n, default y"
    a3='Transfer to computer and open to view >>>[Y/N default N]'
    a4='...View in Linux? Imagemagick needs to be installed in advance>>>[Y/N default N]'
    a5='Compile: Please select the compile function mode: 1). Traditional 2). New version:'
    a6='Clear the data of adbshellpy to restore the original installation. Enter yes to continue.'
    a7='Are you sure to set this? Y/N>>><default is Y>'
        
    w1='W: Unauthorized device: %s found, please allow USB debugging on the phone (all)'
    w2='W: adbshellpy who May not work!'
    w3='W: The device identifiers are consistent?'
    w4='W: Your network seems to be malfunctioning and adb will not be installed. This may cause the toolbox to be unusable, and you may need to manually set the adb file.'
    w5='W: Give up setting'
    w6='W: Unknown command'
    
    i1='The complete package upgrade is complete, please restart the adbshellpy instance'
    i2='The adbshellpy you are currently using is the latest version and does not need to be updated.'
    i3='Devices detected:'
    i4='Skip this device: %s '
    i5='Change to default platform-tools'
    i6='Y Use system package (default, Enter);N Do not use system package manager'
    i7='Devices currently controlled by adbshellpy:'
    i8=' \n You can use who to switch the target device. (It will not be displayed when there is only one device, but the function is still available)'
    i9='push:Copy a file (folder) from the local to the phone'
    i10='Remote path>>>'
    i11='Used by default /sdcard'
    i12='Local file or folder>>>'
    i13='pull:Pull a file (folder) from the phone to the local'
    i14='Use current path by default'
    i15='screencap:Execute the screen capture command on the phone, and choose whether to transfer it to the computer and view it immediately'
    i16='dumpsys:Get or set some debugging information (dump all services). Query the command list in adbmode→help→dumpsys'
    i17='Read/change system settings through ADB. Inquire the command list in adbmode→help→settings'
    i18='Information to view or set>>>'
    i19='Additional parameters>>>'
    i20='The package name of the data to be cleared>>>'
    i21='Package name to be activated>>>'
    i22='The name of the package to be disabled (use applist to view)>>>'
    i23='Compilation mode[default-m speed]>>>'
    i24='Compilation parameters[default empty]>>>'
    i25="Compiled object[default-a]>>>"
    i26='Performing this operation will consume a certain amount of time, please sit and relax'
    i27='Current time: '
    i28='End Time: '
    i29='Execution time: %s Seconds'
    i30='Your choice>>>'
    i31='The name of the package to be removed (use applist to view)>>>'
    i32='Apk file to be installed>>>'
    i33='Your current device:'
    i34='Switched device:'
    i35='The operation is complete, please rerun the instance to initialize'
    i36='The option to be set: [Enter to exit the setting]>>>'
    i37='E: The specified ADB File does not exist, please check Path!'
    i38='Local path>>>'
    
    ltext1='''
    **********************************Setmode*****************************************
    *           setting(default,Enter)      cls        back       exit               *
    *       You can also modify the settings by manually editing adbshell.ini        *
    **********************************Setmode*****************************************
    '''
    ltext2="""
    Usage:adbshell.py [apkfile(s)] [args or Console] [-MORE] 
    [apkfile(s)] [Dev]
    Install apk file to mobile phone. Support multiple files.
    [args]
    -nc --ncheck Skip adb installation detection 
    -h --help help Show Help
    [Console][Abandoned]
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
    """
    ltext3='''
    **********************************Welcome*****************************************
    *                                ADBSystemTOOLBOX                                *
    *                     Android toolbox based on Python3&GoogleADB                 *
    *                    Develop:  CoolApkUser:Baixi  Github:AEnjoy                  *
    *  If you have connected multiple devices, please use the who command first and  *
    *  then other commands!                                                          *
    **********************************Welcome*****************************************
    '''
    ltext4='''
     _____________________________ADBSystemTOOLBOX____________________________________
    ┃  Toolbox command:  ┃  help>  back   cls  set>  who>  home  exit    FixGithub   
    ┃     re-install      update      environment      changes    clean-data        
     ---------------------------------------------------------------------------------
    ┃        ADB command:     ┃ shell   root(√)                                              
    ┃ Device link options:    ┃start_server(√) kill_server devices tcpipconnect usb(√) 
    ┃ Advanced device restart:┃reboot shutdown rec bl edl sideload download(SamsumgDevices)
     ---------------------------------------------------------------------------------
    ┃        App      : ┃ install> uninstall> disable> enable> clear> applist>             
    ┃  System improve : ┃ compile>                                              
    ┃  File  transfer : ┃ pull>        push>   screencap>                            
    ┃  System  adjust : ┃ windowmode>  input>  settings>  dumpsys>                      
    ┃  App  activated : ┃ piebridge shizuku  icebox  kfmark                
    ┃  Other function : ┃ relatedapk                                        
     -------------------------------ADBSystemTOOLBOX----------------------------------
    '''
    ltext5='''
    get [--user <USER_ID> | current] NAMESPACE KEY
      Retrieve the current value of KEY.
    put [--user <USER_ID> | current] NAMESPACE KEY VALUE [TAG] [default]
      Change the contents of KEY to VALUE.
      TAG to associate with the setting.
      {default} to set as the default, case-insensitive only for global/secure namespace
    delete [--user <USER_ID> | current] NAMESPACE KEY
      Delete the entry for KEY.
    reset [--user <USER_ID> | current] NAMESPACE {PACKAGE_NAME | RESET_MODE}
      Reset the global/secure table for a package with mode.
      RESET_MODE is one of {untrusted_defaults, untrusted_clear, trusted_defaults}, case-insensitive
    list [--user <USER_ID> | current] NAMESPACE
      Print all defined keys.
      NAMESPACE is one of {system, secure, global}, case-insensitive
    '''
    ltext6='''
    command:(Only Enter To Return)
    input_text:    Enter a string of characters into the phone
    input_keyevent:Analog input content (instructions can be queried in adbshell→help→input)
    input_tap:     Simulate clicking a pixel on the screen
    input_swipe:   Simulate sliding screen (from one pixel to another)
    '''
    ltext7='''
    Compile :
    Compile New
    Improve performance by compiling AndroidN+ applications with dexopt
    Note: If you are using Android Q or higher, please be careful to compile system applications, especially high-risk components:
    com.android.systemui
    Known issues:
    Android Q
    1.MIUI Android QCompiling system applications will cause severe frame drop
    2.Samsung OneUI 2.0+There will be a problem that the desktop cannot be entered after booting, and the system is globally black.
    3.LG UX 9 Will freeze and restart when the screen is locked
    4.com.android.systemui Does not support manual installation and restoration!!!
    Android N / O
    1. Compilation does not show progress
    If you are a Samsung user: Galaxy Labs' App Booster is recommended. Its principle is the compilation principle and there is no security risk
    performance:everything＞speed＞[default]speed-profile＞quicken＞[Does not compile]
    Compilation time:everything＞speed
    Space occupation:everything＞speed＞[default]speed-profile＞quicken＞spacesave＞[Does not compile]
    **********************************Compile*****************************************
    *  (00).Back [Enter]                                                            
    *  (01).Use everything mode to compile all applications [system, user] (mandatory)
    *  (02).Use everything mode to compile all applications [system, user]            
    *  (03).Use speed mode to compile all applications [system, user] (mandatory)                                
    *  (04).Use speed mode to compile all applications [system, user]                                       
    *       For the first compilation optimization, it is recommended to choose the 
    *       method with (mandatory) option                                 
    *       For small memory devices, devices with low storage remaining, emmc devices, 
    *       it is recommended to use the speed method to reduce IO pressure        
    *       Android N O P recommends the above options (01-04), Android Q recommends the
    *       following options (05-08)             
    *  (05).Use everything mode to compile all applications [user] (mandatory)                                
    *  (06).Use everything mode to compile all applications [user]                                       
    *  (07).Use speed mode to compile all applications [user] (mandatory)                                     
    *  (08).Use speed mode to compile all applications [user]                                            
    *      First aid function                                                                  
    *  (09).Restore systemUI compilation (quicken default) ←Recommended                                       
    *  (10).Restore systemUI compilation (speed default)                                               
    *  (11).Restore systemUI compilation (clear compilation)                                                
    *  (12).Clear third-party application compilation                                                        
    *  (13).Clear system application compilation                                                          
    *  (14).Clear third-party application compilation[quicken]                                               
    *  (15).Clear system application compilation[quicken]                                                           
    *  (16).Clear all compilation[quicken]                                                   
    *  (17).Clear all compilation                                                             
    *  Thanks: CoolApk User:后知                                                     
    **********************************Compile*****************************************
    !:Input 01 and 1 have the same effect.
    '''
