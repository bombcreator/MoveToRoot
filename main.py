from os import listdir
from os.path import isfile,join,basename
import shutil


# def runScript():
#     onlyfiles = [f for f in listdir("G:\\") if isfile(join("G:\\", f))]
#     print(onlyfiles)

def get_list_dir(path):
    directories  = listdir(path)
    file_list = []
    for dir in directories:
        if isfile(join(path,dir)) is not True:
            file_list.extend(get_list_dir(join(path,dir)))
        else:
            file_list.append(join(path,dir))
    return file_list
    





def main():
    files = get_list_dir("G:\\ModabberDMS\\bin\\Debug")
    if len(files) != 0:
        for file in files:
            shutil.move(file,join("G:\\ModabberDMS\\bin\\",basename(file)))
    print("done")


if __name__ == "__main__":
    main()




