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
