#!/usr/bin/python
#shebang line, also includes imports for files and regular expressions
#shebang line found using command: 'which python' in terminal
#Need 'python' to run, cannot use 'python3'
#'python3' uses different syntax and there will be a compiler/printing error 
#when using the 'python3' shebang line

#PROGRAMMER: Michael Ghizzi
#CPSC-323 Summer 2015
#ASSIGNMENT: #2
#FILE: RATSU15.py inputfile.txt outputfile.txt
#FILE USAGE: ./RATSU15.py <inputfile.txt> <outputfile.txt>

#IMPORTS:
#-----------------
import os
import sys      
import os.path  #Used to read / write files
import re       #Used for regular expressions
#-----------------

#Takes in THREEE arguments, the ./RATSU15.py python script and the
#"inputname.txt" which includes the source code we want to test
#"outputname.txt" includes where the output will be written too
#-----------------
if len(sys.argv) != 3:
    print('USEAGE: ./RATSU15.py <inputname.txt> <outputname.txt>')
    exit(1)
if os.path.isfile(sys.argv[1]):
    pass
else:
    print('ERROR: File does not exist. Usage ./RATSU15.py <inputname.txt> <outputname.txt>')
    exit(1)
#-----------------

#Assigns files to appropriate variables  
#-----------------
inputfile = sys.argv[1]
outputfile = sys.argv[2]
#-----------------


#REGULAR EXPRESSIONS(TOKENS):
#-----------------
#INTEGERS
integer = re.compile(r'^[0-9]+$')
#REAL NUMBERS
realNumber = re.compile(r'^([\d]+)[.]([\d]+)$')
#SEPARATORS
separator = re.compile(r'^[$]+|([(]|[)])|([{]|[}])|[,]|[;]$')
sp = re.compile(r'^(\$\$)$')
#IDENTIFIERS
identifier = re.compile(r'^[a-z]([a-z]|[0-9])*[a-z]|([a-z])$', re.IGNORECASE)
#INVALID IDENTIFIER:
invalid = re.compile(r'^([0-9]+[a-z]*)|([a-z]+[0-9]+|&|@|#|%|^)$', re.IGNORECASE)   #ADDED MORE INVALID CHARACTERS
#OPERATORS
operator = re.compile(r'^(<|>|[+]|-|[*]|$|[/]|_|[|]|\$\$)$')
op = re.compile(r'^\=\=|\!\=|=$')
#KEYWORDS
keyword = re.compile(r'^(integer|if|else|fi|return|read|write|while|empty|real|boolean|condition|function|identifier|true|false)$', re.IGNORECASE)


#Need to edit expression in primary
term = re.compile(r'^(-?[0-9]+.?[0-9]+)[\s]?[*|/][\s]?(-?[0-9]+.?[0-9]+)$')
#factor = re.compile(r'^[-]?[\s]?[0-9]+[.]?[0-9]+$')
#primary = re.compile(r'^([a-z]([a-z]|[0-9])*[a-z]|[a-z])|\(\s(([a-z]([a-z]|[0-9])*[a-z]|[a-z]))[\s]\)|([\d]+)[.]([\d]+)|[0-9]+|true|false|([a-z][0-9])$', re.IGNORECASE)
primary = re.compile(r'^([a-z]([a-z]|[0-9])*[a-z]|([a-z]))|(([-][\s])?[0-9]+)|true|false|([a-z]([a-z]|[0-9])*[a-z]|([a-z]))[\s]?[\(][\s]?([a-z]([a-z]|[0-9])*[a-z]|([a-z]))[\s]?[\)]|(([-][\s])?([\d]+)[.]([\d]+))|([\(][\s]?([a-z]([a-z]|[0-9])*[a-z]|([a-z])|([-]?[0-9]+))[\s]?[+|-|<|>|*|/][\s]?(([a-z]([a-z]|[0-9])*[a-z]|([a-z]))|([-]?[0-9]+))[\s]?[\)])$', re.IGNORECASE)

#expression = re.compile(r'^(-?[0-9]+.?[0-9]+[\s]*[+|-]?[\s]*-?[0-9]+.?[0-9]+)$')
expression = re.compile(r'^([\(][\s]?([a-z]([a-z]|[0-9])*[a-z]|([a-z])|([-]?[0-9]+))[\s]?[+|-|<|>|*|/][\s]?(([a-z]([a-z]|[0-9])*[a-z]|([a-z]))|([-]?[0-9]+))[\s]?[\)])$')
relop = re.compile(r'^\=\=|\!\=|=|>|<?$')
condition = re.compile(r'^(-?[0-9]+.?[0-9]+[\s]*[+|-]?[\s]*-?[0-9]+.?[0-9]+)[\=\=|\!\=|=|>|<]+(-?[0-9]+.?[0-9]+[\s]*[+|-]?[\s]*-?[0-9]+.?[0-9]+)$')
#-----------------

#Opens the files to be read / written to
infile = open(inputfile, 'r')
outfile = open(outputfile, 'w')
outfile.write("OUTPUT:\n")

stack = []
lex0r = []

#LEXER FUNCTION
#-----------------
def lexer():
    for line in infile:
        line = line.rstrip('\n')
        #Taking away '\n' from the file to make it easier to read
        #line1 has the list for the line
        line1 = line.lower().split()                                    ##IMPLEMENTED THE .lower() command again because it was messing up with my ASSM#2
        
        #LEXER FUNCTION AFTER FOR LINE IN INFILE
        #GO BY STRING AND BY CHARACTER
        #IF I GET A WHILE GO BY STRING
        #IF I HAVE A OPERATOR OR SEPARATOR USE A CHAR
        #lol has the element in line1
        for lol in line1:
            # determine if lol has a operator, sep
            # if it has either then split the lol further or read by char
            isREAL = realNumber.match(lol)
            isKEY = keyword.match(lol)
            isIDENTIFIER = identifier.match(lol)
            isINVALID = invalid.match(lol)
            isINT = integer.match(lol)
            isOP2 = op.match(lol)
            isSP = sp.match(lol)
        
            if isREAL and not isINT:
                outfile.write("\nToken: Real         Lexeme: ")
                outfile.write(lol)
                stack.append(lol)
                lex0r.append("\nToken: Real         Lexeme: " + lol)
            elif isOP2:
                outfile.write("\nToken: Operator     Lexeme: ")
                outfile.write(lol)
                stack.append(lol)
                lex0r.append("\nToken: Operator     Lexeme: " + lol)
            elif isKEY:
                outfile.write("\nToken: Keyword      Lexeme: ")
                outfile.write(lol)
                stack.append(lol)
                lex0r.append("\nToken: Keyword      Lexeme: " + lol)
            elif isIDENTIFIER and not isINVALID:
                outfile.write("\nToken: Identifier    Lexeme: ")
                outfile.write(lol)
                stack.append(lol)
                lex0r.append("\nToken: Identifier    Lexeme: " + lol)
            elif isINT and not isREAL:
                outfile.write("\nToken: Integer      Lexeme: ")
                outfile.write(lol)
                stack.append(lol)
                lex0r.append("\nToken: Integer      Lexeme: " + lol)
            elif isSP:
                outfile.write("\nToken: Separator    Lexeme: ")
                outfile.write(lol)
                stack.append(lol)
                lex0r.append("\nToken: Separator    Lexeme: " + lol)
            elif isINVALID:
                outfile.write("\nToken: INVALID      Lexeme: ")
                outfile.write(lol)
                stack.append(lol)
                lex0r.append("\nToken: INVALID      Lexeme: " + lol)
        
            if (isREAL == None and isKEY == None and isIDENTIFIER == None and isINT == None and isINVALID == None):
                for ch in lol:
                    isINT = integer.match(ch)
                    isOP = operator.match(ch)
                    isSEP = separator.match(ch)
                    isIDF = identifier.match(ch)
                
                    if isINT:
                        outfile.write("\nToken: Integer      Lexeme: ")
                        outfile.write(ch)
                        stack.append(lol)
                        lex0r.append("\nToken: Integer      Lexeme: " + ch)
                    elif isOP and not isOP2:
                        outfile.write("\nToken: Operator     Lexeme: ")
                        outfile.write(ch)
                        stack.append(lol)
                        lex0r.append("\nToken: Operator     Lexeme: " + ch)
                    elif isSEP and not isSP:
                        outfile.write("\nToken: Separator    Lexeme: ")
                        outfile.write(ch)
                        stack.append(lol)
                        lex0r.append("\nToken: Separator    Lexeme: " + ch)
                    elif isIDF:
                        outfile.write("\nToken: Identifier   Lexeme: ")
                        outfile.write(ch)
                        stack.append(lol)
                        lex0r.append("\nToken: Identifier    Lexeme: " + ch)

##CALLS LEXER FUNCTION - This creates a list of Tokens, and identifiers, and they are then written to the output file.           
lexer();    

#print("TESTING NEW LEX0R STACK")
#def testorz(lex0r):
#    if len(lex0r) > 0:
#        print(lex0r[0])
#        lex0r.pop(0)
#        testorz(lex0r);
#testorz(lex0r);

#--------------------------
#prints stack (debugging)
print "\nTHIS IS OUR STACK BEFORE: "
print "-------------------"
print ', '.join(stack)
print "-------------------\n"
#--------------------------



#The program cannot run if there is not $$ and the start and $$ at the end of the file. 
#This function is a check before we run the parse function.
def check():
    if len(stack) > 0:
        if ((stack[0] != '$$') or (stack[-1] != '$$')):  
            print("ERROR: Program will not run without $$ and the beginning of file,\n\t and $$ at the end of the file")
            exit(1)
check();


#RDP(): Recursive decent parser 
##IF WE STILL HAVE ITEMS IN THE STACK
##CALLS A FUNCTION
##IF THAT FUNCTION MATCHES, THEN IT IS OUTPUTTED
##DELETES LAST ITEM IN STACK
##NOTE: Might need these to be in separate function
def parser(stack):
    if len(stack) > 0:
        if stack[0] == '$$':
            print(lex0r[0])
            lex0r.pop(0)         
            print("$$ <Opt Function Definitions> $$ <Opt Declaration List> <Statement List> $$")
            stack.pop(0)
            print("$$ has been consumed") 
            parser(stack);
        elif stack[0] == 'rat15su':
            print(lex0r[0])
            lex0r.pop(0)         
            print("<RATSU15> ::= $$ <Opt Function Definitions> $$ <Opt Declaration List> <Statement List> $$")
            stack.pop(0)  
            parser(stack);
        elif stack[0] == 'opt.function.definitions':
            print(lex0r[0])
            lex0r.pop(0)
            print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
            stack.pop(0)
            parser(stack);
        elif stack[0] == 'function.definitions': 
            print(lex0r[0])
            lex0r.pop(0)            
            print("<Function Definitions> ::= <Function> | <Function> <Function Definitions>")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'function':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)
            print("<Function> ::= function <Identifier> ( <Opt Parameters> ) <Opt Declaration List> <Body>")
            if identifier.match(stack[0]):
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0)
                print("<Function> ::= <Identifier> ( <Opt Parameters> ) <Opt Declaration List> <Body>")
                if stack[0] == '(':
                    print(lex0r[0])
                    lex0r.pop(0)
                    stack.pop(0)
                    print("<Function> ::= <Opt Parameters> ) <Opt Declaration List> <Body>")
                    if identifier.match(stack[0]):
                        print(lex0r[0])
                        lex0r.pop(0)
                        stack.pop(0)
                        print("<Function> ::=  ) <Opt Declaration List> <Body>")
                        if stack[0] == ')':
                            print(lex0r[0])
                            lex0r.pop(0)
                            stack.pop(0)
                            print("<Function> ::= <Opt Declaration List> <Body>")
                            if identifier.match(stack[0]):
                                print(lex0r[0])
                                lex0r.pop(0)
                                stack.pop(0)
                                print("<Function> ::= <Body>") ##NEED TO IMPLEMENT BODY FUNCTION 
                    else:
                        print("ERROR: Missing Opt Parameters")
                        exit(0)
                else: 
                    print("ERROR: Missing (")
                    exit(0)
            else: 
                print("ERROR: Syntax Error")
                exit(0)
        elif stack[0] == 'opt.parameters':
            print(lex0r[0])
            lex0r.pop(0)        
            print("<Opt Parameters> ::= <Parameters> | <Empty>")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'parameters':
            print(lex0r[0])
            lex0r.pop(0)    
            print("<Parameters> ::= <Parameter> | <Parameter> , <Parameters>")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'parameter':
            print(lex0r[0])
            lex0r.pop(0)  
            print("<Parameter> ::= <Identifier> <Qualifier>")
            stack.pop(0)
            if identifier.match(stack[0]):
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0)
                if stack[0] == 'integer' or 'boolean' or 'real':
                    stack.pop(0)
                    print("Parameter Consumed")
                    parser(stack);
                else: 
                    print("ERROR: Invalid Syntax")
                    exit(0)
            else: 
                print("ERROR: Invalid Syntax")
                exit(0)         
            parser(stack);
        elif stack[0] == 'opt.declaration.list':
            print(lex0r[0])
            lex0r.pop(0)       
            print("<Opt Declaration List> ::= <Declaration List> | <Empty>")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'declaration.list':
            print(lex0r[0])
            lex0r.pop(0)
            print("<Declaration List> := <Declaration> ; | <Declaration> ; <Declaration List>")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'declaration':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)              
            print("<Declaration> ::= <Qualifier > <IDs>")
            if stack[0] == 'integer' or 'boolean' or 'real':
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0)
                print("<Declaration> ::= <IDs>")
                if integer.match(stack[0]):
                    stack.pop(0)
                    print("declaration has been consumed")
                    parser(stack);
                else:
                    print("ERROR: IDs NOT FOUND")
            else:
                print("ERROR: QUALIFIER NOT FOUND")
        elif stack[0] == 'integer' or stack[0] == 'boolean' or stack[0] == 'real':
            if stack[0] == 'integer':
                print(lex0r[0])
                lex0r.pop(0)
                print("<Qualifier> ::= integer")
                stack.pop(0)
                print("Qualifier has been consumed")
                parser(stack);
            elif stack[0] == 'true' or 'false':
                print(lex0r[0])
                lex0r.pop(0)
                print("<Qualifier> ::= boolean")
                stack.pop(0) 
                print("Qualifier has been consumed")
                parser(stack);
            elif stack[0] == 'real':
                print(lex0r[0])
                lex0r.pop(0)
                print("<Qualifier> ::= real")
                stack.pop(0)
                print("Qualifier has been consumed")
                parser(stack);
            else:
                print("ERROR: INVALID SYNTAX")
                exit(0)
        elif stack[0] == 'ids': ##IDs Implementation wont work with my design setup. 
            print(lex0r[0])
            lex0r.pop(0)
            print("<IDs> ::= <Identifier> | <Identifier>, <IDs>")
            stack.pop(0)      
            parser(stack);
#        elif stack[0] == 'body':    ##Same implementation as <Compound>. Combine them?
#            print(lex0r[0])
#            lex0r.pop(0)
#            stack.pop(0)
#            print("<Body> ::= { < Statement List> }")
#            if stack[0] == '{':
#                print(lex0r[0])
#                lex0r.pop(0)
#                stack.pop(0)
#                print("<Body> ::= < Statement List> }")
#                if stack[0] == 'write' or 'read' or 'while' or 'assign' or 'if' or 'compound':
#                    print(lex0r[0])
#                    lex0r.pop(0)
#                    stack.pop(0)
#                    print("<Body> ::= }")
#                    if stack[0] == '}':
#                        print(lex0r[0])
#                        lex0r.pop(0)
#                        stack.pop(0)
#                        print("Body Statement has been consumed")
#                        parser(stack);
#                    else: 
#                        print("ERROR: MISSING }")
#                        exit(0)
#                else: 
#                    print("ERROR: INVALID STATEMENT LIST")
#                    exit(0)
#            else: 
#                print("ERROR: MISSING {")
#                exit(0)
        elif stack[0] == 'statement.list':
            print(lex0r[0])
            lex0r.pop(0)    
            print("<Statement List> ::= <Statement> | <Statement> <Statement List>")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'statement': #'write' or 'read' or 'while' or 'assign' or 'if' or 'compound'
            print(lex0r[0])
            lex0r.pop(0)
            print("<Statement> ::= <Compound> | <Assign> | <If> |<Return> | <Write> | <Read> | <While>")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'compound' or stack[0] == 'body':
            print(lex0r[0])
            lex0r.pop(0)   
            stack.pop(0)
            print("<Compound> ::= { <Statement List> }")
            print("<Body> ::= { < Statement List> }")
            if stack[0] == '{':
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0)
                print("<Compound> ::= < Statement List> }")
                print("<Body> ::= < Statement List> }")
                if stack[0] == 'write' or stack[0] == 'read' or stack[0] == 'while' or stack[0] == 'assign' or stack[0] == 'if' or stack[0] == 'compound' or stack[0] == 'return':                                                                              ##NEED TO IMPLEMENT STATEMENT LIST
                    print(lex0r[0])
                    lex0r.pop(0)
                    stack.pop(0)
                    print("<Compound> ::= }")
                    print("<Body> ::=  }")
                    if stack[0] == '}':
                        print(lex0r[0])
                        lex0r.pop(0)
                        stack.pop(0)
                        print("Compound/Body Statement has been consumed")
                        parser(stack);
                    else: 
                        print("ERROR: MISSING }")
                        exit(0)
                else: 
                    print("ERROR: INVALID STATEMENT LIST")
                    exit(0)
            else: 
                print("ERROR: MISSING {")
                exit(0)
        elif identifier.match(stack[0]) and stack[1] == '=':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)
            print("<Assign> ::= <Identifier> = <Expression> ;")
            if stack[0] == '=':
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0)
                print("<Assign> ::= = <Expression>")
                if expression.match(stack[0]):        #NEED TO FIX
                    print(lex0r[0])
                    lex0r.pop(0)
                    stack.pop(0)
                    print("<Assign> ::= <Expression>") 
                    if stack[0] == ';':
                        print(lex0r[0])
                        lex0r.pop(0)
                        stack.pop(0)
                        print("Assign has been consumed")
                        parser(stack);
                    else:
                        print("ERROR: Missing ;")
                        exit(0)
                else: 
                    print("ERROR: Missing Expression")
                    exit(0)
            else:
                print("ERROR: Missing '='")
                exit(0)
        elif stack[0] == 'if':
            print(lex0r[0])
            lex0r.pop(0)  
            print("<If> ::= if ( <Condition> ) <Statement> fi | if ( <Condition> ) <Statement> else <Statement> fi")
            stack.pop(0)      
            parser(stack);
        elif stack[0] == 'return':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)            
            print("<Return> ::= return <Expression> ;")
            parser(stack);
        elif stack[0] == 'write':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0) 
            print("<Write> := write ( <Expression> ) ;")
            if stack[0] == '(':
                print(lex0r[0])
                lex0r.pop(0)
                print("<Write> := <Expression> ) ;")      
                stack.pop(0)                                             
                if identifier.match(stack[0]) or integer.match(stack[0]) or realNumber.match(stack[0]):     ##I.E. EXPRESSION
                    print(lex0r[0])
                    lex0r.pop(0)
                    stack.pop(0)                           
                    if operator.match(stack[0]):
                        print(lex0r[0])
                        lex0r.pop(0)
                        stack.pop(0)
                        if identifier.match(stack[0]) or integer.match(stack[0]) or realNumber.match(stack[0]):
                            print(lex0r[0])
                            lex0r.pop(0)
                            stack.pop(0)
                            print("<Write> := ) ;")                                          
                            if stack[0] == ')':
                                print(lex0r[0])
                                lex0r.pop(0)
                                print("<Write> := ;")
                                stack.pop(0)                             
                                if stack[0] == ';':
                                    print(lex0r[0])
                                    lex0r.pop(0)                     
                                    print("Write Statement has been consumed")  
                                    stack.pop(0)
                                    parser(stack);
                                else:
                                    print("ERROR: MISSING ;")
                                    exit(0)
                            else: 
                                print("ERROR: MISSING )")
                                exit(0)
                        else: 
                            print("ERROR: INVALID EXPRESSION")
                            exit(0)
                    else: 
                        print("ERROR: INVALID OPERATOR")
                        exit(0) 
                else: 
                    print("ERROR: Not valid syntax")
                    exit(0)  
        elif stack[0] == 'read':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)                                                
            print("<Read> := read ( <IDs> ) ;")                         
            if stack[0] == '(':
                print(lex0r[0])
                lex0r.pop(0)                     
                print("<Read> := <IDs> ) ;")      
                stack.pop(0)                                            
                if identifier.match(stack[0]):              ##identifier, ids       
                    print(lex0r[0])
                    lex0r.pop(0)
                    print("<Read> := ) ;")                                          
                    stack.pop(0)
                    if stack[0] == ')':
                        print(lex0r[0])
                        lex0r.pop(0)
                        print("<Read> := ;")
                        stack.pop(0)                             
                        if stack[0] == ';':                             
                            print(lex0r[0])
                            lex0r.pop(0)
                            print("Read Statement has been consumed")   
                            stack.pop(0)
                            parser(stack);
                        else:
                            print("ERROR: Missing ;")
                            exit(0)
                    else: 
                        print("ERROR: Missing )")
                        exit(0)
                else: 
                    print("ERROR: Missing identifier")
                    exit(0)
            else: 
                print("ERROR: Missing (")
                exit(0)
        elif stack[0] == 'while':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)
            if stack[0] == '(':
                print(lex0r[0])
                lex0r.pop(0)
                print("<While> := write ( <Condition> ) <Statement>")
                stack.pop(0)
                if stack[0] == condition.match(stack[0]):
                    print(lex0r[0])
                    lex0r.pop(0)
                    print("<While> := ) <Statement>")
                    stack.pop(0)
                    if stack[0] == ')':
                        print(lex0r[0])
                        lex0r.pop(0)
                        print("<While> := <Statement>")
                        if stack[0] == statement.match(stack[0]):
                            print(lex0r[0])
                            lex0r.pop(0)
                            print("While has been consumed")
                            parser(stack);
                        else:
                            print("ERROR: While must have a statement after ( <Condition> )")
                            exit(0)
                    else:
                        print("ERROR: While statement must have a )")   
                        exit(0)
                else:
                    print("ERROR: While statement must have a valid condition")
                    exit(0)
            else:
                print("ERROR: While statement must have a (")
                exit(0)
        elif stack[0] == condition.match(stack[0]):
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)            
            print("<Condition> =: <Expression> <Relop> <Expression>")
            parser(stack);
        elif relop.match(stack[0]):
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)      
            print("<Relop> := == | != | > | <")
            if stack[0] == '==' or '!=' or '>' or '<':
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0) 
                print("Relop has been consumed")
                parser(stack);
            else:
                print("ERROR: Relop must have a ==, !=, >, <")
                exit(0)
        elif expression.match(stack[0]):    ##Cannot have spaces in between the expression and term 
            print(lex0r[0])
            lex0r.pop(0)
            print("<Expression> := <Expression> + <Term> | <Expression> - <Term> | <Term>")
            stack.pop(0)
            parser(stack);
        elif stack[0] == 'expression_prime':    ##Dont know how to implement 
            print(lex0r[0])
            lex0r.pop(0)
            print("<Expression_Prime> := +<Term> <Expression_Prime>  | - <Term> <Expression_Prime>  | EPSILON")
            stack.pop(0)      
            parser(stack);
        elif term.match(stack[0]):
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0) 
            print("<Term> := <Term> * <Factor> | <Term> / <Factor> | <Factor>")
            if stack[0] == '*' or '/':
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0)
                print("<Term> :=  * <Factor> |  / <Factor>")
                if integer.match(stack[0]) or identifier.match(stack[0]):
                    print(lex0r[0])
                    lex0r.pop(0)
                    stack.pop(0)
                    print("Term has been consumed")
                    parser(stack);
                else: 
                    print("ERROR: MISSING FACTOR")
                    exit(0)
            else:
                print("ERROR: MISSING * OR /")
                exit(0) 
        elif primary.match(stack[0]):  ##Need to change to actual factor statement
            print(lex0r[0])
            lex0r.pop(0)
            print("<Factor> := - <Primary> | <Primary>")
            stack.pop(0) 
            parser(stack);
        elif primary.match(stack[0]):
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)
            print("<Primary> := <Identifier> | <Integer> | <Identfier> (<IDs) | ( <Expression> ) | <Real> | true | false")
            if primary.match(stack[0]):
                print(lex0r[0])
                lex0r.pop(0)
                print("Primary Variable has been consumed")
                stack.pop(0)
                parser(stack);
            else:
                print("ERROR: Missing <Identifier> | <Integer> | <Identfier> (<IDs) | ( <Expression> ) | <Real> | true | false")
                exit(0)
        elif stack[0] == 'empty':
            print(lex0r[0])
            lex0r.pop(0)
            stack.pop(0)           
            print("<Empty> := Empty")
            if stack[0] == 'empty':
                print(lex0r[0])
                lex0r.pop(0)
                stack.pop(0) 
                print("Empty has been consumed")
                parser(stack);
            else: 
                print("ERROR: INVALID SYNTAX")
        elif len(stack) < 0:
            print("ERROR: OUT OF TOKENS, EXITING.")
            exit(0)
        else:           ##FOR DEBUGGING
            print "ERROR: EXITING"
            print ', '.join(stack)
            print "ERROR: EXITING"
            exit(0)
    elif len(stack) <= 0:
        print("\n======================================")
        print("NOTICE: OUT OF TOKENS.\n NOW EXITING")
        print("======================================\n")
        
        #--------------------------
        #prints stack (debugging)
        print "THIS IS OUR STACK AFTER THE PROGRAM HAS BEEN RAN: "
        print "-------------------"
        print ', '.join(stack)
        print "-------------------\n"
        #--------------------------
        exit(0)
            
parser(stack);





print "\n=====================\n"
print "THIS SHOULD NOT OUTPUT\n"
print "=====================\n"

#--------------------------






#PATCH NOTES & NEED TO WORK ON:
#----------------------- 
#The file has the start with $$ and end with $$, correct?
#Confused on how to remove left recursion
#I have no idea what the definition of a statement list is, need to implement, have it just written as the word 'statementlist' atm. Can use RE to fix. 


#LATER..
#Work on getting the Token / Lexemes and syntax analysis on the same line
