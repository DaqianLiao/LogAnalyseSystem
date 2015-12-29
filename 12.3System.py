# -*- coding:utf-8 -*-
import datetime
import os
import time
import LogSystem
import VsimInformationCopy
import deletefile.deltxtandtxt
import VsimLogCalculate
import TxtAnswerAnalyse

##获取当前时间的前一天，也可以是前N天
def GetForeTime():
    TimeForm = '%Y-%m-%d'
    nowtime = datetime.datetime.now()
    yesterday = nowtime + datetime.timedelta(days = -3)
    Timestr = datetime.datetime.strftime(yesterday, TimeForm)
    return Timestr

##判断是否是符合要求的时间格式，例如2015-01-01
def TimeStrCheck(timestr):
    checkbool = False
    TimeLen = 10
    judgement = '-'
    if len(timestr) == TimeLen and judgement in timestr:
        strlist = timestr.split(judgement)
        checkbool = ListElementIsDigit(strlist)
    return checkbool

##判断list中的元素是否都是数字
def ListElementIsDigit(strlist):
    checkbool = False
    if strlist:
        for strindex in strlist:
            if strindex.isdigit:
                checkbool = True
    return checkbool

def SetSplitStr():
##    splitstr = '\\' ## For PC
    splitstr = '/'## For Linux
    return splitstr
	
def CountNum(count, logpath):
    output = count
    pathlist = logpath.split(SetSplitStr())
    if IsSN(pathlist[-2]):
        output = count + 1
    return output

def GetSNandTime(logpath):
    pathlist = logpath.split(SetSplitStr())
    sntimepath = os.path.join(pathlist[-2],pathlist[-1])
    return sntimepath

def GetSN(logpath):
    pathlist = logpath.split(SetSplitStr())
    if IsSN(pathlist[-1]):
       SNstring = pathlist[-1]
    else:
       SNstring = ''
    return SNstring	

def IsSN(sn):
    snflag = 'sky'
    flag = False
    if snflag in sn and len(sn) ==16:
        flag = True
    return flag

def IsMatchTime(dirpaths):
    flag = False
    splitList = dirpaths.split(SetSplitStr())
    strname = splitList[-1]
    if TimeStrCheck(strname):
        if strname == GetForeTime():
            flag = True
    return flag
	
def RightDateAnalyseSystem():
##    log_path = input('enter the log path:')
    log_path = '/log/TRACE_SERVER/Log/3Gmate+/4.4.12.3'
    count = 0
    dailycount = 0
    SNlist = []
    SNPathlist = []
    if os.path.exists(log_path):
        for dirpaths, dirnames, filenames in os.walk(log_path):
            SNstring = GetSN(dirpaths)
            if not SNstring == '':
               SNlist.append(SNstring)
            if IsMatchTime(dirpaths):
               sntimepath = GetSNandTime(dirpaths)
               if not sntimepath in SNPathlist:
                  SNPathlist.append(sntimepath)
                  dailycount = CountNum(dailycount, dirpaths)
                  deletefile.deltxtandtxt.DelXlsAndTxt(dirpaths)
                  LogSystem.log_system_main(dirpaths)
                  ##分析结果文件复制到指定文件夹
                  targetpath = VsimInformationCopy.CalculateInfo(dirpaths, GetForeTime())
                  ##删除缓存TXT文件和XLS文件
                  deletefile.deltxtandtxt.DelXlsAndTxt(dirpaths)
                  ##整理分析结果，生成TXT格式结果文件
                  VsimLogCalculate.LogFileAnalyse(targetpath, GetForeTime())
        TxtAnswerAnalyse.GetAllAnalyse(targetpath,len(SNlist))
        print('There are %s SN device!' %len(SNlist))
        print('There are %s device used today!' %dailycount)
        print('LogAnalyseDone') 
    else:
        print('that path does not exist!!!')
        RightDateAnalyseSystem()
            
if __name__=="__main__":
    timestart = time.time()
    RightDateAnalyseSystem()
    timestop = time.time()
    timedeta = str(int(timestop) - int(timestart))
    print('This spends ' + timedeta + ' seconds!!')            
            
