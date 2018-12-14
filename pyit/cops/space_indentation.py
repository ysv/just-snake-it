from pyit.cop import ITokenCop, Cop
from pyit.offence import Offence
from token import *


class SpaceIndentationCop(Cop):

    COP_CONFIG = {}
    OPEN_BRACKETS = {
        '(': LPAR,
        '[': LSQB,
        '{': LBRACE,
    }

    CLOSE_BRACKETS = {
        '}': RBRACE,
        ']': RSQB,
        ')': RPAR,
    }

    __implements__ = [ITokenCop]
    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'space_indentation_cop'

    def process_tokens(self, tokens, filename):
        if not self.processable():
            return

        opened_brackets = 0

        for i, tkn in enumerate(tokens):
            if tkn.type in self.CLOSE_BRACKETS.values():
                opened_brackets -= 1

            if tkn.type in self.OPEN_BRACKETS.values():
                opened_brackets += 1

            if tkn.type == INDENT:
                if tkn.string.startswith(' ') and \
                        len(tkn.string) % 4 != 0 and \
                        opened_brackets == 0:
                    off = Offence(
                        cop_name=self.name(),
                        location=tkn.start,
                        message="Indentation is not multiple of four.",
                        filename=filename,
                        severity='convention'
                    )
                    self.offences.append(off)
