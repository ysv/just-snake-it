from pyit.cop import IRawFileCop, Cop
from pyit.offence import Offence


class LineLengthCop(Cop):

    COP_CONFIG = {
        'max_length': 80,
    }
    __implements__ = [IRawFileCop]

    offences = []
    ALLOWED_LINE_LENGTH = 120

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'line_length_cop'

    def max_length(self):
        if self.cop_conf['max_length'] < self.ALLOWED_LINE_LENGTH:
            return self.cop_conf['max_length']
        return self.ALLOWED_LINE_LENGTH

    def process_file(self, lines, filename):
        if not self.processable():
            return

        for i, line in enumerate(lines):
            if len(line) < self.max_length():
                continue
            message = "Line is too long (" + str(len(line)) + " char). Brakes " + str(self.max_length())\
                      + " char limit"
            off = Offence(
                cop_name=self.name(),
                location=(i, self.max_length()),
                message=message,
                filename=filename,
                severity='convention'
            )
            self.offences.append(off)
