from pyit.cop import IRawFileCop, Cop
from pyit.offence import Offence
from pyit.helpers import *

class SpaceIndentationCop(Cop):

    COP_CONFIG = {}

    __implements__ = [IRawFileCop]
    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'space_indentation_cop'

    def process_file(self, lines, filename):
        if not self.processable():
            return

        for i, line in enumerate(lines):
            line_ident = line.replace(line.lstrip(), '')

            if len(line_ident) % 4 != 0:
                off = Offence(
                    cop_name=self.name(),
                    location=(i + 1, 0),
                    message="Indentation is not multiple of four.",
                    filename=filename,
                    severity='convention'
                )
                self.offences.append(off)
