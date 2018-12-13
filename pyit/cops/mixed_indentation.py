from pyit.cop import IRawFileCop, Cop
from pyit.offence import Offence


class MixedIndentationCop(Cop):

    COP_CONFIG = {}

    TAB_IDENT = '\t'
    SPACE_IDENT = ' ' * 4

    INDENT_TO_NAME = {
        TAB_IDENT: 'tab',
        SPACE_IDENT: 'space'
    }

    __implements__ = [IRawFileCop]
    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'mixed_indentation_cop'

    def process_file(self, lines, filename):
        if not self.processable():
            return

        # First is allowed and second is not allowed for this file.
        file_indent = (None, None)

        for index, line in enumerate(lines):
            if not (line.startswith(self.SPACE_IDENT) or
                    line.startswith(self.TAB_IDENT)):
                continue

            line_ident = line.replace(line.lstrip(), '')

            # If there is no file indentation detected yet.
            if file_indent[0] is None:
                tmp = (self.SPACE_IDENT, self.TAB_IDENT)
                if line_ident.startswith(self.TAB_IDENT):
                    tmp = tuple(reversed(tmp))

                file_indent = tmp

            if file_indent[1] in line_ident:
                wrong_indent_index = line_ident.find(file_indent[1])
                message = 'Inconsistent indentation. Previous line used ' \
                    + self.INDENT_TO_NAME[file_indent[0]] + ' current line uses ' \
                    + self.INDENT_TO_NAME[file_indent[1]] + '.'
                off = Offence(
                    cop_name=self.name(),
                    location=(index + 1, wrong_indent_index),
                    filename=filename,
                    message=message,
                    severity='convention'
                )
                self.offences.append(off)
