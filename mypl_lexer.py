"""The MyPL Lexer class.

NAME: Lauren Chin
DATE: Spring 2024
CLASS: CPSC 326 OPL

"""

from mypl_token import *
from mypl_error import *


class Lexer:
    """For obtaining a token stream from a program."""

    def __init__(self, in_stream):
        """Create a Lexer over the given input stream.

        Args:
            in_stream -- The input stream. 

        """
        self.in_stream = in_stream
        self.line = 1
        self.column = 0


    def read(self):
        """Returns and removes one character from the input stream."""
        self.column += 1
        return self.in_stream.read_char()

    
    def peek(self):
        """Returns but doesn't remove one character from the input stream."""
        return self.in_stream.peek_char()

    
    def eof(self, ch):
        """Return true if end-of-file character"""
        return ch == ''

    
    def error(self, message, line, column):
        raise LexerError(f'{message} at line {line}, column {column}')

    def next_token(self):
        """Return the next token in the lexer's input stream."""
        # read initial character
        ch = self.read()

        # TODO: finish the rest of the next_token function
        column_start = self.column
        line_start = self.line
        if(self.eof(ch)):
            #then end of file so return eof
            tok = Token(TokenType.EOS, "", self.line, self.column)
            return tok
        else:
            while(self.eof(ch) == False):
                #CHECKING WHITE SPACE
                if(ch.isspace()):
                    while((ch.isspace()) and (self.eof(ch) == False)):
                        if(ch == '\n'):
                            #if the character is a new line
                            self.line = self.line + 1
                            self.column = 0
                        ch = self.read()
                    if(self.eof(ch)):
                        #then end of file so return eof
                        tok = Token(TokenType.EOS, "", self.line, self.column)
                        return tok
                    
                #CHECKING EASY LEXER PUNCTUATION
                if(ch == "."):
                    #then token is a dot and should be returned
                    tok = Token(TokenType.DOT, ".", self.line, self.column)
                    return tok
                if(ch == ","):
                    #then token is a comma and should be returned
                    tok = Token(TokenType.COMMA, ",", self.line, self.column)
                    return tok
                if(ch == "("):
                    #then token is a left parentheses and should be returned
                    tok = Token(TokenType.LPAREN, "(", self.line, self.column)
                    return tok
                if(ch == ")"):
                    #then token is a right parentheses and should be returned
                    tok = Token(TokenType.RPAREN, ")", self.line, self.column)
                    return tok
                if(ch == "["):
                    #then token is a left bracket and should be returned
                    tok = Token(TokenType.LBRACKET, "[", self.line, self.column)
                    return tok
                if(ch == "]"):
                    #then token is a right bracket and should be returned
                    tok = Token(TokenType.RBRACKET, "]", self.line, self.column)
                    return tok
                if(ch == ";"):
                    #then token is a semicolon and should be returned
                    tok = Token(TokenType.SEMICOLON, ";", self.line, self.column)
                    return tok
                if(ch == "{"):
                    #then token is a left brace and should be returned
                    tok = Token(TokenType.LBRACE, "{", self.line, self.column)
                    return tok
                if(ch == "}"):
                    #then token is a right brace and should be returned
                    tok = Token(TokenType.RBRACE, "}", self.line, self.column)
                    return tok

                #CHECKING LEXER (single or double character) OPERATORS
                if(ch == "+"):
                    #then token is a plus and should be returned
                    tok = Token(TokenType.PLUS, "+", self.line, self.column)
                    return tok
                if(ch == "-"):
                    #then token is a minus and should be returned
                    tok = Token(TokenType.MINUS, "-", self.line, self.column)
                    return tok
                if(ch == "*"):
                    #then token is a times and should be returned
                    tok = Token(TokenType.TIMES, "*", self.line, self.column)
                    return tok
                if(ch == "/"):
                    next = self.peek()
                    if(next == "/"):
                        #then token is comment and we should read to end of line and return this
                        comment = ""
                        line_start = self.line
                        column_start = self.column
                        ch = self.read() #need to read the "/" character
                        ch = self.read()
                        while(ch != "\n"):
                            if(self.eof(ch)):
                                #if the comment takes us to the end of stream then we should return the token
                                tok = Token(TokenType.COMMENT, comment, line_start, column_start)
                                return tok
                            comment = comment + ch
                            ch = self.read()
                        if(ch == "\n"):
                            #if new line then we need to adjust the line and column
                            self.line = self.line + 1
                            self.column = 0
                        tok = Token(TokenType.COMMENT, comment, line_start, column_start)
                        return tok
                    else:
                        #then token is a divide and should be returned
                        tok = Token(TokenType.DIVIDE, "/", self.line, self.column)
                        return tok
                    
                #CHECKING LEXER RELATIONAL COMPARATORS (and checking for assign)
                if(ch == "="):
                    line_start = self.line
                    column_start = self.column
                    next = self.peek()
                    if(next == "="):
                        #then token is a equal comparator and should be returned
                        ch = self.read() #reads the second =
                        tok = Token(TokenType.EQUAL, "==", line_start, column_start)
                        return tok
                    else:
                        #then token is an assign because it's just one "=" and should be returned
                        tok = Token(TokenType.ASSIGN, "=", self.line, self.column)
                        return tok
                if(ch == "!"):
                    line_start = self.line
                    column_start = self.column
                    next = self.peek()
                    if(next == "="):
                        #then token is a not equal comparator and should be returned
                        ch = self.read() #reads the =
                        tok = Token(TokenType.NOT_EQUAL, "!=", line_start, column_start)
                        return tok
                if(ch == "<"):
                    line_start = self.line
                    column_start = self.column
                    next = self.peek()
                    if(next == "="):
                        #then token is a less than or equal to comparator and should be returned
                        ch = self.read() #reads the =
                        tok = Token(TokenType.LESS_EQ, "<=", line_start, column_start)
                        return tok
                    else:
                        #then token is just a less than comparator and should be returned
                        tok = Token(TokenType.LESS, "<", self.line, self.column)
                        return tok
                if(ch == ">"):
                    line_start = self.line
                    column_start = self.column
                    next = self.peek()
                    if(next == "="):
                        #then token is a greater than or equal to comparator and should be returned
                        ch = self.read() #reads the =
                        tok = Token(TokenType.GREATER_EQ, ">=", line_start, column_start)
                        return tok
                    else:
                        #then token is just a greater than comparator and should be returned
                        tok = Token(TokenType.GREATER, ">", self.line, self.column)
                        return tok      
                
                #CHECKING STRINGS
                if(ch == '"'):
                    line_start = self.line
                    column_start = self.column
                    str = ""
                    ch = self.read()
                    while(ch != '"'):
                        if((self.eof(ch)) or (ch == "\n")):
                            #then there wasn't an end double quote and error should be thrown
                            self.error("String not terminated correctly", line_start, column_start)
                        str = str + ch
                        ch = self.read()
                    #then token is a string value and should be returned
                    tok = Token(TokenType.STRING_VAL, str, line_start, column_start)
                    return tok
                
                #CHECKING FOR INT OR DOUBLE
                if(ch.isdecimal()):
                    line_start = self.line
                    column_start = self.column
                    number = ch
                    dot_counter = 0
                    next = self.peek()
                    if((ch == '0') and (next.isdecimal())):
                        #need to throw an error
                        self.error("Leading zero error", self.line, self.column)
                    while((next.isdecimal()) or (next == ".") and (dot_counter < 1)):
                        if(next == "."):
                            #then we need to increase the dot_counter to ensure only one dot is read
                            dot_counter = dot_counter + 1
                            ch = self.read()
                            if(self.peek().isdecimal() == False):
                                #need to throw an error
                                self.error("Invalid double syntax", self.line, self.column)
                        else:
                            ch = self.read()
                        number = number + ch
                        next = self.peek()
                    if "." in number:
                        #then token is a double and should be returned
                        tok = Token(TokenType.DOUBLE_VAL, number, line_start, column_start)
                        return tok 
                    else:
                        #then token is an int and should be returned
                        tok = Token(TokenType.INT_VAL, number, line_start, column_start)
                        return tok 
                    
                #CHECKING FOR ID AND RESERVED WORDS
                if(ch.isalpha()):
                    line_start = self.line
                    column_start = self.column
                    #then we need to read the string until it's not an alpha, digit, or underscore
                    fullNextString = ch
                    next = self.peek()
                    while((next.isalpha()) or (next.isdigit()) or (next == "_")):
                        #then keep reading the characters
                        ch = self.read()
                        fullNextString = fullNextString + ch
                        next = self.peek()
                    #here now fullNextString is the token string and we can check against other multiple character tokens
                    if(fullNextString == "and"):
                        tok = Token(TokenType.AND, "and", line_start, column_start)
                        return tok
                    elif(fullNextString == "or"):
                        tok = Token(TokenType.OR, "or", line_start, column_start)
                        return tok
                    elif(fullNextString == "not"):
                        tok = Token(TokenType.NOT, "not", line_start, column_start)
                        return tok
                    elif(fullNextString == "int"):
                        tok = Token(TokenType.INT_TYPE, "int", line_start, column_start)
                        return tok
                    elif(fullNextString == "double"):
                        tok = Token(TokenType.DOUBLE_TYPE, "double", line_start, column_start)
                        return tok
                    elif(fullNextString == "string"):
                        tok = Token(TokenType.STRING_TYPE, "string", line_start, column_start)
                        return tok
                    elif(fullNextString == "bool"):
                        tok = Token(TokenType.BOOL_TYPE, "bool", line_start, column_start)
                        return tok
                    elif(fullNextString == "void"):
                        tok = Token(TokenType.VOID_TYPE, "void", line_start, column_start)
                        return tok
                    elif(fullNextString == "null"):
                        tok = Token(TokenType.NULL_VAL, "null", line_start, column_start)
                        return tok
                    elif(fullNextString == "true"):
                        tok = Token(TokenType.BOOL_VAL, "true", line_start, column_start)
                        return tok
                    elif(fullNextString == "false"):
                        tok = Token(TokenType.BOOL_VAL, "false", line_start, column_start)
                        return tok
                    elif(fullNextString == "struct"):
                        tok = Token(TokenType.STRUCT, "struct", line_start, column_start)
                        return tok
                    elif(fullNextString == "array"):
                        tok = Token(TokenType.ARRAY, "array", line_start, column_start)
                        return tok
                    elif(fullNextString == "for"):
                        tok = Token(TokenType.FOR, "for", line_start, column_start)
                        return tok
                    elif(fullNextString == "while"):
                        tok = Token(TokenType.WHILE, "while", line_start, column_start)
                        return tok
                    elif(fullNextString == "if"):
                        tok = Token(TokenType.IF, "if", line_start, column_start)
                        return tok
                    elif(fullNextString == "elseif"):
                        tok = Token(TokenType.ELSEIF, "elseif", line_start, column_start)
                        return tok
                    elif(fullNextString == "else"):
                        tok = Token(TokenType.ELSE, "else", line_start, column_start)
                        return tok
                    elif(fullNextString == "new"):
                        tok = Token(TokenType.NEW, "new", line_start, column_start)
                        return tok
                    elif(fullNextString == "return"):
                        tok = Token(TokenType.RETURN, "return", line_start, column_start)
                        return tok
                    else:
                        tok = Token(TokenType.ID, fullNextString, line_start, column_start)
                        return tok
                else:
                    #need to throw an error
                    self.error("Invalid symbol", self.line, self.column)
                
                #now go to next character
                ch = self.read()
                    
            #taking care of end of file after the while loop
            if(self.eof(ch)):
                #then end of file so return eof
                tok = Token(TokenType.EOS, "", self.line, self.column)
                return tok    
            