from pyit.utils import *


class Offence:
    # TODO: severity should be in separate class.
    # By design it could be
    # R: :refactor, C: :convention,
    # W: :warning, E: :error
    cop_name = str()
    location = ()
    message = str()
    severity = str()
    filename = str()

    SEVERITY_COLORS = {
        'refactor':   COLORS[CYAN],
        'convention': COLORS[BLUE],
        'warning':    COLORS[YELLOW],
        'error':      COLORS[RED]
    }

    RESET_COLOR = COLORS[RESET]
    BOLD_COLOR = COLORS[BOLD]

    def __init__(self, cop_name, location, message, filename=None, severity='refactor'):
        self.cop_name = cop_name
        self.location = location
        self.message = message
        self.severity = severity
        self.filename = filename

    def __str__(self):
        color = self.SEVERITY_COLORS[self.severity]
        formatted_output = self.BOLD_COLOR + self.cop_name + ' says:' + '\n' \
                          + color + self.message + '\n' \
                          + self.filename + str(self.location) \
                          + '\n' + self.RESET_COLOR

        return formatted_output
