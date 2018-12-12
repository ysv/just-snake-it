"""File with cops"""


class ICop:
    cop_conf = dict()

    @classmethod
    def name(self):
        """The Cop name"""


class ITokenCop(ICop):
    def process_tokens(self, tokens):
        """Method receives generator of tokens and process them one by one."""


class IRawFileCop(ICop):
    def process_file(self, lines):
        """Method receives list of file lines and process them one by one."""
