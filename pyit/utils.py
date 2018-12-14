from token import *

BINARY_TOKENS = {
    '+': PLUS,
    '-': MINUS,
    '*': STAR,
    '/': SLASH,
    '|': VBAR,
    '&': AMPER,
    '<': LESS,
    '>': GREATER,
    '=': EQUAL,
    '%': PERCENT,
    '==': EQEQUAL,
    '!=': NOTEQUAL,
    '<=': LESSEQUAL,
    '>=': GREATEREQUAL,
    '^': CIRCUMFLEX,
    '<<': LEFTSHIFT,
    '>>': RIGHTSHIFT,
    '+=': PLUSEQUAL,
    '-=': MINEQUAL,
    '*=': STAREQUAL,
    '/=': SLASHEQUAL,
    '%=': PERCENTEQUAL,
    '&=': AMPEREQUAL,
    '|=': VBAREQUAL,
    '^=': CIRCUMFLEXEQUAL,
    '<<=': LEFTSHIFTEQUAL,
    '>>=': RIGHTSHIFTEQUAL,
    '**=': DOUBLESTAREQUAL,
    '//': DOUBLESLASH,
    '//=': DOUBLESLASHEQUAL,
}


def binary_operator_keys():
    return BINARY_TOKENS.keys()


def binary_operator_values():
    return BINARY_TOKENS.values()


def token_line_indent(token):
    line = token.line
    return line.replace(line.lstrip(), '')


def is_first_token_except_indent(token):
    indent = token_line_indent(token)
    return token.start[1] == len(indent)

RESET = -1
CYAN = 1
BLUE = 2
YELLOW = 3
RED = 4
GREEN = 5
BOLD = 100
COLORS = {
    CYAN:   '\033[1;36m',
    BLUE:   '\033[1;34m',
    YELLOW: '\033[93m',
    RED:    '\033[91m',
    GREEN:  '\033[92m',
    BOLD:   '\033[;1m',
    RESET:  '\033[0;0m',
}

