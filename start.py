#!/usr/bin/python
# -*- coding: latin-1 -*-
from subprocess import call
import os
import sys

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

class download_all(object):
    def __init__(self):
        self.flag = 0
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        cls()
        x = """{}______                    _                 _    ___  _ _ 
|  _  \                  | |               | |  / _ \| | |
| | | |_____      ___ __ | | ___   __ _  __| | / /_\ \ | |
| | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` | |  _  | | |
| |/ / (_) \ V  V /| | | | | (_) | (_| | (_| | | | | | | |
|___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| \_| |_/_|_|
                                         {} v.0.0.1 {}       
        {}   https://github.com/byRo0t96 {}
            """.format(self.y, self.r, self.y, self.g, self.rr)
        cls()
        print (x)
        try:
            txtfile = sys.argv[1] #raw_input('Enter TXT file: ') #takes input from user
            os.system("chmod +x functions.sh")
            with open(txtfile,'r') as f:
                for line in f.readlines():
                    values = line.split("/")
                    user = str(values[0].replace("\r\n",""))
                    git = str(values[1].replace("\r\n",""))
                    gitclone = "./functions.sh %s %s"% (user,git)
                    rc = call(gitclone, shell=True)
        except:
            print('{}Usage:{} python start.py exemple.txt{}\n').format(self.r, self.y, self.rr)
            sys.exit()

download_all()
