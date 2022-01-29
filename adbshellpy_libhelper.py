#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   adbshellpy_libhelper.py
#       By : 神郭
#  Version : 0.8
import sys
class helper():
    def kf(self):
        print('kfmark:激活快否APP实例')
    def relatedapk(self):
        print('''relatedapk:关联Android 应用程序.apk文件
        关联.apk文件,以方便apk文件的安装
        Requirement:
        System         : Windows 7 + x86/AMD64/IA64/arm/arm64 新特性关联文件
        Microsoft.NET  : 4.0 + (opt) 用于显示APP图标
        ''')
    def who(self):
        print('''who:切换adbshellpy设备
        当使用两个或两个以上设备时,可以使用who来改变你当前操作的设备
        ''')
    def usage(self):
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
    
    def push(self):
        print('''push:从本地中复制一个文件(夹)至手机
        远端路径>>>[/sdcard/]手机端的文件或文件夹可空,默认为/sdcard
        本地文件或文件夹>>>本地文件或文件夹所在路径
        ''')
    def fixgithub(self):
        print('FixGitHub:修复由于中国DNS污染导致GitHub访问异常的问题,可以解决GitHubRAW异常,修复软件更新检测,lib下载等(需要修改Hosts文件,需要更高权限及杀软同意)')
    def pull(self):
        print('''pull:从手机中拉取一个文件(夹)至本地
        远端路径>>>手机端的文件
        本地路径>>>[local]可空,默认为脚本执行路径
        ''')
    def screencap(self):
        print('''screencap:对手机执行截屏命令,并可选择是否传输至电脑并立即查看
        传输至电脑并打开查看>>>[Y/N 默认N]
        ...LINUX查看?需要提前安装display>>>[Y/N 默认N]
        ''')
    def driver_install(self):
        print('用于安装adbwinusb驱动程序以使软件正常运行')
    def dumpsys(self):
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
    def settings(self):
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
    def applist(self):
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
    def input(self):
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
    def install(self):
        print('''install:
        欲安装的apk文件>>><apkfile>  欲安装的apk文件路径(支持绝对路径,本地路径)
        欲附加的参数>>>[<args>default=-d -g] -l锁定应用程序 -t允许测试包 -d允许降级覆盖安装 -p部分应用安装  -g为应用程序授予所有运行时的权限 所有指令之间保留空格
        ''')
    def uninstall(self):
        print('''unistall:
        欲移除的程序包名(使用applist查看)>>><Package>
        欲附加的参数>>>[<args>] -k 保留应用数据
        ''')
    def compile(self):
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
        编译参数>>>[<func>可选] -f强制编译甚至是不需要的程序 --check-prof (true | false)在进行dexopt时查看配置文件 --split SPLIT: compile only the given split name
        编译对象>>>[<pkg>default=-a] -a 所有程序包 pkg:指定的一个程序包
        ''')
    def disable(self):
        print('''disable:
        欲禁用的程序包名(使用applist查看)>>><Package>
        ''')
    def enable(self):
        print('''enable:
        欲启用的程序包名(使用applist查看)>>><Package>
        ''')
    def clear(self):
        print('''clear:
        欲清除数据的程序包名(使用applist查看)>>><Package>
        ''')
    def clen_data(self):
        print('执行干净安装,清除程序数据和设置项.将会清除__pycache__,adb,build-tools,adbshell.ini 并重新初始化程序')
    def windowmode(self):
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
    def help(self):
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
        activate:激活黑域 shizuku服务
        who:改变adbshellpy操作的设备
        relatedapk:关联apk文件
        kfmark,shizuku,piebridge,scene:激活快否,zhizuku,黑彧,scene 5
        driver-install:安装adb驱动文件.
        ****************************ADBSystemTOOLBOXHELP**********************************
        ''')
        '''
        inputtext=input('>>>')
        inputtext=inputtext.replace(" ", "")
        '''
def main():
    h=helper()
    h.help()
    print("输入你要详细查询的命令:(back,exit,回车(Enter)结束help视图view)")
    inputtext=input('>>>')
    inputtext=inputtext.replace(" ", "")
    if inputtext=='' or inputtext == 'back' or inputtext=='exit':
        return
    if inputtext == 'kfmark':
        h.kf()
        return
    if inputtext=='push':
        h.push()
        return
    if inputtext=='pull':
        h.pull()
        return
    if inputtext=='screencap':
        h.screencap()
        return
    if inputtext =='dumpsys':
        h.dumpsys()
        return
    if inputtext=='settings':
        h.settings()
        return
    if inputtext=='applist':
        h.applist()
        return
    if inputtext=='input':
        h.input()
        return
    if inputtext=='install':
        h.install()
        return
    if inputtext=='uninstall':
        h.uninstall()
        return
    if inputtext=='compile':
        h.compile()
        return
    if inputtext=='disable':
        h.disable()
        return
    if inputtext=='enable':
        h.enable()
        return
    if inputtext=='clear':
        h.clear()
        return
    if inputtext=='windowmode':
        h.windowmode()
        return
    if inputtext=='who':
        h.who()
        return
    if inputtext=='relatedapk':
        h.relatedapk()
        return
    if inputtext=='fixgithub':
        h.fixgithub()
        return
    if inputtext=='clean-data':
        h.clen_data()
        return
    if inputtext=='driver-install':
        h.driver_install()
        return
    print('Unkonw command!')
    return
if __name__ == '__main__':
    main()