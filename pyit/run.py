
""" Class which receive package name and call code linting. """

from os import walk
from os.path import isdir, join, splitext, abspath
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP

from pyit.cop import *
from pyit.cops.tab_indentation import TabIndentationCop


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
    REGISTERED_COPS = [
        TabIndentationCop
    ]

    inspection_files = []
    config = dict()
    cops = []
    lint_result = {}

    def __init__(self, package, config):
        abs_path = abspath(package)
        self.inspection_files = get_files_in(abs_path)
        self.config = config
        for cop in self.REGISTERED_COPS:
            cop_name = cop.name()
            cop_conf = config.value('cops').get(cop_name, None)
            self.cops.append(cop(cop_conf))

    def lint(self):
        for cop in self.cops:
            for file in self.inspection_files:
                self.lint_file(cop, file)
                import code
                code.interact(local=dict(globals(), **locals()))

    def lint_file(self, cop, file):
        if ITokenCop in cop.__implements__:
            readline = open(file, 'rb').__next__
            tokens = tokenize(readline)
            cop.process_tokens(tokens, file)
        if IRawFileCop in cop.__implements__:
            f = open(file, 'r')
            lines = f.read().splitlines()
            cop.process_file(lines, file)

    def print_offences(self):
        for cop in self.cops:
            for off in cop.offences:
                print(off)
