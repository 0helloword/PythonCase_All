#coding=utf-8
import os

def kill_process(name):
    '''
              杀死进程
    '''
    os.system("taskkill /f /im "+ name +" >nul 2>nul")

kill_process("firefox.exe")