"""
Solutions to module 2 VA
Student: Alexander Hedene
Mail: alexander.hedene.3178@student.uu.se
Reviewed by Andrey
Reviewed date: 19-10-2024
"""

"""
Solutions to module 2 - A calculator
Student: Alexander Hedene
Mail: alexander.hedene.3178@student.uu.se
Reviewed by: Mattias
Reviewed date: 20-09-2024
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)
        
class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def mean(arg_list):
    return sum(arg_list)/len(arg_list)

def std(arg_list):
    Mean = mean(arg_list)
    return (sum(map(lambda x: (x-Mean)**2, arg_list)))**0.5

def log(arg):
    if arg > 0:
        return math.log(arg)
    else:
        raise EvaluationError("Argument to log less than or equal to 0")

def fac(n):
    if n >= 0 and round(n,5) % 1 == 0: # Since we rarely get integers 
        n = int(round(n,5)) # Want an integer as an answer
        if n == 0:
            return 1
        else:
            return n* fac(n-1)
    else:
        raise EvaluationError(f"Argument to fac {n}, need to be a positive integer")

def fib(n:int) -> int:
    if n >= 0 and round(n,5) % 1 == 0:
        n = int(round(n,5))
        memory = {0:0, 1:1}
        def fib_internal(n: int) -> int:
            if n not in memory:
                memory[n] = fib_internal(n-1) + fib_internal(n-2)
            return memory[n]
        return fib_internal(n)
    else:
        raise EvaluationError(f"Argument to fib {n}, need to be a positive integer")


def arglist(wtok, variables):
    if  not wtok.get_current() == '(':
        raise SyntaxError("Expected '(' after function name")
        
    arg_list = []
    wtok.next()
    arg_list.append(assignment(wtok, variables))

    while wtok.get_current() == ",":
        wtok.next()
        arg_list.append(assignment(wtok, variables))

    if wtok.get_current() == ")":
        return arg_list
    else:
        raise SyntaxError("Expected argument list to end with ')'")
        

def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end():
        return result
    else:
        raise SyntaxError("Expected end of line")


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)

    while wtok.get_current() == "=":
        wtok.next()
        if wtok.is_name():
            if wtok.get_current() == "PI" or wtok.get_current() == "E":
                raise SyntaxError("Cant change value of PI or E")
            else:  
                variables[wtok.get_current()] = result
                wtok.next()
            
            # Keeps my vars list sorted, case insensitive
            sorted_dict = sorted(variables.items(), key=lambda item: item[0].lower())
            variables.clear()
            variables.update(sorted_dict)
        else:
            raise SyntaxError("Name of assignment need to be a character or string")  
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ['+', '-']:
        wtok.next()
        if wtok.get_previous() == '+': 
            result = result + term(wtok, variables)
        elif wtok.get_previous() == '-': 
             result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ['*', '/', '%']:
        wtok.next()
        if wtok.get_previous() == '*': 
            result = result*factor(wtok, variables)
        elif wtok.get_previous() == '/':
             value = factor(wtok, variables) 
             if abs(value) == 0:
                raise EvaluationError("Devision by zero")
             else:
                result = result/value
        elif wtok.get_previous() == '%':
            value = factor(wtok, variables) 
            if abs(value) == 0:
               raise EvaluationError("Devision by zero")
            else:
                result = result % value
            
    return result

def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '(':
        wtok.next()       
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
            
    elif wtok.get_current() in functions_1:
        wtok.next()
        if wtok.get_current() == '(':
            result = functions_1[wtok.get_previous()](factor(wtok, variables))
        else:
            raise SyntaxError("Expected '(' after function name")
        
    elif wtok.get_current() in functions_N:
        wtok.next()
        func_name = wtok.get_previous()
        result = functions_N[func_name](arglist(wtok, variables))
        wtok.next()
    
    elif wtok.is_name(): 
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
             raise EvaluationError(
            f"Undefined variable:  \"{wtok.get_current()}\" ")
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
        
    elif wtok.get_current() == '-':
        wtok.next()
        return -factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number, word or '('")  
    return result


# Accessable functions of the calculator
functions_1 = {'cos': math.cos, 'sin': math.sin, 'exp': math.exp, 'log': log, 'fac':fac, 'fib': fib}
functions_N = {'mean': mean, 'max': max, 'min': min, 'sum': sum, "std": std} 
 
         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2Files/MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        print("can not read file")

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print('\n'.join(f"{key}: {value}" for key, value in variables.items()))
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
                
            except EvaluationError as ee:
                print("*** Evaluation error:", ee)
 


if __name__ == "__main__":
    main()
