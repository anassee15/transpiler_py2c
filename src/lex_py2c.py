import ply.lex as lex

# stack to keep track of the indentation level
indent_stack = []

reserved_words = (
    "while",
    "print",
    "not",
    "def",
    "else",
    "elif",
    "return",
    "and",
    "or",
    "global",
)

# Définition des lexèmes à utiliser
tokens = (
    "ID",
    "FLOAT",
    "INT",
    "CHAR",
    "STRING",
    "EQ",
    "NE",
    "GE",
    "LE",
    "NEWLINE",
    "INDENT",
    "DEDENT",
    "MAIN",
    "ARROW",
    "TYPE",
    "IF",
    "TRUE",
    "FALSE",
) + tuple(map(lambda s: s.upper(), reserved_words))

literals = [
    "(",
    ")",
    "=",
    "+",
    "-",
    "*",
    "/",
    "%",
    ",",
    ":",
    "<",
    ">",
    "{",
    "}",
    "[",
    "]",
]


def t_MAIN(t):
    r"if[ ]*__name__[ ]*==[ ]*[\"']__main__[\"'][ ]*:"
    return t


def t_IF(t):
    r"if"
    return t


def t_TYPE(t):
    r"str|int|float|None"
    return t


def t_ARROW(t):
    r"->"
    return t


def t_TRUE(t):
    r"True"
    t.value = "true"
    return t


def t_FALSE(t):
    r"False"
    t.value = "false"
    return t


def t_ID(t):
    r"[A-Za-z_]\w*"
    if t.value in reserved_words:
        t.type = t.value.upper()
    return t


def t_CHAR(t):
    r"(\".\")|(\'.\')"  # TODO: check if tab enters in regex
    t.value = str(t.value)
    return t


def t_STRING(t):
    r"(\".*\")|(\'.*\')"
    t.value = str(t.value)
    return t


def t_FLOAT(t):
    r"\d*\.\d+"

    t.value = float(t.value)
    return t


def t_INT(t):
    r"\d+"

    t.value = int(t.value)
    return t


def t_EQ(t):
    r"=="
    return t


def t_NE(t):
    r"!="
    return t


def t_GE(t):
    r"\>="
    return t


def t_LE(t):
    r"\<="
    return t


def t_INDENT(t):
    r"\n+([ ]{4})+"
    global indent_stack

    # add the number of indentations to the stack
    indent_value = len(str(t.value).strip("\n")) / 4
    indent_stack.append(indent_value)

    """
    Check if it's an DEDENT : 
    1. if the current indentation value is lower than the previous one then it's an DEDENT :
    2. pop all indentation value are greater than current from the stack
    3. change the token type to DEDENT
    4. save the number of dedentations to do in the token value
    """
    if len(indent_stack) > 1:
        # if the indent value is decreasing, we return a DEDENT
        if indent_stack[-2] > indent_value:
            indent_stack.pop()
            count_dedent = int(indent_stack[-1] - indent_value)
            indent_stack.pop()

            # pop all the indentations that are greater than the last one
            while len(indent_stack) > 0 and indent_stack[-1] > indent_value:
                indent_stack.pop()

            t.type = "DEDENT"
            t.value = count_dedent
            return t

        # if the indent value is not increasing, we stay at the same level so we return a NEWLINE
        elif indent_stack[-2] == indent_value:
            indent_stack.pop()
            t.type = "NEWLINE"
            return t

    return t


def t_NEWLINE(t):
    r"\n+"
    global indent_stack

    # if the stack isn't empty, it means that we have an DEDENT to return
    if len(indent_stack) > 0:
        count_dedent = indent_stack[-1]

        while len(indent_stack) > 0:
            indent_stack.pop()

        t.type = "DEDENT"
        # the value of the DEDENT is the number of dedentations to do
        t.value = int(count_dedent)
        return t

    return t


# Trace des lignes traitées
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " "


def t_error(t):
    print("Illegal character'%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()


if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()

    lex.input(prog)
    while 1:
        tok = lex.token()
        if not tok:
            break
        print("line%d:%s(%s)" % (tok.lineno, tok.type, tok.value))
