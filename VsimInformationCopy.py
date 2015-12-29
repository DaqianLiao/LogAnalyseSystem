import shutil
import os.path
import time

def TimeStringForm():
    timeform = '%Y%m%d%X'
    LocalTime = time.localtime()
    TimeFormString = time.strftime(timeform, LocalTime)
    TimeFormString = TimeFormString.replace(':', '')
    return TimeFormString

def TargetFolder(targetpath, outputname):
    targetfile = os.path.join(targetpath, outputname)
    return targetfile
  
def InitFolder(inittpath, filename):
    initfile = os.path.join(inittpath, filename)
    return initfile

def TagetFileName(filename, count):
    outputfilename = filename[:-4] + TimeStringForm() + '_' + str(count) + '.xls'
    return outputfilename

def NewFolder(targetpath,datetime):
##    dateinit = GetForeTime()
    targetpath = os.path.join(targetpath, datetime)
    return targetpath

def CalculateInfo(log_path, datetime):
##    targetpathinit = 'd:\\LogAnalyse'
    targetpathinit = '/tem/LogAnalyse'
    targetpath = NewFolder(targetpathinit,datetime)
    if not os.path.exists(targetpath):
       os.makedirs(targetpath)
    filekey = 'answer_log_analyse'
    filecount = 0  # #统计文件个数
    for dirpath, dirnames, filenames in os.walk(log_path):
        for filename in filenames:
            if filekey in filename:                
                filecount = filecount + 1
                initfile = InitFolder(dirpath, filename)
                outputfilename = TagetFileName(filename, filecount)
                targetfile = TargetFolder(targetpath, outputfilename)
                shutil.copy(initfile, targetfile)
                ##删除源文件
                os.remove(initfile)  
    mark = 'analize path_file ' + dirpath + ' complete at time:' + TimeStringForm()
    print(mark)
    return targetpath

