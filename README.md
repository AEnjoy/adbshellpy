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

# 功能介绍:0.7.x

安卓玩机精灵是您的下一代Android玩机助手,基于Google的adb,需要Python3.6+的辅助

功能:

访问Android手机的终端shell

重启Android手机至特殊状态reboot shutdown rec bl edl sideload download

为Android手机安装/卸载/禁用/启用应用

查看您的Android手机所安装的应用

终端与PC之间传输文件push/pull

系统调节

支持了多语言!!!!

模拟操作(input)

系统监控

系统截屏

黑域 shizuku  冰箱  快否激活

etc.

工具箱大小较小,支持自动下载所需功能(0.6.0始支持)

如果你的系统是Linux,且使用的是二进制文件,请解压后授予可执行权限和su权限后再运行!(su)

Windows系统可选是否使用管理员权限=.=

![功能界面](des.png)

开发分支:https://github.com/AEnjoy/adbshellpy/tree/dev 包含所有最新的功能及改进

# ChangeLog:

```
0.7.1→0.7.2       2021-2-17 15:12:10
1.IMPROVE:提升快否下载速度
2.NEW:增加了手动编译终端:make.py,供用户自行编译为可执行文件(至其它平台)
3.FIX:修复update检查更新失败
4.FIX:修复environment崩溃
5.IMPROVE:若检查不到libshfile,则脚本会自动下载扩展

0.7→0.7.1          2020-11-13 17:49
1.FIX:If your system is Linux, adb installation will no longer fail.
2.IMPROVE:Multi-version compilation is enadble.

0.6.2.4→0.7        2020-8-10 00:23:20
1.FIX:初始化运行时只需要一次即可完成安装adb至进主页.
2.NEW:logging日志系统引入
3.NEW:多语言支持

0.6.2.3→0.6.2.4    2020-8-6 19:08:35
1.FIX:修复adb安装时一处可能的代码bug导致的崩溃
2.IMPROVE:优化了代码结构

0.6.2.1→0.6.2.2    2020-8-2 16:36:40
1.FIX:修复默认设置不生效的问题
2.FIX:修复NewCompile模式的bug

0.6.1.3→0.6.2.1  2020-8-1 15:44:04
1.IMPROVE:更新了部分源地址 
2.IMPROVE:将changelog变更为utf-8编码
3.IMPROVE:help文件更新
4.NEW:现在将在启动时检查文件完整性
5.NEW:现在支持-more(但不支持静默模式)
6.NEW:现在支持重启至edl模式(9008)(仅部分设备支持)
7.NEW:现在可以启用特性:在检测不到内置命令时直接执行shell命令
8.NEW:clen-data功能,清除程序数据,执行干净安装
9.NEW:支持显示服务器的信息(项目地址),可设置关闭.
10.NEW:支持显示可自定义的设置项.
11.FIX:修复NewCompile模式的bug
12.FIX:修复setting崩溃的问题
13.FIX:修复set死循环问题

0.6.1.2→0.6.1.3 2020-7-30 22:22:58
1.IMPROVE:提升检查更新成功率


...剩余内容请看ChangeLog

```

[Changelogs Full](Changlog)
