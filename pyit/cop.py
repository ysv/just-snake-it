"""File with cops"""


class Cop:
    cop_conf = dict()

    DEFAULT_CONFIG = {
        'enabled': True
    }

    def processable(self):
        return self.cop_conf.get('enabled', True)


class ICop:
    cop_conf = dict()

    @classmethod
    def name(self):
        """The Cop name"""


class ITokenCop(ICop):
    def process_tokens(self, tokens, filename):
        """Method receives generator of tokens and process them one by one."""


class IRawFileCop(ICop):
    def process_file(self, lines, filename):
        """Method receives list of file lines and process them one by one."""


class IFormatCop(ICop):
    def fix_format(self, lines, filename):
        """Method receives list of file lines and process them one by one."""
