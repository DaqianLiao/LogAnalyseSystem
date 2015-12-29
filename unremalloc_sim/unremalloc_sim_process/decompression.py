#-*-coding:utf-8 -*-
import gzip
import os.path
import time

#获取gz压缩文件中源文件的名称  
def get_decompress_file_name(filepath):
    timeform = '%Y%m%d'
    timestr = time.localtime()
    timestr = time.strftime(timeform, timestr)
    filenames = 'simo_log_' + timestr + '.txt'
    return filenames

#解压单个gz文件
def untar(filepath , txtfilename):
    gz_file_isok = gz_isok_to_decompress(filepath)
    if gz_file_isok:
       file = gzip.open(filepath)
       filedata = file.read()
       outfilexls = open(txtfilename, 'ab')
       outfilexls.write(filedata)
       outfilexls.close
       file.close
    else:
        print(filepath + 'That gz_file is broken!')

#gz文件校验
def gz_isok_to_decompress(filepath):
    bool_value = True
    try :
        file = gzip.open(filepath)
        file.read()
        file.close
    except Exception:
        bool_value = False
    return bool_value

#解压指定路径下的所有文件
def  decompression_gz_all(log_path):
    for dirpath, dirnames, filenames in os.walk(log_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.gz':
               gzfilepath = os.path.join(dirpath, filename)
               txtfile = get_decompress_file_name(gzfilepath)
               txtfilepath = os.path.join(dirpath, txtfile)
               untar(gzfilepath,txtfilepath)
        print(dirpath + ': decompress gz file successfully ! ')
        print('================================================================')
#删除单个文件          
def delfile(fname):
    if os.path.exists(fname):
        os.remove(fname)
#多个txt文件组合成一个大txt文件     
def adddatatotxt(filepath , txtname):
    filedata= open(filepath,'rb')
    data=filedata.read()
    txtfile = open(txtname,'ab')
    txtfile.write(data)
    filedata.close
    txtfile.close         
               
def decompression_main(log_path):
    decompression_gz_all(log_path)
      



