from pyit.cop import IRawFileCop, Cop
from pyit.offence import Offence


class MixedIndentationCop(Cop):

    COP_CONFIG = {
        "allow_tabs": False,
    }

    TAB_IDENT = '\t'
    SPACE_IDENT = ' ' * 4

    __implements__ = [IRawFileCop]
    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = self.DEFAULT_CONFIG
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'indentation_cop'

    def allow_tabs(self):
        return self.cop_conf.get('allow_tabs', False)

    def process_file(self, lines, filename):
        if not self.processable():
            return
        initial_ident_for_file = None

        if not self.allow_tabs():
            initial_ident_for_file = self.SPACE_IDENT

        if not self.allow_tabs():
            self.find_tabs(lines)

        # for line in lines:
        #     if not (line.startswith(self.SPACE_IDENT) or
        #             line.startswith(self.TAB_IDENT)):
        #         continue
        #
        #     line_ident = line.replace(line.lstrip(), '')
        #
        #     if initial_ident_for_file is None:
        #         initial_ident_for_file = self.SPACE_IDENT \
        #             if line_ident.startswith(self.SPACE_IDENT)\
        #             else self.TAB_IDENT

            # if self.allow_tabs():
            #     if line.startswith(self.SPACE_IDENT):
            #         initial_ident_for_file = self.SPACE_IDENT
            #     else:
            #         initial_ident_for_file = self.TAB_IDENT
    def find_tabs(self, lines):
        self.offences
        for i, line in enumerate(lines):
            tab_index = line.find('\t')
            if tab_index != -1:
                off = Offence(
                    cop_name=self.name(),
                    location=(i, tab_index),
                    message="Indentation contains tab",
                )
                self.offences.append(off)
