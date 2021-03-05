from os import listdir
from os.path import isfile, join, basename
import shutil
import sys
import getopt


# def runScript():
#     onlyfiles = [f for f in listdir("G:\\") if isfile(join("G:\\", f))]
#     print(onlyfiles)

def get_list_dir(path):
    directories = listdir(path)
    file_list = []
    for dirc in directories:
        if isfile(join(path, dirc)) is not True:
            file_list.extend(get_list_dir(join(path, dirc)))
        else:
            file_list.append(join(path, dirc))
    return file_list


def move_dir(src, dest):
    files = get_list_dir(src)
    if len(files) != 0:
        for file in files:
            try:
                shutil.move(file, join(dest, basename(file)))
            except shutil.Error as err:
                print(str(err))


def parse_command_line(argv):
    short_options = "hs:d:"
    long_options = ["help", "source", "destination"]
    try:
        arguments, values = getopt.getopt(argv, short_options, long_options)
        return arguments
    except getopt.error as err:
        print(str(err))
        sys.exit(2)


def command_line_switch(arguments):
    src, dest = '', ''
    for current_arguments, current_value in arguments:
        if current_arguments in ("-h", "--help"):
            print("help")
        elif current_arguments in ("-s", "--source"):
            src = current_value
        elif current_arguments in ("-d", "destination"):
            dest = current_value
    move_dir(src, dest)


def main():
    arguments = parse_command_line(sys.argv[1:])
    command_line_switch(arguments)
    print("done!!")


if __name__ == "__main__":
    main()
