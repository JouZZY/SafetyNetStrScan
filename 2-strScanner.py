# coding:utf-8

import os

apkDir = './apps/'

apks = os.listdir(apkDir)
for apk in apks:
    # print(apk.split(".apk")[0])

    os.system('echo '+apk+' >> rslt.txt')
    ResultFile = os.system('apktool d '+apkDir+apk)
    os.system('echo decomp finish')
    # findstr /s safetynet %%i/*.smali >> test.txt
    # os.system('findstr /s safetynet '+ apk.split(".apk")[0] + '/*.smali >> rslt.txt')
    os.system('findstr /s BLUETOOTH '+ apk.split(".apk")[0] + '/AndroidManifest.xml >> rslt.txt')
    os.system('echo '+"\\n"+' >> rslt.txt')
    break
    
