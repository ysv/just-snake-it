
""" Class which receive package path and call code linting. """

from os import walk
from os import listdir
from os.path import *


def get_files_in(root, extension='.py'):
    file_pathes = []
    if isdir(root):
        for (dirpath, dirnames, filenames) in walk(root):
            for file in filenames:
                file_pathes.append(join(dirpath, file))
    else:
        file_pathes.append(root)

    return [file for file in file_pathes if splitext(file)[1] == extension]


class Run:
    inspection_files = []

    def __init__(self, package):
        abs_path = abspath(package)
        inspection_files = get_files_in(abs_path)
        print(inspection_files)


Run('../bin/pyit')