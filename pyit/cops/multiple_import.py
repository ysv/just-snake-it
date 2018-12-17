from pyit.cop import IRawFileCop, Cop, IFormatCop
from tokenize import tokenize, untokenize
from pyit.offence import Offence
from io import BytesIO


class MultipleImport(Cop):

    COP_CONFIG = {}
    __implements__ = [IFormatCop]

    offences = []

    def __init__(self, cop_conf=None):
        if cop_conf is None:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG}
        else:
            self.cop_conf = {**self.DEFAULT_CONFIG, **self.COP_CONFIG, **cop_conf}

    @classmethod
    def name(cls):
        return 'multiple_import_cop'

    def process_file(self, lines, filename):
        pass

    def fix_tokens(self, tokens, filename):
        res = []

        processed_lines = 0
        for tkn in tokens:
            if not tkn.line.startswith('import'):
                res.append(tkn)
                processed_lines = tkn.start[0]
                continue

            if tkn.string == 'import':
                if tkn.start[0] <= processed_lines:
                    continue
                spl = tkn.line.split(',')
                first_import = spl.pop(0).split()[1]
                spl.insert(0, first_import)
                for import_name in spl:
                    import_token = (1, 'import')
                    mod_token = (1, import_name.lstrip())
                    endline_token = (4, "\n")
                    res.append(import_token)
                    res.append(mod_token)
                    res.append(endline_token)

        return untokenize(res)

