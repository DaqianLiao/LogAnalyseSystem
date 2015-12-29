#-*- coding:utf-8 -*-
import os.path

def InputTxtFilePath():
    log_path =  input('enter the txt file path:')
##    log_path = ''
    return log_path

def IsTxtFile(filename):
    boolflag = False
    fileflag = os.path.splitext(filename)[1]
    if fileflag == '.txt':
        boolflag = True
    return boolflag

def SetFliePath(dirpath, filename):
    filepath = os.path.join(dirpath, filename)
    return filepath    

def GetTxtContent(txtfilepath):
    file = open(txtfilepath,'r')
    txtfile = file.readlines()
    file.close()
    return txtfile

def SplitByenter(liststring):
    listcontent = liststring.split('\t')
    return listcontent

def DelEnterInList(stringlist):
    if '\n' in stringlist:
        stringlist.remove('\n')
    return stringlist

def GetAllSNByTxt(txtfile):
    SNlist=[]
    for index in txtfile:
        listcontent = SplitByenter(index)
        listcontent = DelEnterInList(listcontent)
        snstring = listcontent[0]
        if not snstring in SNlist:
            SNlist.append(snstring)
    return SNlist

def SnInit():
    snlist = ['skych5513m0f5wxe','skych5813sb8f5g1','skych5513kejx1q8','skych5313exsun9n',
              'skyc40r136up689a','skych5813t747mbm','skych5513m0f67nb','skych5713r7uzzka','skych5513kejx1q8',
              'skych5813sb8f5g1','skych5713r7v0mxp','skych5513kejy547','skych5813sb8f125','skych5513m0f6r91']

    return snlist


def IsContent(txtfile,snlist):
    findanswer = []
    for index in txtfile:
        listcontent = SplitByenter(index)
        if listcontent[0] in snlist:
            print(index)
            findanswer.append(index)
    return findanswer
            

def GetFunctionDepart(txtfile):
    unremalloc = 'unremalloc_sim'
    unremalloccount = 0
    unmodelrestart = 'model_restart'
    unmodelrestartcount = 0
    vsimokdatafail = 'VSIM_ok_but_data_fail'
    vsimokdatafailcount = 0
    pushremall = 'all_ok_but_pushremalloc'
    pushremallcount = 0
    dppass = 'DP_Pass'
    dppasscount = 0
    unstrengthfail = 'Vsim_strength_fail'
    unstrengthfailcount = 0
    
    remalloc = 'remalloc_sim'
    remalloccount = 0
    modelrestart = 'model_restart'
    modelrestartcount = 0
    fightdata = 'fight_model_connect_data'
    fightdatacount = 0
    simbug = 'SIM_Bug'
    simbugcount = 0
    tokenexception = 'token_exception'
    tokenexceptioncount = 0
    strengthfail = 'Vsim_strength_fail'
    strengthfailcount = 0
    unknown = 'unknown'
    unknowncount = 0
    no_subscription = 'no_subscription'
    no_subscriptioncount = 0
    
    for index in txtfile:
        listcontent = SplitByenter(index)
        if unremalloc == listcontent[3]:
            unremalloccount = unremalloccount +1
            if unmodelrestart == listcontent[4]:
                unmodelrestartcount = unmodelrestartcount + 1
            elif vsimokdatafail == listcontent[4]:
                vsimokdatafailcount = vsimokdatafailcount + 1
            elif pushremall == listcontent[4]:
                pushremallcount = pushremallcount + 1
            elif dppass == listcontent[4]:
                dppasscount = dppasscount + 1
            elif unstrengthfail == listcontent[4]:
                unstrengthfailcount = unstrengthfailcount + 1
        elif remalloc == listcontent[3]:
            remalloccount = remalloccount +1
            if modelrestart == listcontent[4]:
                modelrestartcount = modelrestartcount + 1
            elif fightdata == listcontent[4]:
                fightdatacount = fightdatacount + 1
            elif simbug == listcontent[4]:
                simbugcount = simbugcount + 1
            elif tokenexception == listcontent[4]:
                tokenexceptioncount = tokenexceptioncount + 1
            elif strengthfail == listcontent[4]:
                strengthfailcount = strengthfailcount + 1
            elif unknown == listcontent[4]:
                unknowncount = unknowncount + 1
            elif no_subscription == listcontent[4]:
                no_subscriptioncount = no_subscriptioncount + 1
    allcount = unremalloccount + remalloccount
    string = unremalloc + ' = %s ' + unmodelrestart + ' = %s ' + vsimokdatafail + ' = %s ' + pushremall + ' = %s ' + dppass + ' = %s ' + unstrengthfail + ' = %s '
    print(string %(unremalloccount, unmodelrestartcount, vsimokdatafailcount ,pushremallcount ,dppasscount ,unstrengthfailcount))
    string = remalloc + ' = %s ' + modelrestart + ' = %s ' + fightdata + ' = %s ' + simbug + ' = %s ' + tokenexception + ' = %s ' + strengthfail + ' = %s ' + unknown + ' = %s ' + no_subscription + ' = %s'
    print(string %(remalloccount, modelrestartcount, fightdatacount, simbugcount, tokenexceptioncount, strengthfailcount,unknowncount,no_subscriptioncount))
    return unremalloccount, remalloccount, allcount            

        
def GetAllAnalyse(log_path,count):
    for dirpath, dirnames, filenames in os.walk(log_path):
        for filename in filenames:
            if IsTxtFile(filename):
                filepath = SetFliePath(dirpath, filename)
                txtfile = GetTxtContent(filepath)
                SNlist = GetAllSNByTxt(txtfile)
                print('the rate of the exception device: ', len(SNlist)/count)
                unremalloccount, remalloccount, allcount = GetFunctionDepart(txtfile)
                print('unremalloccount = [%s], remalloccount = [%s], allcount = [%s]' %(unremalloccount, remalloccount, allcount))
##                snlist = SnInit()
##                findanswer = IsContent(txtfile,snlist)

                
##                
##log_path = InputTxtFilePath()             
##GetAllAnalyse(log_path)       
    

    


