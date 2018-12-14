from pyit.cop import ITokenCop, Cop
from pyit.offence import Offence
from pyit.utils import token_line_indent


class BlankLinesCop(Cop):

    COP_CONFIG = {
        'top_level_blanklines': 2,
        'nested_level_blanklines': 1
    }

    NEEDS_BLANK_LINES_OPER = [
        'def', 'class'
    ]

    __implements__ = [ITokenCop]
    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'blank_lines_cop'

    def top_level_blanklines(self):
        return self.cop_conf['top_level_blanklines']

    def nested_level_blanklines(self):
        return self.cop_conf['nested_level_blanklines']

    def process_tokens(self, tokens, filename):
        if not self.processable():
            return

        # Amount of blank lines in a row before current token.
        blank_lines = 0

        # Amount of blank lines expected before next token.
        # expected_blank_lines = 0

        # TODO: split into methods.
        for tkn in tokens:
            if tkn.line == '\n':
                blank_lines += 1
                continue

            if tkn.string not in self.NEEDS_BLANK_LINES_OPER:
                print(tkn)
                print('blanks=', blank_lines)
                # If there was 0 or 1 blank line it's okay.
                if blank_lines <= 1:
                    blank_lines = 0
                    continue
                else:
                    blank_lines = 0
                    off = Offence(
                        cop_name=self.name(),
                        location=tkn.start,
                        message="Extra blank lines found",
                        severity='convention',
                        filename=filename
                    )
                    self.offences.append(off)
                    continue

            # Otherwise we have 'def' or 'class' token.
            token_indent = token_line_indent(tkn)

            # If top level indent required.
            if token_indent == '':
                expected_blanklines = self.top_level_blanklines()
            else:
                expected_blanklines = self.nested_level_blanklines()

            if blank_lines != expected_blanklines:
                msg = "Expected " + str(expected_blanklines) + " but found " + str(blank_lines)
                off = Offence(
                    cop_name=self.name(),
                    location=tkn.start,
                    message=msg,
                    severity='convention',
                    filename=filename
                )
                self.offences.append(off)

            blank_lines = 0
