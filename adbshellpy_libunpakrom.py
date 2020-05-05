#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_libunpakrom
#       By : 神郭
#  Version : 1.0
from __future__ import print_function
import sys,os,zipfile,urllib.request
class adbshellpyinformation():
    import platform
    p=platform.system()
    try:from adbshell_alpha import branch
    except:
        try:from adbshell import branch
        except:branch='dev'
    uselinuxpkgmanagertoinstalladb=None
    adbfile=None
    aapt=None
    conf=None

class rominformation:
    '''brotli=None
    newdat=None
    olnyimg=None
    onlyfolder=None
    ozip=None
    androidVersion=''
    '''
    type=None #1功能性卡刷包(如opengapps) 2ROM卡刷包 3线刷包
    def __init__(self,file=''):
        '''获取ROM信息 输入的文件可以是线刷包,也可以是卡刷包'''
        if os.path.exists(file)==False:
            print('E:请选择一个正确的文件!!!')
            self.flag=1#无效文件路径
            return
        if zipfile.is_zipfile(file)==False:
            self.flag=2
            if file.find('.ozip') > -1:self.ozip=True
            if file.find('.kd') > -1:self.lgkd=True
            if file.find('.kdz') > -1:self.lgkdz=True
            if file.find('.tar.md5') > -1:self.samsumgodinfile=True
            return
        z=zipfile.ZipFile(file)
        self.l=z.namelist()
        #z.close()
        if 'system.img' in self.l:
            self.olnyimg=True
        if 'system/framework/framework.jar' in self.l:
            self.onlyfolder=True
        if 'system.new.dat.br' in self.l and 'system.transfer.list' in self.l:
            self.brotil=True
        if 'system.new.dat' in self.l and 'system.transfer.list' in self.l:
            self.newdat=True
        if 'system.transfer.list' in self.l:
            z.extract('system.transfer.list')
            f = open('system.transfer.list', 'r')
            v = int(f.readline())
            f.close()
            if v == 1:
                print('Android Lollipop 5.0 检测到!\n')
                self.androidVersion='Lollipop 5.0 API 21'
            elif v == 2:
                print('Android Lollipop 5.1 检测到!\n')
                self.androidVersion='Lollipop 5.1 API 22'
            elif v == 3:
                print('Android Marshmallow 6.x 检测到!\n')
                self.androidVersion='Marshmallow 6.x API 23'
            elif v == 4:
                print('Android Nougat 7.x / Oreo 8.x 或更高版本检测到!\n')
                self.androidVersion='Nougat 7.x or higher API 24+'
        for names in self.l:#prop获取Android版本
            if names.find('*.prop') > -1:
                try:z.extract(names)
                except:pass
                if os.path.exists('system.prop'):
                    f=open('system.prop')
                    l=[]
                    for i in f:l.append(i.strip())
                    f.close()
                    for i in l:
                        x=i.split('=')
                        if x[0]=='ro.build.version.sdk':
                            try:
                                sdk=int(x[1])
                                if sdk < 21:print('W:您处理的ROM太老旧了哦,不支持显示版本及代号,仅支持显示API版本')
                                elif sdk==21:self.androidVersion='Lollipop 5.0'
                                elif sdk ==22:self.androidVersion='Lollipop 5.1'
                                elif sdk ==23:self.androidVersion='Marshmallow 6.0'
                                elif sdk ==24:self.androidVersion='Nougat 7.0'
                                elif sdk ==25:self.androidVersion='Nougat 7.1'
                                elif sdk ==26:self.androidVersion='Oreo 8.0'
                                elif sdk ==27:self.androidVersion='Oreo 8.1'
                                elif sdk ==28:self.androidVersion='Pie 9.0'
                                elif sdk ==29:self.androidVersion='Q 10.0'
                                elif sdk ==30:self.androidVersion='R 11.0'
                                self.androidVersion=self.androidVersion+ ' API: '+x[1]
                            except:print('E:你目前处理的ROM似乎是开发者内侧版或被修改成了错误的值.')
                        
def lz4install():
    if adbshellpyinformation().p=='Linux':
        os.system('sudo apt install lz4 -y')
        os.system('sudo yum install lz4 -y')
    else:
        if os.path.exists('lz4.exe')==False:
            urllib.request.urlretrieve('https://github.wuyanzheshui.workers.dev/lz4/lz4/releases/download/v1.9.2/lz4_win32_v1_9_2.zip','lz4.zip')
            z=zipfile.ZipFile('lz4.zip')
            z.extract('lz4.exe')
            z.close()
    return
class lg_kd_kdz():
    def __init__(self,file):
        """
        GitHub Paper:https://github.com/randomstuffpaul/kdztools
        Copyright (C) 2016 Elliott Mitchell <ehem+android@m5p.com>
        Copyright (C) 2013 IOMonster (thecubed on XDA)
	    This program is free software: you can redistribute it and/or modify
	    it under the terms of the GNU General Public License as published by
	    the Free Software Foundation, either version 3 of the License, or
	    (at your option) any later version.
	    This program is distributed in the hope that it will be useful,
	    but WITHOUT ANY WARRANTY; without even the implied warranty of
	    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	    GNU General Public License for more details.
	    You should have received a copy of the GNU General Public License
	    along with this program.  If not, see <http://www.gnu.org/licenses/>.
        file 输入的文件(kdz/kd)
        """        
        if os.path.exists(file)==False:
            print('E:无效文件路径!')
            return
        
class oppoozip():
    # (c) B. Kerler 2017-2020, licensed under MIT license
    # GitHub Paper:https://github.com/tahirtaous/ozip2zip
    #from docopt import docopt
    #args = docopt(__doc__, version='1.2')
    import stat,shutil,binascii
    from Crypto.Cipher import AES
    keys = [
        "D6EECF0AE5ACD4E0E9FE522DE7CE381E",  # mnkey
        "D6ECCF0AE5ACD4E0E92E522DE7C1381E",  # mkey
        "D6DCCF0AD5ACD4E0292E522DB7C1381E",  # realkey
        "D7DCCE1AD4AFDCE2393E5161CBDC4321",  # testkey
        "D7DBCE2AD4ADDCE1393E5521CBDC4321",  # utilkey
        "D7DBCE1AD4AFDCE1393E5121CBDC4321",  # R11s CPH1719 MSM8976, Plus
        "D6DCCF0AD5ACD4E0292E522DB7C1381E",  # R9s CPH1607 MSM8953, Plus, R11
        "D4D2CD61D4AFDCE13B5E01221BD14D20",  # FindX CPH1871 SDM845
        "261CC7131D7C1481294E532DB752381E",  # FindX
        "1CA21E12271335AE33AB81B2A7B14622",  # Realme 2 pro SDM660/MSM8976
        "D4D2CE11D4AFDCE13B3E0121CBD14D20",  # K1 SDM660/MSM8976
        "D6DCCF0AD5ACD4E0292E522DB7C1381E",  # RMX1921 Realme XT, RMX1851EX Realme Android 10
        "1c4c1ea3a12531ae491b21bb31613c11",  # Realme 3 Pro SDM710, X, 5 Pro, Q, RMX1921 Realme XT
        "1c4c1ea3a12531ae4a1b21bb31c13c21",  # Reno 10x zoom PCCM00 SDM855, CPH1921EX Reno 5G
        "1c4a11a3a12513ae441B23BB31513121",  # Reno 2 PCKM00 SDM730G
        "1c4a11a3a12589ae441a23bb31517733",  # Realme X2 SDM730G
        "1C4A11A3A22513AE541B53BB31513121",  # Realme 5 SDM665
        "2442CE821A4F352E33AE81B22BC1462E",  # R17 Pro SDM710
        "14C2CD6214CFDC2733AE81B22BC1462C",  # CPH1803 OppoA3s SDM450/MSM8953
        "1E38C1B72D522E29E0D4ACD50ACFDCD6",
        "12341EAAC4C123CE193556A1BBCC232D",
        "2143DCCB21513E39E1DCAFD41ACEDBD7",
        "2D23CCBBA1563519CE23C1C4AA1E3412",  # A77 CPH1715 MT6750T
        "172B3E14E46F3CE13E2B5121CBDC4321",  # Realme 1 MTK P60
        "acaa1e12a71431ce4a1b21bba1c1c6a2",  # Realme U1 RMX1831 MTK P70
        "acac1e13a72531ae4a1b22bb31c1cc22",  # Realme 3 RMX1825EX P70
        "1c4411a3a12533ae441b21bb31613c11",  # A1k CPH1923 MTK P22
        "1c4416a8a42717ae441523b336513121",  # Reno 3 PCRM00 MTK 1000L
        "ACAC1E13A12531AE4A1B21BB31C13C21",  # Reno, K3
        "ACAC1E13A72431AE4A1B22BBA1C1C6A2",  # A9
        "12cac11211aac3aea2658690122c1e81",  # A1,A83t
        "1CA21E12271435AE331B81BBA7C14612",  # CPH1909 OppoA5s MT6765
        "D6DCCF0AD5ACD4E0292E522DB7C1381E",  # RMX1992EX_11_OTA_1050
        #F3 Plus CPH1613 - MSM8976
    ]
    def __init__(self,file):
        'file : import ozip file'
        self.file=file
    def keytest(self,data):
        for key in self.keys:
            ctx = self.AES.new(self.binascii.unhexlify(key), self.AES.MODE_ECB)
            dat = ctx.decrypt(data)
            if (dat[0:4] == b'\x50\x4B\x03\x04'):
                print("找到正确的 AES key: " + key)
                return self.binascii.unhexlify(key)
            elif (dat[0:4] == b'\x41\x56\x42\x30'):
                print("找到正确的 AES key: " + key)
                return self.binascii.unhexlify(key)
            elif (dat[0:4] == b'\x41\x4E\x44\x52'):
                print("找到正确的 AES key: " + key)
                return self.binascii.unhexlify(key)
        return -1
    def del_rw(self,action, name, exc):
        os.chmod(name, self.stat.S_IWRITE)
        os.remove(name)
    def rmrf(self,path):
        if os.path.exists(path):
            if os.path.isfile(path):
                self.del_rw("", path, "")
            else:
                self.shutil.rmtree(path, onerror=self.del_rw)
    def decryptfile(self,key, rfilename):
        with open(rfilename,'rb') as rr:
            with open(rfilename+".tmp", 'wb') as wf:
                rr.seek(0x10)
                dsize = int(rr.read(0x10).replace(b"\x00", b"").decode('utf-8'), 10)
                rr.seek(0x1050)
                print("Decrypting " + rfilename)
                flen = os.stat(rfilename).st_size - 0x1050
                ctx = self.AES.new(key, self.AES.MODE_ECB)
                while (dsize > 0):
                    if flen > 0x4000:
                        size = 0x4000
                    else:
                        size = flen
                    data = rr.read(size)
                    if dsize < size:
                        size = dsize
                    if len(data) == 0:
                        break
                    dr = ctx.decrypt(data)
                    wf.write(dr[:size])
                    flen -= size
                    dsize -= size
        os.remove(rfilename)
        os.rename(rfilename+".tmp",rfilename)
    def mode2(self,filename):
        with open(filename, 'rb') as fr:
            magic = fr.read(12)
            if magic[:2] == b"PK":
                testkey = True
                with zipfile.ZipFile(sys.argv[1], 'r') as zipObj:
                    if os.path.exists('temp'):
                        self.rmrf('temp')
                    os.mkdir('temp')
                    if os.path.exists('out'):
                        self.rmrf('out')
                    os.mkdir('out')
                    print("Extracting " + sys.argv[1])
                    zipObj.extractall('temp')
                    for r, d, f in os.walk('temp'):
                        for file in f:
                            rfilename = os.path.join(r, file)
                            rbfilename = os.path.basename(rfilename)
                            wfilename = os.path.join("out", rbfilename)
                            with open(rfilename, 'rb') as rr:
                                magic = rr.read(12)
                                if (magic == b"OPPOENCRYPT!"):
                                    if testkey == True:
                                        with open(os.path.join("temp", "boot.img"), "rb") as rt:
                                            rt.seek(0x50)
                                            data = rt.read(16)
                                            key = self.keytest(data)
                                            if (key == -1):
                                                print("未知的AES密钥，请先从Recovery获取反向密钥！")
                                                return
                                        testkey = False
                                    with open(wfilename, 'wb') as wf:
                                        print("Decrypting " + rfilename)
                                        rr.seek(0x50)
                                        data = bytearray(rr.read())
                                        ctx = self.AES.new(key, self.AES.MODE_ECB)
                                        data[0:16] = ctx.decrypt(data[0:16])
                                        data[0x4050:0x4050 + 16] = ctx.decrypt(data[0x4050:0x4050 + 16])
                                        wf.write(data)
                                else:
                                    self.shutil.move(rfilename, wfilename)
                    self.rmrf('temp')
                    print("完成 ... 文件已解密到 \"out\" 目录 !!")
    def main(self):
        print("ozipdecrypt 1.1 (c) B.Kerler 2017-2020")
        filename=self.file
        with open(filename, 'rb') as fr:
            magic = fr.read(12)
            if (magic == b"OPPOENCRYPT!"):
                pk = False
            elif magic[:2] == b"PK":
                pk = True
            else:
                print("ozip has unknown magic, OPPOENCRYPT! expected !")
                return
            if pk == False:
                fr.seek(0x1050)
                data = fr.read(16)
                key = self.keytest(data)
                if (key == -1):
                    print("未知的AES密钥，请先从Recovery获取反向密钥！")
                    return
                ctx = self.AES.new(key, self.AES.MODE_ECB)
                filename = sys.argv[1][:-4] + "zip"
                with open(filename, 'wb') as wf:
                    fr.seek(0x1050)
                    print("解密中...")
                    while (True):
                        data = fr.read(16)
                        if len(data) == 0:
                            break
                        wf.write(ctx.decrypt(data))
                        data = fr.read(0x4000)
                        if len(data) == 0:
                            break
                        wf.write(data)
                print("完成!!")
            else:
                testkey = True
                filename = sys.argv[1]
                path = os.path.dirname(filename)
                outpath = os.path.join(path, "out")
                if os.path.exists(outpath):
                    self.shutil.rmtree(outpath)
                os.mkdir(outpath)
                with zipfile.ZipFile(filename, 'r') as zo:
                    clist = []
                    try:
                        if zo.extract('oppo_metadata', outpath):
                            with open(os.path.join(outpath, 'oppo_metadata')) as rt:
                                for line in rt:
                                    clist.append(line[:-1])
                    except:
                        print("Detected mode 2....")
                        self.mode2(filename)
                        exit(0)
                    if testkey:
                        fname = ''
                        if "firmware-update/vbmeta.img" in clist:
                            fname = os.path.join('firmware-update', 'vbmeta.img')
                        elif "vbmeta.img" in clist:
                            fname = 'vbmeta.img'
                        if fname != '':
                            if zo.extract(fname, outpath):
                                with open(os.path.join(outpath, fname), "rb") as rt:
                                    rt.seek(0x1050)
                                    data = rt.read(16)
                                    key = self.keytest(data)
                                    if (key == -1):
                                        print("未知的AES密钥，请先从Recovery获取反向密钥！")
                                        return
                                testkey = False
                        if testkey == True:
                            print("Unknown image, please report an issue with image name !")
                            exit(0)
                    for info in zo.infolist():
                        print("Extracting " + info.filename)
                        outfile = os.path.join(outpath, info.filename)
                        if not os.path.exists(outfile):
                            zo.extract(info.filename, outpath)
                        if len(clist) > 0:
                            if info.filename in clist:
                                self.decryptfile(key, outfile)
                        else:
                            magic = b''
                            with open(outfile, 'rb') as rr:
                                magic = rr.read(12)
                            if (magic == b"OPPOENCRYPT!"):
                                self.decryptfile(key, outfile)
                    print("完成 ... 解密的文件 :" + outpath)
class unpackrom():
    file=''
    unpacktodir=1
    def __init__(self,file,unpacktodir=1,check=0):
        '''file:inputfile unpacktodir 0/1 0:Only run onec ;1 only to system dir check:lib 0/1'''
        self.file=file
        self.unpacktodir=unpacktodir
        if check==1:
            try:import brotli,Crypto.Cipher,binascii,stat,docopt
            except:
                print('正在安装依赖...')
                os.system('pip3 install brotli Crypto binascii stat docopt')
    def samsumg_tar(self):
        import tarfile
        tar=tarfile.open(self.file)
        tar.extractall(path='samsungrom')
        tar.close()
        lz4install()
        if adbshellpyinformation.p=='Windows':
            os.system('for %%a in (samsungrom\\*.lz4) do lz4 -d %%a')
            os.system('for %%a in (samsungrom\\*.lz4) do del /f/s/q %%a')
        else:
            os.system('find ./samsungrom -name *.lz4  |xargs lz4 -d')
            os.system('find ./samsungrom -name *.lz4  |xargs rm -rf')
    def lg_kdz(self):
        pass
    def oppo_ozip(self):
        o=oppoozip(self.file)
        o.main()
    def unzip(self):
        info=rominformation(self.file)
        if info.flag==1:return
        if info.flag==2:
            #专属格式解包
            pass
        z=zipfile.ZipFile(self.file)
        z.extractall('rom')
        z.close()
        if self.unpacktodir==0:
            print('Done! 输出的到的目录: /rom')
            return
        else:pass
    def imgunpack(self,flag=1):
        '''flag: 1mount 2unmount Linux'''
        if adbshellpyinformation.p=='Linux':
            if flag==1:
                os.system('mkdir android-system-img')
                os.system('sudo mount %s android-system-img'%self.file)
                print('Done!: 挂载镜像到文件夹 android-system-img')
            if flag==2:
                os.system('sudo umount android-system-img')
                os.system('e2fsck -p -f '+self.file)
                os.system('resize2fs -M '+self.file)
                print('Done!: 保存的镜像 '+self.file)
        if adbshellpyinformation.p=='Windows':
            url='https://github.com/AEnjoy/adbshellpy/raw/master/Imgextractor.exe'
            if os.path.exists('Imgextractor.exe')==False:
                try:urllib.request.urlretrieve(url,'Imgextractor.exe')
                except:
                    print('E:下载失败!')
                    return
            os.system('Imgextractor '+self.file)
            print('Done!')
        
    def newdatunpack(self,TRANSFER_LIST_FILE='system.transfer.list', NEW_DATA_FILE='system.new.dat', OUTPUT_IMAGE_FILE='system.img'):
        #GitHub Paper: https://github.com/xpirt/sdat2img
        #====================================================
        #          FILE: sdat2img.py
        #       AUTHORS: xpirt - luxi78 - howellzhu
        #          DATE: 2018-10-27 10:33:21 CEST
        #       Chinese: 神郭
        #====================================================
        import errno
        __version__ = '1.2'
        print('sdat2img Version: {}\n'.format(__version__))
        if os.path.exists(NEW_DATA_FILE)==False:NEW_DATA_FILE=self.file
        def rangeset(src):
            src_set = src.split(',')
            num_set =  [int(item) for item in src_set]
            if len(num_set) != num_set[0]+1:
                print('以下数据分析到RangeSet时出错:\n {}'.format(src), file=sys.stderr)
                sys.exit(1)
            return tuple ([ (num_set[i], num_set[i+1]) for i in range(1, len(num_set), 2) ])
        def parse_transfer_list_file(path):
            trans_list = open(TRANSFER_LIST_FILE, 'r')
            # First line in transfer list is the version number
            version = int(trans_list.readline())
            # Second line in transfer list is the total number of blocks we expect to write
            new_blocks = int(trans_list.readline())
            if version >= 2:
                # Third line is how many stash entries are needed simultaneously
                trans_list.readline()
                # Fourth line is the maximum number of blocks that will be stashed simultaneously
                trans_list.readline()
            # Subsequent lines are all individual transfer commands
            commands = []
            for line in trans_list:
                line = line.split(' ')
                cmd = line[0]
                if cmd in ['erase', 'new', 'zero']:
                    commands.append([cmd, rangeset(line[1])])
                else:
                    # Skip lines starting with numbers, they are not commands anyway
                    if not cmd[0].isdigit():
                        print('命令 "{}" 无效.'.format(cmd), file=sys.stderr)
                        trans_list.close()
                        sys.exit(1)
            trans_list.close()
            return version, new_blocks, commands
        BLOCK_SIZE = 4096
        version, new_blocks, commands = parse_transfer_list_file(TRANSFER_LIST_FILE)
        if version == 1:print('Android Lollipop 5.0 检测到!\n')
        elif version == 2:print('Android Lollipop 5.1 检测到!\n')
        elif version == 3:print('Android Marshmallow 6.x 检测到!\n')
        elif version == 4:print('Android Nougat 7.x / Oreo 8.x 检测到!\n')
        else:print('未知的 Android 版本!\n')
        try:output_img = open(OUTPUT_IMAGE_FILE, 'wb')
        except IOError as e:
            if e.errno == errno.EEXIST:
                print('错误: 输出的文件 "{}" 已经存在'.format(e.filename), file=sys.stderr)
                print('移动它, 重命名它, 或选择一个不同的文件名.', file=sys.stderr)
                sys.exit(e.errno)
            else:raise
        new_data_file = open(NEW_DATA_FILE, 'rb')
        all_block_sets = [i for command in commands for i in command[1]]
        max_file_size = max(pair[1] for pair in all_block_sets)*BLOCK_SIZE
        for command in commands:
            if command[0] == 'new':
                for block in command[1]:
                    begin = block[0]
                    end = block[1]
                    block_count = end - begin
                    print('复制 {} 区段到位置 {}...'.format(block_count, begin))
                    # Position output file
                    output_img.seek(begin*BLOCK_SIZE)
                    # Copy one block at a time
                    while(block_count > 0):
                        output_img.write(new_data_file.read(BLOCK_SIZE))
                        block_count -= 1
            else:print('跳过命令 {}...'.format(command[0]))
        # Make file larger if necessary
        if(output_img.tell() < max_file_size):output_img.truncate(max_file_size)
        output_img.close()
        new_data_file.close()
        print('完成! 输出的镜像文件:  {}'.format(os.path.realpath(output_img.name)))            
    def brotli(self,INPUT_FILE='system.new.dat.br',OUTPUT_FILE='system.new.dat',flag=1):
        import brotli as b
        if flag==1:
            f=open(INPUT_FILE)
            f=b.decompress(f.read())
            ofile=open(OUTPUT_FILE, 'wb')
            os.write(ofile,f)
            f.close()
            ofile.close()
            sys.exit()
        if flag==2:
            f=open(INPUT_FILE)
            f=b.compress(f.read())
            ofile=open(OUTPUT_FILE, 'wb')
            os.write(ofile,f)
            f.close()
            ofile.close()
            sys.exit()
        print('参数无效!')
