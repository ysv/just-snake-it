
""" Class which receive package name and call code linting. """

from os import walk, mkdir
from os.path import isdir, join, splitext, abspath, split, dirname
from tokenize import tokenize
import time

from pyit.utils import COLORS, GREEN, YELLOW, RED
from pyit.cop import *

from pyit.cops.tab_indentation import TabIndentationCop
from pyit.cops.mixed_indentation import MixedIndentationCop
from pyit.cops.space_indentation import SpaceIndentationCop
from pyit.cops.line_length import LineLengthCop
from pyit.cops.binary_operator_line_brake import BinaryOperatorLineBrakeCop
from pyit.cops.blank_lines import BlankLinesCop
from pyit.cops.multiple_import import MultipleImport



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
        TabIndentationCop,
        MixedIndentationCop,
        SpaceIndentationCop,
        LineLengthCop,
        BinaryOperatorLineBrakeCop,
        BlankLinesCop,
        MultipleImport
    ]

    inspection_files = []
    config = dict()
    cops = []
    lint_result = {}

    def __init__(self, package, config):
        self.abs_path = abspath(package)
        if isdir(package):
            self.dir_path = self.abs_path
        else:
            self.dir_path = dirname(self.abs_path)

        self.inspection_files = get_files_in(self.abs_path)
        self.config = config
        for cop in self.REGISTERED_COPS:
            cop_name = cop.name()
            cop_conf = config.value('cops').get(cop_name, None)
            self.cops.append(cop(cop_conf))

    def lint(self):
        for cop in self.cops:
            for file in self.inspection_files:
                lint_result = self.lint_file(cop, file)
                if lint_result == -1:
                    formatted_str = COLORS[RED] + 'F'
                elif lint_result > 0:
                    formatted_str = COLORS[YELLOW] + '*'
                else:
                    formatted_str = COLORS[GREEN] + '.'
                print(formatted_str, end='')

    # TODO: Beautiful Exceptions (save skipped files).
    def lint_file(self, cop, file):
        if ITokenCop in cop.__implements__:
            try:
                readline = open(file, 'rb').__next__
                tokens = tokenize(readline)
                cop.process_tokens(tokens, file)
            except Exception as e:
                return -1
        if IRawFileCop in cop.__implements__:
            try:
                f = open(file, 'r')
                lines = f.read().splitlines()
                cop.process_file(lines, file)
            except Exception as e:
                return -1

        return len(cop.offences)

    def print_offences(self):
        for cop in self.cops:
            for off in cop.offences:
                print(off)

    def format(self):
        head, tail = split(self.dir_path)
        linted_dir = join(head, 'linted_' + str(int(time.time())))

        mkdir(linted_dir)

        for cop in self.cops:
            for file in self.inspection_files:
                if IFormatCop in cop.__implements__:
                    try:
                        readline = open(file, 'rb').__next__
                        tokens = tokenize(readline)
                        fixed_bytes = cop.fix_tokens(tokens, file)
                        outp_path = file.replace(self.dir_path, linted_dir)
                        output_file = open(outp_path, 'w')
                        output_file.write(fixed_bytes.decode("utf-8"))
                    except Exception as e:
                        print(e)
                        continue
