
""" Class which receive package name and call code linting. """

from os import walk
from os.path import isdir, join, splitext, abspath


def get_files_in(root, extension='.py'):
    file_paths = []
    if isdir(root):
        for (dirpath, dirnames, filenames) in walk(root):
            for file in filenames:
                file_paths.append(join(dirpath, file))
    else:
        file_paths.append(root)

    return [file for file in file_paths if splitext(file)[1] == extension]


class Run:
    inspection_files = []

    def __init__(self, package):
        abs_path = abspath(package)
        self.inspection_files = get_files_in(abs_path)

