from pyit.cop import ITokenCop, Cop
from pyit.offence import Offence
from pyit.helpers import *
from token import *


class BinaryOperatorLineBrakeCop(Cop):

    COP_CONFIG = {}
    __implements__ = [ITokenCop]

    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'binary_operator_line_brake_cop'

    def process_tokens(self, tokens, filename):
        if not self.processable():
            return

        for tkn in tokens:
            if tkn.type != OP:
                continue

            if tkn.string in binary_operator_keys():
                nxt_tkn = next(iter(tokens), None)
                if nxt_tkn is not None and nxt_tkn.string == '\n':
                    if tkn.string == '*' and \
                            (tkn.line.startswith('import')
                             or tkn.line.startswith('from')):
                        continue
                    off = Offence(
                        cop_name=self.name(),
                        location=tkn.start,
                        message="Line brake after binary operator '" + str(tkn.string) + "' detected.",
                        filename=filename,
                        severity='refactor'
                    )
                    self.offences.append(off)
