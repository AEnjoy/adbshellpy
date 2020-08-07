#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   adbshellpy_libunpakrom
#       By : 神郭
#  Version : Sub
import os,zipfile,urllib.request,argparse

def download():
    print('正在下载libunpakrom')
    url='https://hub.fastgit.org/AEnjoy/unpackandroidrom/archive/master.zip'
    urllib.request.urlretrieve(url,'master.zip')
    z=zipfile.ZipFile('master.zip')
    z.extractall()
    z.close()
    os.remove('master.zip')
    os.rename('unpackandroidrom-master','libromparse')
    print('初始化完成!')

def main(args=None):
    if os.path.exists('libromparse/main.py'):
        sys.path.append(os.path.join(sys.path[0], "libromparse"))
        try:
            import main
            main.main(args)
            return
        except ImportError:
            print('初始化失败?请重新安装libunpakrom.')
    print('''
    **********************************libunpakrom*****************************************
    *                           Android ROM 智能处理工具箱 Sub版本                         *
    *       支持市面上绝大部分Android手机的ROM解包,未来更新后还将支持ROM打包等操作         *
    *       功能:                                                                         *
    *                     ①OPPO OZIP解密                                                  *
    *                     ②Android O+ A/B分区(System As Root) payload.bin 解包            *
    *                     ③Android Q+ 真(假)动态分区payload.bin解包                        *
    *                     ④Android L+ .new.dat, .new.dat.br 转换img                       *
    *                     ⑤Android L+ 分区.img解包                                        *
    *                     ⑥常规解包,卡刷包解包.                                            *
    *                     ⑦部分ROM卡刷包支持直接读取ROM信息                                 *
    *                     ⑧Samsung odin .tar.md5 文件解包/获取ROM信息                      *
    *                      (仅官方.tar.md5文件支持) 解包.lz4→.img                          *
    *                     ⑨LG KDZ / DZ 文件解包                                           *
    *                     ⑩.tar线刷包解包                                                 *
    *       支持文件格式:                                                                 *
    *                     .img/.zip/.tar/.tar.gz/.tar.md5/.new.dat/.new.dat.br/          *
    *                     .kdz/.dz/.ozip/payload.bin                                     *
    *       项目地址:      https://github.com/AEnjoy/unpackandroidrom                     *
    *                                                                                    *
    **********************************libunpakrom*****************************************
    ''')
    input('按Enter键初始化libunpakrom')
    download()
    a=input('是否进入libunpakrom?y/n[默认y]>>>')
    if a=='y' or a=='':main()
    else:input('按Enter键退出...')
def parseArgs():
    parser = argparse.ArgumentParser(description='ROM智能处理工具箱')
    parser.add_argument('-f', '--file', help='欲解包的ROM文件', action='store', required=False, dest='file')
    parser.add_argument("-t", "--type", type=str, choices=['kdz', 'dz', 'samsumgodin','abota','flashable','ozip'], help="强制指定输入的文件ROM的类型", required=False)
    return parser.parse_args()    
if __name__ == "__main__":
    args=parseArgs()
    main(args)
