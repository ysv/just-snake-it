from pyit.cop import ITokenCop


class IndentationCop:

    DEFAULT_CONFIG = {
        'enabled': True
    }
    __implements__ = [ITokenCop]

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = self.DEFAULT_CONFIG
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **cop_conf}

    def process_tokens(self, tokens):
        if not self.cop_conf.get('enabled', True):
            return

        # for token in tokens:
        #     print(token)

    @classmethod
    def name(cls):
        return 'indentation_cop'



