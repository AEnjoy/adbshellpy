# This is the stable-building Version

How to use

```
git clone https://github.com/AEnjoy/adbshellpy.git
```

And then, running adbshell.py. Enjoy it!

你至少需要下载以下文件:

adbshell.py

adbshellpy_home.py

~~adbshellpy_libapkfile.py~~(dev)

adbshellpy_libhelper.py

# 功能介绍:0.6.0

adbshellpy是您的下一代Android玩机助手,需要Python3.6+

功能:

访问Android手机的终端shell

重启Android手机至特殊状态reboot shutdown rec bl edl sideload download

为Android手机安装/卸载/禁用/启用应用

查看您的Android手机所安装的应用

终端与PC之间传输文件push/pull

系统调节

模拟操作(input)

系统监控

系统截屏

黑域 shizuku  冰箱  快否激活

etc.

工具箱大小较小,支持自动下载所需功能(0.6.0始支持)

![功能界面](des.png)

开发分支:https://github.com/AEnjoy/adbshellpy/tree/dev 包含所有最新的功能及改进

# ChangeLog:

```
0.6.1.1→0.6.1.2 2020-7-25 00:14:50
1.NEW:Changlog分离
2.NEW:fixgithub功能
3.NEW:现在可以选择添加是否在启动时Kill ADB服务
4.FIX:修复了查看help后直接退出的bug
5.FIX:修复了compile的一些bug
6.FIX:修复从旧版本更新上来因为adbshell.ini配置老旧,导致的错误崩溃
0.6.1→0.6.1.1 2020-7-23 09:50:55
1.修复了一个Root的Bug

0.6.0→0.6.1 2020-6-26 01:24:55
1.修复who不识别第三方REC的问题
2.compile可选择高级编译

0.5.4Beta→0.6.0Stable  2020-5-5 00:12:54
1.UI优化
2.修复崩溃问题
3.支持激活快否
4.一些小改进
5.支持激活冰箱
6.支持多设备切换:who指令
7.支持关联apk文件(实验性)
8.代码块拆分

0.5.3Beta→0.5.4Beta 2020-4-21 00:17:19
1.修复第一次运行adb不安装的bug
2.修复shell wm overscan闪退bug

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

...剩余内容请看ChangeLog

```

[Changelogs Full](Changlog)