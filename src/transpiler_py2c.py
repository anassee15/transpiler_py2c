import AST
from AST import addToClass

HEADER = "#include <iostream>\n#include <string>\n\nusing namespace std;\n\n"

global_vars = {}  # variables that have been created outside a program main block
in_program_main = False
is_global_variable = False

vars = {}  # local variables

# Functions dictionary to store function names, return types, and argument data types
# Example: {"func_name": {"return": "int", "arg1": "int", "arg2": "string"}}
func = {"": {"": None}}

current_func = ""
call_func_not_stmt = False  # bool to know if we are in a function call or not

# Types dictionary to map Python data types to C++ data types
types = {
    type(3): "int",
    type(3.5): "float",
    type("string"): "string",
    type(5 > 2): "bool",
    "int": "int",
    "float": "float",
    "str": "string",
    "bool": "bool",
    "None": "void",
}

ops_convertion = {
    "not": "!",
    "and": "&&",
    "or": "||",
    "+": "+",
    "-": "-",
    "/": "/",
    "*": "*",
    "%": "%",
    "==": "==",
    "!=": "!=",
    "<": "<",
    ">": ">",
    "<=": "<=",
    ">=": ">=",
}

bool_ops = ["==", "!=", "<", ">", "<=", ">=", "and", "or", "not"]


def get_type(node):
    """
    Get the c++ type of a node
    :param node: the node
    :return: c++ type of the node
    """
    if node.__class__.__name__ == "CallFunctionNode":
        return func[node.children[0].tok]["return"]
    if node.tok in ["true", "false"]:
        return "bool"
    if node.tok in vars:
        # if the variable is already declared, return its type
        return vars[node.tok]
    elif node.tok in func[current_func].keys():
        # if the variable is a function argument, return its type
        return func[current_func][node.tok]["type"]
    else:
        # in this case, we know we are assigning a value to a variable that is not declared
        return types[type(node.tok)]


@addToClass(AST.ProgramNode)
def compile(self):
    code = "".join(c.compile() for c in self.children)
    return HEADER + code


@addToClass(AST.MainNode)
def compile(self):
    code = "\nint main() {\n"
    for c in self.children:
        code += c.compile()

    code += "return 0;\n}"
    return code


@addToClass(AST.ProgramMainNode)
def compile(self):
    global in_program_main
    in_program_main = True
    code = "\n{\n"
    for c in self.children:
        code += c.compile()

    code += "}\n"
    in_program_main = False
    return code


@addToClass(AST.TokenNode)
def compile(self):
    return f"{self.tok}".replace("'", '"')


@addToClass(AST.GlobalNode)
def compile(self):
    global is_global_variable
    if self.children[0].tok in global_vars.keys():
        is_global_variable = True
    else:
        raise Exception("Variable not declared in global scope")
    return ""


@addToClass(AST.OpNode)
def compile(self):
    global call_func_not_stmt
    # call_func_not_stmt used to avoid adding a semicolon at the end of a function call
    call_func_not_stmt = True

    if self.op == "/" and self.children[1].tok == 0:
        raise ZeroDivisionError("Division by 0")

    if len(self.children) > 1:
        code = f"{self.children[0].compile()} {ops_convertion[self.op]} {self.children[1].compile()}"
    else:
        code = f"{ops_convertion[self.op]} {self.children[0].compile()}"
    call_func_not_stmt = False
    return code


@addToClass(AST.AssignNode)
def compile(self):
    global call_func_not_stmt
    global global_vars
    global is_global_variable
    code = ""

    # call_func_not_stmt used to avoid adding a semicolon at the end of a function call
    call_func_not_stmt = True

    # to find the type of the variable :
    # if the variable is initialized with a an operation
    if self.children[1].__class__.__name__ == "OpNode":

        opNode = self.children[1]
        # set used to control the types of the variables
        set_type = set()

        # if the operation is a boolean operation
        if opNode.op in bool_ops:
            set_type.add("bool")

        set_type.add(get_type(opNode.children[0]))

        # if the operation is a chain of operations
        while (
            opNode.__class__.__name__ == "OpNode"
            and len(opNode.children[1].children) > 1
        ):
            opNode = opNode.children[1]
            set_type.add(get_type(opNode.children[0]))
        set_type.add(get_type(opNode.children[1]))

        if "bool" in set_type:
            if len(set_type) == 2:
                var_type = "bool"
                # get the type of the variable and add it to the variables
                if not is_global_variable:
                    code += f"{var_type} "
                is_global_variable = False

                if not in_program_main:
                    global_vars[self.children[0].tok] = var_type
            else:
                set_type.remove("bool")
                raise TypeError(f"Cannot compare different types : {set_type}")

            vars[self.children[0].tok] = var_type

        elif len(set_type) > 1:
            # if there is more than one type in the set, it means that we are trying to assign different types
            raise TypeError(f"Cannot assign different types : {set_type}")

        elif (
            self.children[0].tok not in vars
            and self.children[0].tok not in func[current_func].keys()
        ):
            var_type = set_type.pop()

            # get the type of the variable and add it to the variables
            if not is_global_variable:
                code += f"{var_type} "
            is_global_variable = False

            if not in_program_main:
                global_vars[self.children[0].tok] = var_type

            vars[self.children[0].tok] = var_type

    elif (
        self.children[0].tok not in vars
        and self.children[0].tok not in func[current_func].keys()
    ):
        if not is_global_variable:
            code += f"{get_type(self.children[1])} "
        is_global_variable = False
        vars[self.children[0].tok] = get_type(self.children[1])

        # if the variable is declared in the global scope, add it to the global variables
        if not in_program_main:
            global_vars[self.children[0].tok] = get_type(self.children[1])

    code += f"{self.children[0].compile()} = {self.children[1].compile()};\n"
    call_func_not_stmt = False
    is_global_variable = False
    return code


@addToClass(AST.PrintNode)
def compile(self):
    global call_func_not_stmt
    call_func_not_stmt = True
    code = f"cout << {self.children[0].compile()}" + " << endl;\n"
    call_func_not_stmt = False
    return code


@addToClass(AST.WhileNode)
def compile(self):
    global call_func_not_stmt
    call_func_not_stmt = True
    code = f"while ({self.children[0].compile()})"
    call_func_not_stmt = False
    code += f" {self.children[1].compile()}"
    return code


@addToClass(AST.FunctionNode)
def compile(self):
    global current_func
    global call_func_not_stmt
    code = ""
    # get size of children to know if there is args
    size = len(self.children)

    # function name
    func_name = self.children[1].tok
    func[func_name] = {}
    current_func = func_name

    # function return type
    code += f"{self.children[0].compile()} {self.children[1].tok}"
    func[func_name]["return"] = self.children[0].compile()

    code += "("

    # if there is args
    if size == 4:
        # function args
        call_func_not_stmt = True
        for arg in self.children[2].children:
            func[func_name][arg.children[1].tok] = {}
            func[func_name][arg.children[1].tok]["type"] = arg.children[0].compile()
            func[func_name][arg.children[1].tok]["used"] = False

        code += self.children[2].compile()
        call_func_not_stmt = False

    code += ")"
    # function body
    code += self.children[-1].compile()
    return code


@addToClass(AST.TypeNode)
def compile(self):
    return f"{types[self.children[0].tok]}"


@addToClass(AST.FunctionArgsNode)
def compile(self):
    code = ""
    for c in self.children:
        code += c.compile()
        code += ", "

    return code[:-3]


@addToClass(AST.ArgNode)
def compile(self):
    code = ""
    for c in self.children:
        code += c.compile()
        code += " "

    return code


@addToClass(AST.CallFunctionNode)
def compile(self):
    global current_func

    code = ""
    current_func = self.children[0].tok
    for c in self.children:
        code += c.compile()
        code += "("

    code = code[:-1]
    code += ")"

    if not call_func_not_stmt:
        code += ";\n"

    return code


@addToClass(AST.ParamsNode)
def compile(self):
    code = ""
    for i, c in enumerate(self.children, start=1):
        code += c.compile()
        # compare the type of the argument with the type of the function argument
        param_type = ""

        if c.__class__.__name__ == "OpNode":
            opNode = c
            set_type = {get_type(opNode.children[0])}
            while (
                opNode.children[1].__class__.__name__ == "OpNode"
                and len(opNode.children[1].children) > 1
            ):
                opNode = opNode.children[1]
                set_type.add(get_type(opNode.children[0]))
            set_type.add(get_type(opNode.children[1]))

            if len(set_type) > 1:
                raise TypeError(
                    f"Can't pass multiple types to a function argument : {list(set_type)} != "
                    + func[current_func][list(func[current_func].keys())[i]]["type"]
                    + " in function "
                    + current_func
                )

            else:
                param_type = set_type.pop()
        else:
            param_type = get_type(c)

        if param_type != func[current_func][list(func[current_func].keys())[i]]["type"]:
            raise TypeError(
                f"Argument type is not the same as the function argument type : {get_type(c)} != "
                + func[current_func][list(func[current_func].keys())[i]]["type"]
            )
        code += ", "

    return code[:-2]


@addToClass(AST.ReturnNode)
def compile(self):
    global call_func_not_stmt
    call_func_not_stmt = True
    # check if the return type is the same as the function return type
    if self.children[0].__class__.__name__ == "OpNode":
        opNode = self.children[0]
        set_type = {get_type(opNode.children[0])}
        while (
            opNode.children[1].__class__.__name__ == "OpNode"
            and len(opNode.children[1].children) > 1
        ):
            opNode = opNode.children[1]
            set_type.add(get_type(opNode.children[0]))
        set_type.add(get_type(opNode.children[1]))

        if len(set_type) > 1:
            raise TypeError(
                f'Return type is different from function return type in function "{current_func} : {list(set_type)} != {func[current_func]["return"]}'
            )
    elif get_type(self.children[0]) != func[current_func]["return"]:
        raise TypeError(
            f'Return type is different from function return type in function "{current_func}" : {get_type(self.children[0])} != {func[current_func]["return"]}'
        )

    code = f"return {self.children[0].compile()};\n"
    call_func_not_stmt = False
    return code


@addToClass(AST.ConditionNode)
def compile(self):
    return "".join(c.compile() for c in self.children)


@addToClass(AST.IfNode)
def compile(self):
    global call_func_not_stmt
    call_func_not_stmt = True
    code = f"if ({self.children[0].compile()})"
    call_func_not_stmt = False
    code += f" {self.children[1].compile()}"
    return code


@addToClass(AST.ElifNode)
def compile(self):
    global call_func_not_stmt
    call_func_not_stmt = True
    code = f"else if ({self.children[0].compile()})"
    call_func_not_stmt = False
    code += f" {self.children[1].compile()}"
    return code


@addToClass(AST.ElseNode)
def compile(self):
    return f"else {self.children[0].compile()}"


if __name__ == "__main__":
    import os
    import sys

    from parser_py2c import parse

    prog = open(sys.argv[1]).read()

    ast = parse(prog, debug=0)
    transpiled = ast.compile()

    name = f"{os.path.splitext(sys.argv[1])[0]}.cpp"

    with open(name, "w") as f:
        f.write(transpiled)

    print("Compilation successful to ", name)
