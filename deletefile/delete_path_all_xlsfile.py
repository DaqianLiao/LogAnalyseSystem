import gzip
import os.path

#解压指定路径下的所有文件
def  delete_xls_all(log_path):
    for dirpath, dirnames, filenames in os.walk(log_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.xls':
               filepath = os.path.join(dirpath, filename)
               delfile(filepath) # 删除文件

#删除单个文件          
def delfile(fname):
    if os.path.exists(fname):
        os.remove(fname)
               
def delxlsfilemain(log_path):
    delete_xls_all(log_path)
              



