
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+left-left*left/rightUMINUSAND ARROW CHAR DEDENT DEF ELIF ELSE EQ FALSE FLOAT GE GLOBAL ID IF INDENT INT LE MAIN NE NEWLINE NOT OR PRINT RETURN STRING TRUE TYPE WHILEprograms : program mainprograms : mainmain : MAIN INDENT program_main DEDENTprogram : statement\n    | statement NEWLINEprogram : program statement NEWLINE\n    | program statementstatement : assignation\n    | functionfunction : DEF ID '(' args ')' ARROW TYPE ':' INDENT program_main DEDENTfunction : DEF ID '(' ')' ARROW TYPE ':' INDENT program_main DEDENTargs : argargs : args ',' argarg : ID ':' TYPEprogram_main : statement_main NEWLINE\n    | statement_mainprogram_main : program_main statement_main NEWLINE\n    | program_main statement_mainstatement_main : assignation\n    | global\n    | structure_main\n    | return_func\n    | call_func\n    | conditionglobal : GLOBAL IDstatement_main : PRINT expressionreturn_func : RETURN expressionassignation : ID '=' expressionstructure_main : WHILE expression ':' INDENT program_main DEDENTcondition : if_stmt\n    | if_stmt else_stmt\n    | if_stmt elifs else_stmt\n    if_stmt : IF expression ':' INDENT program_main DEDENTelse_stmt : ELSE ':' INDENT program_main DEDENTelifs : elif_stmt\n    | elifs elif_stmt\n    elif_stmt : ELIF expression ':' INDENT program_main DEDENTexpression : call_funccall_func : ID '(' ')'call_func : ID '(' list_expr ')'list_expr : expressionlist_expr : list_expr ',' expressionexpression : NUMBERexpression : IDexpression : TEXTexpression : BOOLexpression : '(' expression ')'expression : expression '+' expression\n    | expression '-' expression\n    | expression '*' expression\n    | expression '/' expression\n    | expression '%' expressionexpression : '+' expression %prec UMINUS\n    | '-' expression %prec UMINUSexpression : expression AND expression\n    | expression OR expression\n    | expression EQ expression\n    | expression NE expression\n    | expression GE expression\n    | expression LE expression\n    | expression '>' expression\n    | expression '<' expressionexpression : NOT expressionNUMBER : INT\n    | FLOATTEXT : STRING\n    | CHARBOOL : TRUE\n    | FALSE"
    
_lr_action_items = {'MAIN':([0,2,4,6,7,11,12,16,32,33,34,35,36,37,42,43,44,45,46,47,77,78,79,85,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,139,140,],[5,5,-4,-8,-9,-7,-5,-6,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-53,-54,-63,-39,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,-11,-10,]),'ID':([0,2,4,6,7,9,11,12,13,14,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,56,57,61,63,64,65,66,67,68,69,70,71,72,73,74,75,77,78,79,84,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,112,113,114,115,117,123,124,125,126,129,130,131,132,134,136,137,138,139,140,],[8,8,-4,-8,-9,15,-7,-5,26,32,-6,26,-16,-19,-20,-21,-22,-23,-24,32,54,32,32,-30,32,-44,-28,-38,-43,-45,-46,32,32,32,32,-64,-65,-66,-67,-68,-69,80,-18,-15,-26,32,-25,-27,-31,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-53,-54,-63,-17,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,80,-40,32,26,26,26,26,26,26,26,-29,-34,26,-33,26,26,26,26,-11,-10,]),'DEF':([0,2,4,6,7,11,12,16,32,33,34,35,36,37,42,43,44,45,46,47,77,78,79,85,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,139,140,],[9,9,-4,-8,-9,-7,-5,-6,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-53,-54,-63,-39,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,-11,-10,]),'$end':([1,3,10,49,],[0,-2,-1,-3,]),'NEWLINE':([4,6,7,11,18,19,20,21,22,23,24,30,32,33,34,35,36,37,42,43,44,45,46,47,50,52,54,56,57,77,78,79,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,129,130,132,139,140,],[12,-8,-9,16,51,-19,-20,-21,-22,-23,-24,-30,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,84,-26,-25,-27,-31,-53,-54,-63,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,-29,-34,-33,-11,-10,]),'INDENT':([5,88,91,93,116,128,133,],[13,114,115,117,125,134,136,]),'=':([8,26,],[14,14,]),'PRINT':([13,17,18,19,20,21,22,23,24,30,32,33,34,35,36,37,42,43,44,45,46,47,50,51,52,54,56,57,77,78,79,84,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,114,115,117,123,124,125,126,129,130,131,132,134,136,137,138,],[25,25,-16,-19,-20,-21,-22,-23,-24,-30,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-18,-15,-26,-25,-27,-31,-53,-54,-63,-17,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,25,25,25,25,25,25,25,-29,-34,25,-33,25,25,25,25,]),'GLOBAL':([13,17,18,19,20,21,22,23,24,30,32,33,34,35,36,37,42,43,44,45,46,47,50,51,52,54,56,57,77,78,79,84,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,114,115,117,123,124,125,126,129,130,131,132,134,136,137,138,],[27,27,-16,-19,-20,-21,-22,-23,-24,-30,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-18,-15,-26,-25,-27,-31,-53,-54,-63,-17,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,27,27,27,27,27,27,27,-29,-34,27,-33,27,27,27,27,]),'WHILE':([13,17,18,19,20,21,22,23,24,30,32,33,34,35,36,37,42,43,44,45,46,47,50,51,52,54,56,57,77,78,79,84,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,114,115,117,123,124,125,126,129,130,131,132,134,136,137,138,],[28,28,-16,-19,-20,-21,-22,-23,-24,-30,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-18,-15,-26,-25,-27,-31,-53,-54,-63,-17,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,28,28,28,28,28,28,28,-29,-34,28,-33,28,28,28,28,]),'RETURN':([13,17,18,19,20,21,22,23,24,30,32,33,34,35,36,37,42,43,44,45,46,47,50,51,52,54,56,57,77,78,79,84,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,114,115,117,123,124,125,126,129,130,131,132,134,136,137,138,],[29,29,-16,-19,-20,-21,-22,-23,-24,-30,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-18,-15,-26,-25,-27,-31,-53,-54,-63,-17,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,29,29,29,29,29,29,29,-29,-34,29,-33,29,29,29,29,]),'IF':([13,17,18,19,20,21,22,23,24,30,32,33,34,35,36,37,42,43,44,45,46,47,50,51,52,54,56,57,77,78,79,84,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,114,115,117,123,124,125,126,129,130,131,132,134,136,137,138,],[31,31,-16,-19,-20,-21,-22,-23,-24,-30,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-18,-15,-26,-25,-27,-31,-53,-54,-63,-17,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,31,31,31,31,31,31,31,-29,-34,31,-33,31,31,31,31,]),'(':([14,15,25,26,28,29,31,32,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[38,48,38,53,38,38,38,53,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'+':([14,25,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,55,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,113,122,],[39,39,39,39,39,-44,63,-38,-43,-45,-46,39,39,39,39,-64,-65,-66,-67,-68,-69,63,39,63,63,39,63,39,39,39,39,39,39,39,39,39,39,39,39,39,63,-53,-54,63,-39,63,63,-48,-49,-50,-51,63,63,63,63,63,63,63,63,63,-47,-40,39,63,]),'-':([14,25,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,55,56,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,113,122,],[40,40,40,40,40,-44,64,-38,-43,-45,-46,40,40,40,40,-64,-65,-66,-67,-68,-69,64,40,64,64,40,64,40,40,40,40,40,40,40,40,40,40,40,40,40,64,-53,-54,64,-39,64,64,64,-49,-50,-51,64,64,64,64,64,64,64,64,64,-47,-40,40,64,]),'NOT':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'INT':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'FLOAT':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'STRING':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'CHAR':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'TRUE':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FALSE':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'DEDENT':([17,18,19,20,21,22,23,24,30,32,33,34,35,36,37,42,43,44,45,46,47,50,51,52,54,56,57,77,78,79,84,85,89,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,123,124,126,129,130,131,132,137,138,],[49,-16,-19,-20,-21,-22,-23,-24,-30,-44,-28,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-18,-15,-26,-25,-27,-31,-53,-54,-63,-17,-39,-32,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,129,130,132,-29,-34,135,-33,139,140,]),'ELSE':([30,58,60,90,132,135,],[59,59,-35,-36,-33,-37,]),'ELIF':([30,58,60,90,132,135,],[61,61,-35,-36,-33,-37,]),'*':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,65,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,65,65,65,65,65,-53,-54,65,-39,65,65,65,65,-50,-51,65,65,65,65,65,65,65,65,65,-47,-40,65,]),'/':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,66,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,66,66,66,66,66,-53,-54,66,-39,66,66,66,66,66,-51,66,66,66,66,66,66,66,66,66,-47,-40,66,]),'%':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,67,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,67,67,67,67,67,-53,-54,67,-39,67,67,-48,-49,-50,-51,67,67,67,67,67,67,67,67,67,-47,-40,67,]),'AND':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,68,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,68,68,68,68,68,-53,-54,68,-39,68,68,-48,-49,-50,-51,68,68,68,68,68,68,68,68,68,-47,-40,68,]),'OR':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,69,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,69,69,69,69,69,-53,-54,69,-39,69,69,-48,-49,-50,-51,69,69,69,69,69,69,69,69,69,-47,-40,69,]),'EQ':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,70,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,70,70,70,70,70,-53,-54,70,-39,70,70,-48,-49,-50,-51,70,70,70,70,70,70,70,70,70,-47,-40,70,]),'NE':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,71,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,71,71,71,71,71,-53,-54,71,-39,71,71,-48,-49,-50,-51,71,71,71,71,71,71,71,71,71,-47,-40,71,]),'GE':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,72,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,72,72,72,72,72,-53,-54,72,-39,72,72,-48,-49,-50,-51,72,72,72,72,72,72,72,72,72,-47,-40,72,]),'LE':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,73,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,73,73,73,73,73,-53,-54,73,-39,73,73,-48,-49,-50,-51,73,73,73,73,73,73,73,73,73,-47,-40,73,]),'>':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,74,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,74,74,74,74,74,-53,-54,74,-39,74,74,-48,-49,-50,-51,74,74,74,74,74,74,74,74,74,-47,-40,74,]),'<':([32,33,34,35,36,37,42,43,44,45,46,47,52,55,56,62,76,77,78,79,85,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,122,],[-44,75,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,75,75,75,75,75,-53,-54,75,-39,75,75,-48,-49,-50,-51,75,75,75,75,75,75,75,75,75,-47,-40,75,]),':':([32,34,35,36,37,42,43,44,45,46,47,55,59,62,77,78,79,80,85,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,121,127,],[-44,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,88,91,93,-53,-54,-63,108,-39,116,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,128,133,]),')':([32,34,35,36,37,42,43,44,45,46,47,48,53,76,77,78,79,81,83,85,86,87,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,118,120,122,],[-44,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,82,85,107,-53,-54,-63,109,-12,-39,112,-41,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,-14,-13,-42,]),',':([32,34,35,36,37,42,43,44,45,46,47,77,78,79,81,83,85,86,87,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,118,120,122,],[-44,-38,-43,-45,-46,-64,-65,-66,-67,-68,-69,-53,-54,-63,110,-12,-39,113,-41,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-47,-40,-14,-13,-42,]),'ARROW':([82,109,],[111,119,]),'TYPE':([108,111,119,],[118,121,127,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programs':([0,],[1,]),'program':([0,],[2,]),'main':([0,2,],[3,10,]),'statement':([0,2,],[4,11,]),'assignation':([0,2,13,17,114,115,117,123,124,125,126,131,134,136,137,138,],[6,6,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'function':([0,2,],[7,7,]),'program_main':([13,114,115,117,125,134,136,],[17,123,124,126,131,137,138,]),'statement_main':([13,17,114,115,117,123,124,125,126,131,134,136,137,138,],[18,50,18,18,18,50,50,18,50,50,18,18,50,50,]),'global':([13,17,114,115,117,123,124,125,126,131,134,136,137,138,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'structure_main':([13,17,114,115,117,123,124,125,126,131,134,136,137,138,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'return_func':([13,17,114,115,117,123,124,125,126,131,134,136,137,138,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'call_func':([13,14,17,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,114,115,117,123,124,125,126,131,134,136,137,138,],[23,34,23,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,23,23,23,23,23,23,23,23,23,23,23,23,]),'condition':([13,17,114,115,117,123,124,125,126,131,134,136,137,138,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'if_stmt':([13,17,114,115,117,123,124,125,126,131,134,136,137,138,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'expression':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[33,52,55,56,62,76,77,78,79,87,92,94,95,96,97,98,99,100,101,102,103,104,105,106,122,]),'NUMBER':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TEXT':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'BOOL':([14,25,28,29,31,38,39,40,41,53,61,63,64,65,66,67,68,69,70,71,72,73,74,75,113,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'else_stmt':([30,58,],[57,89,]),'elifs':([30,],[58,]),'elif_stmt':([30,58,],[60,90,]),'args':([48,],[81,]),'arg':([48,110,],[83,120,]),'list_expr':([53,],[86,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programs","S'",1,None,None,None),
  ('programs -> program main','programs',2,'p_programs_complex','parser_py2c.py',9),
  ('programs -> main','programs',1,'p_programs','parser_py2c.py',14),
  ('main -> MAIN INDENT program_main DEDENT','main',4,'p_main','parser_py2c.py',19),
  ('program -> statement','program',1,'p_program','parser_py2c.py',24),
  ('program -> statement NEWLINE','program',2,'p_program','parser_py2c.py',25),
  ('program -> program statement NEWLINE','program',3,'p_program_rec','parser_py2c.py',30),
  ('program -> program statement','program',2,'p_program_rec','parser_py2c.py',31),
  ('statement -> assignation','statement',1,'p_statement','parser_py2c.py',36),
  ('statement -> function','statement',1,'p_statement','parser_py2c.py',37),
  ('function -> DEF ID ( args ) ARROW TYPE : INDENT program_main DEDENT','function',11,'p_function','parser_py2c.py',42),
  ('function -> DEF ID ( ) ARROW TYPE : INDENT program_main DEDENT','function',10,'p_function_no_args','parser_py2c.py',52),
  ('args -> arg','args',1,'p_args','parser_py2c.py',61),
  ('args -> args , arg','args',3,'p_args_rec','parser_py2c.py',66),
  ('arg -> ID : TYPE','arg',3,'p_arg','parser_py2c.py',71),
  ('program_main -> statement_main NEWLINE','program_main',2,'p_program_main','parser_py2c.py',77),
  ('program_main -> statement_main','program_main',1,'p_program_main','parser_py2c.py',78),
  ('program_main -> program_main statement_main NEWLINE','program_main',3,'p_program_main_rec','parser_py2c.py',83),
  ('program_main -> program_main statement_main','program_main',2,'p_program_main_rec','parser_py2c.py',84),
  ('statement_main -> assignation','statement_main',1,'p_statement_main','parser_py2c.py',89),
  ('statement_main -> global','statement_main',1,'p_statement_main','parser_py2c.py',90),
  ('statement_main -> structure_main','statement_main',1,'p_statement_main','parser_py2c.py',91),
  ('statement_main -> return_func','statement_main',1,'p_statement_main','parser_py2c.py',92),
  ('statement_main -> call_func','statement_main',1,'p_statement_main','parser_py2c.py',93),
  ('statement_main -> condition','statement_main',1,'p_statement_main','parser_py2c.py',94),
  ('global -> GLOBAL ID','global',2,'p_global','parser_py2c.py',99),
  ('statement_main -> PRINT expression','statement_main',2,'p_statement_main_print','parser_py2c.py',104),
  ('return_func -> RETURN expression','return_func',2,'p_return_func','parser_py2c.py',109),
  ('assignation -> ID = expression','assignation',3,'p_assignation','parser_py2c.py',114),
  ('structure_main -> WHILE expression : INDENT program_main DEDENT','structure_main',6,'p_structure_main','parser_py2c.py',119),
  ('condition -> if_stmt','condition',1,'p_condition','parser_py2c.py',124),
  ('condition -> if_stmt else_stmt','condition',2,'p_condition','parser_py2c.py',125),
  ('condition -> if_stmt elifs else_stmt','condition',3,'p_condition','parser_py2c.py',126),
  ('if_stmt -> IF expression : INDENT program_main DEDENT','if_stmt',6,'p_if','parser_py2c.py',137),
  ('else_stmt -> ELSE : INDENT program_main DEDENT','else_stmt',5,'p_else','parser_py2c.py',142),
  ('elifs -> elif_stmt','elifs',1,'p_elifs','parser_py2c.py',147),
  ('elifs -> elifs elif_stmt','elifs',2,'p_elifs','parser_py2c.py',148),
  ('elif_stmt -> ELIF expression : INDENT program_main DEDENT','elif_stmt',6,'p_elif','parser_py2c.py',157),
  ('expression -> call_func','expression',1,'p_expression_func','parser_py2c.py',162),
  ('call_func -> ID ( )','call_func',3,'p_call_func_no_params','parser_py2c.py',167),
  ('call_func -> ID ( list_expr )','call_func',4,'p_call_func','parser_py2c.py',172),
  ('list_expr -> expression','list_expr',1,'p_list_expr','parser_py2c.py',177),
  ('list_expr -> list_expr , expression','list_expr',3,'p_list_expr_rec','parser_py2c.py',182),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser_py2c.py',187),
  ('expression -> ID','expression',1,'p_expression_id','parser_py2c.py',192),
  ('expression -> TEXT','expression',1,'p_expression_text','parser_py2c.py',197),
  ('expression -> BOOL','expression',1,'p_expression_bool','parser_py2c.py',202),
  ('expression -> ( expression )','expression',3,'p_expression_parenthesis','parser_py2c.py',207),
  ('expression -> expression + expression','expression',3,'p_expression_op','parser_py2c.py',212),
  ('expression -> expression - expression','expression',3,'p_expression_op','parser_py2c.py',213),
  ('expression -> expression * expression','expression',3,'p_expression_op','parser_py2c.py',214),
  ('expression -> expression / expression','expression',3,'p_expression_op','parser_py2c.py',215),
  ('expression -> expression % expression','expression',3,'p_expression_op','parser_py2c.py',216),
  ('expression -> + expression','expression',2,'p_expression_uminus','parser_py2c.py',221),
  ('expression -> - expression','expression',2,'p_expression_uminus','parser_py2c.py',222),
  ('expression -> expression AND expression','expression',3,'p_expression_logic','parser_py2c.py',227),
  ('expression -> expression OR expression','expression',3,'p_expression_logic','parser_py2c.py',228),
  ('expression -> expression EQ expression','expression',3,'p_expression_logic','parser_py2c.py',229),
  ('expression -> expression NE expression','expression',3,'p_expression_logic','parser_py2c.py',230),
  ('expression -> expression GE expression','expression',3,'p_expression_logic','parser_py2c.py',231),
  ('expression -> expression LE expression','expression',3,'p_expression_logic','parser_py2c.py',232),
  ('expression -> expression > expression','expression',3,'p_expression_logic','parser_py2c.py',233),
  ('expression -> expression < expression','expression',3,'p_expression_logic','parser_py2c.py',234),
  ('expression -> NOT expression','expression',2,'p_expression_not','parser_py2c.py',240),
  ('NUMBER -> INT','NUMBER',1,'p_number','parser_py2c.py',245),
  ('NUMBER -> FLOAT','NUMBER',1,'p_number','parser_py2c.py',246),
  ('TEXT -> STRING','TEXT',1,'p_string','parser_py2c.py',251),
  ('TEXT -> CHAR','TEXT',1,'p_string','parser_py2c.py',252),
  ('BOOL -> TRUE','BOOL',1,'p_bool','parser_py2c.py',257),
  ('BOOL -> FALSE','BOOL',1,'p_bool','parser_py2c.py',258),
]
