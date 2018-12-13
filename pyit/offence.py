class Offence:
    # TODO: severity should be in separate class.
    # By design it could be
    # R: :refactor, C: :convention,
    # W: :warning, E: :error
    cop_name = str()
    location = ()
    message = str()
    severity = str()

    def __init__(self, cop_name, location, message, severity='refactor'):
        self.cop_name = cop_name
        self.location = location
        self.message = message
        self.severity = severity
