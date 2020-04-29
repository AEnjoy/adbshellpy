#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_libroot
#       By : 神郭
#  Version : 1.0
import sys,os,zipfile
try:
    from adbshell import errexit
    from adbshell import update
    from adbshell import checkinternet
    from adbshell import clear
    from adbshell import adbcommand
    from adbshell import install
    from adbshell import changes
    from adbshell import github
    from adbshell import version
    from adbshell import builddate
    from adbshell import p
    from adbshell import adbfile
    from adbshell import conf   
except:
    from adbshell_alpha import errexit
    from adbshell_alpha import update
    from adbshell_alpha import checkinternet
    from adbshell_alpha import clear
    from adbshell_alpha import adbcommand
    from adbshell_alpha import install
    from adbshell_alpha import changes
    from adbshell_alpha import github
    from adbshell_alpha import version
    from adbshell_alpha import builddate
    from adbshell_alpha import p
    from adbshell_alpha import adbfile
    from adbshell_alpha import conf
class adbshellpyinformation:
    branch=None
    uselinuxpkgmanagertoinstalladb=None
    adbfile=None
    aapt=None
