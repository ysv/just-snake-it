from pyit.cop import IRawFileCop, Cop
from pyit.offence import Offence


class TabIndentationCop(Cop):
    TAB_INDENT = '\t'

    __implements__ = [IRawFileCop]
    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = self.DEFAULT_CONFIG
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'tab_indentation_cop'

    def process_file(self, lines, filename):
        if not self.processable():
            return

        for i, line in enumerate(lines):
            tab_index = line.find(self.TAB_INDENT)
            if tab_index != -1:
                off = Offence(
                    cop_name=self.name(),
                    location=(i, tab_index),
                    message="Indentation contains tab",
                    filename=filename,
                    severity='warning'
                )
                self.offences.append(off)
