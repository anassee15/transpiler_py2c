import ply.yacc as yacc

import AST
import lex_py2c
from lex_py2c import tokens


def p_programs_complex(p):
    """programs : program main"""
    p[0] = AST.ProgramNode(p[1].children + [p[2]])


def p_programs(p):
    """programs : main"""
    p[0] = AST.ProgramNode([p[1]])


def p_main(p):
    """main : MAIN INDENT program_main DEDENT"""
    p[0] = AST.MainNode(p[3].children)


def p_program(p):
    """program : statement
    | statement NEWLINE"""
    p[0] = AST.ProgramNode(p[1])


def p_program_rec(p):
    """program : program statement NEWLINE
    | program statement"""
    p[0] = AST.ProgramNode(p[1].children + [p[2]])


def p_statement(p):
    """statement : assignation
    | function"""
    p[0] = p[1]


def p_function(p):
    """function : DEF ID '(' args ')' ARROW TYPE ':' INDENT program_main DEDENT"""
    p[0] = AST.FunctionNode(
        [AST.TypeNode(AST.TokenNode(p[7]))]
        + [AST.TokenNode(p[2])]
        + [AST.FunctionArgsNode(p[4])]
        + [AST.ProgramMainNode(p[10].children)]
    )


def p_function_no_args(p):
    """function : DEF ID '(' ')' ARROW TYPE ':' INDENT program_main DEDENT"""
    p[0] = AST.FunctionNode(
        [AST.TypeNode(AST.TokenNode(p[6]))]
        + [AST.TokenNode(p[2])]
        + [AST.ProgramMainNode(p[9].children)]
    )


def p_args(p):
    """args : arg"""
    p[0] = [p[1]]


def p_args_rec(p):
    """args : args ',' arg"""
    p[0] = p[1] + [p[3]]


def p_arg(p):
    """arg : ID ':' TYPE"""
    p[0] = AST.ArgNode(
        [AST.TypeNode(AST.TokenNode(p[3]))] + [AST.TokenNode(p[1])])


def p_program_main(p):
    """program_main : statement_main NEWLINE
    | statement_main"""
    p[0] = AST.ProgramMainNode(p[1])


def p_program_main_rec(p):
    """program_main : program_main statement_main NEWLINE
    | program_main statement_main"""
    p[0] = AST.ProgramMainNode(p[1].children + [p[2]])


def p_statement_main(p):
    """statement_main : assignation
    | global
    | structure_main
    | return_func
    | call_func
    | condition"""
    p[0] = p[1]


def p_global(p):
    """global : GLOBAL ID"""
    p[0] = AST.GlobalNode(AST.TokenNode(p[2]))


def p_statement_main_print(p):
    """statement_main : PRINT expression"""
    p[0] = AST.PrintNode(p[2])


def p_return_func(p):
    """return_func : RETURN expression"""
    p[0] = AST.ReturnNode(p[2])


def p_assignation(p):
    """assignation : ID '=' expression"""
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])


def p_structure_main(p):
    """structure_main : WHILE expression ':' INDENT program_main DEDENT"""
    p[0] = AST.WhileNode([p[2], p[5]])


def p_condition(p):
    """condition : if_stmt
    | if_stmt else_stmt
    | if_stmt elifs else_stmt
    """
    if len(p) == 2:
        p[0] = AST.ConditionNode([p[1]])
    elif len(p) == 3:
        p[0] = AST.ConditionNode([p[1], p[2]])
    else:
        p[0] = AST.ConditionNode([p[1]] + p[2] + [p[3]])


def p_if(p):
    """if_stmt : IF expression ':' INDENT program_main DEDENT"""
    p[0] = AST.IfNode([p[2], p[5]])


def p_else(p):
    """else_stmt : ELSE ':' INDENT program_main DEDENT"""
    p[0] = AST.ElseNode([p[4]])


def p_elifs(p):
    """elifs : elif_stmt
    | elifs elif_stmt
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_elif(p):
    """elif_stmt : ELIF expression ':' INDENT program_main DEDENT"""
    p[0] = AST.ElifNode([p[2], p[5]])


def p_expression_func(p):
    """expression : call_func"""
    p[0] = p[1]


def p_call_func_no_params(p):
    """call_func : ID '(' ')'"""
    p[0] = AST.CallFunctionNode(AST.TokenNode(p[1]))


def p_call_func(p):
    """call_func : ID '(' list_expr ')'"""
    p[0] = AST.CallFunctionNode([AST.TokenNode(p[1])] + [AST.ParamsNode(p[3])])


def p_list_expr(p):
    """list_expr : expression"""
    p[0] = [p[1]]


def p_list_expr_rec(p):
    """list_expr : list_expr ',' expression"""
    p[0] = p[1] + [p[3]]


def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = AST.TokenNode(p[1])


def p_expression_id(p):
    """expression : ID"""
    p[0] = AST.TokenNode(p[1])


def p_expression_text(p):
    """expression : TEXT"""
    p[0] = AST.TokenNode(p[1])


def p_expression_bool(p):
    """expression : BOOL"""
    p[0] = AST.TokenNode(p[1])


def p_expression_parenthesis(p):
    """expression : '(' expression ')'"""
    p[0] = p[2]


def p_expression_op(p):
    """expression : expression '+' expression
    | expression '-' expression
    | expression '*' expression
    | expression '/' expression
    | expression '%' expression"""
    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_expression_uminus(p):
    """expression : '+' expression %prec UMINUS
    | '-' expression %prec UMINUS"""
    p[0] = AST.OpNode(p[1], [p[2]])


def p_expression_logic(p):
    """expression : expression AND expression
    | expression OR expression
    | expression EQ expression
    | expression NE expression
    | expression GE expression
    | expression LE expression
    | expression '>' expression
    | expression '<' expression"""

    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_expression_not(p):
    """expression : NOT expression"""
    p[0] = AST.OpNode(p[1], [p[2]])


def p_number(p):
    """NUMBER : INT
    | FLOAT"""
    p[0] = p[1]


def p_string(p):
    """TEXT : STRING
    | CHAR"""
    p[0] = p[1]


def p_bool(p):
    """BOOL : TRUE
    | FALSE"""
    p[0] = p[1]


def p_error(p):
    print(f"Syntax error inline {p.lineno}")
    yacc.errok()


precedence = (
    ("left", "+"),
    ("left", "-"),
    ("left", "*"),
    ("left", "/"),
    ("right", "UMINUS"),
)

yacc.yacc(outputdir="generated")


def gen_token():
    while 1:
        tok = lex_py2c.lex.token()
        if tok is not None:
            if tok.type == "DEDENT":
                i = tok.value
                tok.value = 1
                for i in range(i - 1):
                    yield tok
                    # print("line %d: %s(%s)" %
                    #       (tok.lineno, tok.type, tok.value))
        yield tok

        if not tok:
            break

        # print("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))


def get_token(gen=gen_token()):
    return next(gen)


def parse(program, debug=0):
    lex_py2c.lex.input(program)
    return yacc.parse(tokenfunc=get_token, debug=debug)


if __name__ == "__main__":
    import os
    import sys

    prog = open(sys.argv[1]).read()
    lex_py2c.lex.input(prog)

    result = yacc.parse(tokenfunc=get_token, debug=1)
    print(result)

    try:
        graph = result.makegraphicaltree()
        name = f"{os.path.splitext(sys.argv[1])[0]}-ast.pdf"
        graph.write_pdf(name)
        print(f"wrote ast to {name}")
    except Exception as e:
        print("Please install graphviz to visualize AST...")
