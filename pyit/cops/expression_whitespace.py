from pyit.cop import IRawFileCop, Cop, IFormatCop
from tokenize import tokenize, untokenize
from pyit.offence import Offence
from io import BytesIO
import re


class ExpressionWhitespace(Cop):

    COP_CONFIG = {}
    __implements__ = [IFormatCop]

    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'import_cop'

    def process_file(self, lines, filename):
        pass

    def fix_format(self, lines, filename):

        mid_res = self.fix_brackets(lines)
        # import code
        # code.interact(local=dict(globals(), **locals()))

        return mid_res

    def fix_brackets(self, file):
        new_lines = []
        for line in file:
            # Fix Brackets.
            line = re.sub(r'.+\s+', ' ', line)
            line = re.sub(r'\(\s+', '(', line)
            line = re.sub(r'\s+\)', ')', line)

            line = re.sub(r'\[\s+', '(', line)
            line = re.sub(r'\s+\]', ')', line)

            line = re.sub(r'\s+:', ':', line)
            new_lines.append(line)

        return new_lines

