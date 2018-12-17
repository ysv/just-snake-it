from pyit.cop import ITokenCop, Cop
from pyit.offence import Offence
from pyit.utils import token_line_indent, is_first_token_except_indent
from token import ENCODING, DEDENT, COMMENT


class BlankLinesCop(Cop):

    COP_CONFIG = {
        'top_level_blanklines': 2,
        'nested_level_blanklines': 1,
        'logical_blanklines': 1
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

    def logical_blanklines(self):
        return self.cop_conf['logical_blanklines']

    def process_tokens(self, tokens, filename):
        if not self.processable():
            return

        # Amount of blank lines in a row before current token.
        blank_lines = 0
        was_class_or_def = False

        # TODO: split into methods.
        for tkn in tokens:
            if tkn.line == '\n':
                blank_lines += 1
                was_class_or_def = False
                continue

            # Skip:
            #   - not first tokens in line except indent.
            #   - encoding token.
            #   - dedent.
            #   - @something.
            #   - comments.
            if not is_first_token_except_indent(tkn) \
                    or tkn.type == ENCODING \
                    or tkn.type == DEDENT \
                    or tkn.string == '@'\
                    or tkn.type == COMMENT:
                continue

            if tkn.string not in self.NEEDS_BLANK_LINES_OPER:
                # If there was 0 or 1 blank line it's okay.
                if blank_lines <= self.logical_blanklines():
                    blank_lines = 0
                else:
                    msg = "Extra " + str(blank_lines - self.logical_blanklines()) \
                          + " logical blank line found."
                    off = Offence(
                        cop_name=self.name(),
                        location=tkn.start,
                        message=msg,
                        severity='convention',
                        filename=filename
                    )
                    blank_lines = 0
                    self.offences.append(off)
                was_class_or_def = False
                continue

            # Otherwise we have 'def' or 'class' token.
            token_indent = token_line_indent(tkn)

            if token_indent == '':
                expected_blanklines = self.top_level_blanklines()
            else:
                expected_blanklines = self.nested_level_blanklines()

            if blank_lines != expected_blanklines \
                    and tkn.start[0] not in [1, 2] \
                    and not was_class_or_def:
                msg = "Expected " + str(expected_blanklines) \
                      + " but found " + str(blank_lines) + '.'
                off = Offence(
                    cop_name=self.name(),
                    location=tkn.start,
                    message=msg,
                    severity='convention',
                    filename=filename
                )
                self.offences.append(off)

            was_class_or_def = True
            blank_lines = 0
