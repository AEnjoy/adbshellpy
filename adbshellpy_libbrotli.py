#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellPy_LibBrotli
#       By : 神郭
#  Version : 1.0
import sys,os
try:
    import brotli as b
except:
    import time
    print('LibBrotli is not installed,the mode will be installed after 3s.')
    time.sleep(3)
    os.system('pip3 install brotli')
    import brotli as b
class adbshellpyinformation:
    p=None
    branch=None
    uselinuxpkgmanagertoinstalladb=None
    adbfile=None
    aapt=None
    conf=None    
def main(INPUT_FILE='system.new.dat.br',OUTPUT_FILE='system.new.dat',flag=1):
    if flag==1:
        f=open(INPUT_FIL)
        f=b.decompress(f.read())
        ofile=open(OUTPUT_FILE, 'wb')
        os.write(ofile,f)
        f.close()
        ofile.close()
        sys.exit()
    if flag==2:
        f=open(INPUT_FIL)
        f=b.compress(f.read())
        ofile=open(OUTPUT_FILE, 'wb')
        os.write(ofile,f)
        f.close()
        ofile.close()
        sys.exit()
    print('参数无效!')
    sys.exit(1)
    pass
if __name__ == '__main__':
    try :
        INPUT_FILE=str(sys.argv[1])
        #OUTPUT_FILE=str(sys.argv[2])
    except IndexError:
        print('''
        \n用法: adbshellPy_libBrotli.py <INPUT_FILE> [<OUTPUT_FILE>] [Flag] \n
                 INPUT_FILE           输入文件
                 OUTPUT_FILE          输出文件
                 Flag                 参数 1.br解压缩,2.压缩为br
        ''')
        input('按 ENTER 退出...')
        sys.exit(1)
    try:
        OUTPUT_FILE=str(sys.argv[2])
        flag=int(sys.argv[3])
    except : pass
    main(INPUT_FILE,OUTPUT_FILE,flag)