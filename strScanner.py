# coding:utf-8

import os
import subprocess
from sys import stdin
import time
import signal
import win32api
import win32con


apktoolpath=r"D:\Academic\AndroidSec\ApkTool\installer\apktool.bat"

apkDir = './apps/'

apks = os.listdir(apkDir)
for apk in apks:
    # print(apk.split(".apk")[0])

    os.system('echo '+apk+' >> rslt.txt')
    # ResultFile = os.system('apktool d -f '+apkDir+apk)
    # p = subprocess.Popen('apktool d '+apkDir+apk)
    # process = subprocess.Popen(apktoolpath+r" d -f "+apkDir+apk, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # process = subprocess.Popen(apktoolpath+r" d -f "+apkDir+apk, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    process = subprocess.Popen(apktoolpath+r" d -f "+apkDir+apk)
    
    # while 1:
    #     print(process.pid,'input a')
    #     process.communicate(input="a",timeout=150)
    #     time.sleep(10) 

    # while 1: 
    #     line = process.stdout.readline()
    #     print(line)
    
    i=0
    while 1:  
        i=i+1   
        ret1 = subprocess.Popen.poll(process)     
        if ret1 == 0:
            print(process.pid,'finish')    
            break    
        elif ret1 is None:
            print(process.pid,'not finish',i)

            # process.stdin.write("a")

            # instr = "a"
            # process.stdin.write('{}\n'.format(instr).encode('utf-8'))
            
            win32api.keybd_event(65,0,0,0);

            # process.send_signal(signal.SIGINT)
            # process.communicate(input="a")
            # line = process.stdout.readline()
            # print(line)

            # win32api.keybd_event(65,0,0,0);

            time.sleep(1) 
        else:
            # print(sub2.pid,'term')
            print(process.pid,'term')
            break    
    print("apk tools end")  
    
    os.system('echo decomp finish')
    # findstr /s safetynet %%i/*.smali >> test.txt
    # os.system('findstr /s safetynet '+ apk.split(".apk")[0] + '/*.smali >> rslt.txt')
    os.system('findstr /s BLUETOOTH '+ apk.split(".apk")[0] + '/AndroidManifest.xml >> rslt.txt')
    os.system('echo '+"\\n"+' >> rslt.txt')
    break
    
