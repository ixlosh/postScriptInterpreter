import logging
logging.basicConfig(level = logging.INFO)

import math

op_stack = []
dict_stack = []
dict_stack.append({})

class ParseFailed(Exception):
    """ Exception while parsing """
    def __init__(self, message):
        super().__init__(message)

class TypeMismatch(Exception):
    """ Exception with types of operators and operands """
    def __init__(self, message):
        super().__init__(message)

class DivisionBy0(Exception):
    """ Exception raised for division by zero """
    def __init__(self, message):
        super().__init__(message)

class IndexMissmatch(Exception):
    """ Exception when the index is not applicable to the main string """
    def __init__(self, message):
        super().__init__(message)

def repl():
    while True:
        user_input = input("REPL> ")
        if user_input.lower() == "quit":
            break
        process_input(user_input)
        logging.debug(f"Operand Stack: {op_stack}")

def process_boolean(input):
    logging.debug(f"Input to process boolean: {input}")
    if input == "true":
        return True
    elif input == "false":
        return False
    else:
        raise ParseFailed("can't parse it into boolean")
    
def process_number(input):
    logging.debug(f"Input to process number: {input}")
    try:
        float_value = float(input)
        if float_value.is_integer():
            return int(float_value)
        else:
            return float_value
    except ValueError:
        raise ParseFailed("can't parse this into a number")
    
def process_code_block(input):
    logging.debug(f"Input to process number: {input}")
    if len(input) >= 2 and input.startswith("{") and input.endswith("}"):
        return input[1:-1].strip().split()
    else:
        raise ParseFailed("can't parse this into a code block")

def process_name_constant(input):
    logging.debug(f"Input to process number: {input}")
    if input.startswith("/"):
        return input
    else:
        raise ParseFailed("Can't parse into name constant")
    
PARSERS = [
    process_boolean,
    process_number,
    process_code_block,
    process_name_constant
]

def process_constants(input):
    for parser in PARSERS:
        try:
            res = parser(input)
            op_stack.append(res)
            return
        except ParseFailed as e:
            logging.debug(e)
            continue
    raise ParseFailed(f"None of the parsers worked for the input {input}")

def add_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        res = op1 + op2
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation add")
    
dict_stack[-1]["add"] = add_operation

def def_operation():
    if len(op_stack) >= 2:
        value = op_stack.pop()
        name = op_stack.pop()
        if isinstance(name, str) and name.startswith("/"):
            key = name[1:]
            dict_stack[-1][key] = value
        else:
            op_stack.append(name)
            op_stack.append(value)
    else:
        raise TypeMismatch("Not enough operands for operation add")
    
dict_stack[-1]["def"] = def_operation

def pop_and_print():
    if(len(op_stack) >= 1):
        op1 = op_stack.pop()
        print(op1)
    else:
        raise TypeMismatch("Stack is empty! nothing to print")
    
dict_stack[-1]["="] = pop_and_print

def lookup_in_dictionary(input):
    top_dict = dict_stack[-1]
    if input in top_dict:
        value = top_dict[input]
        if callable(value):
            value()
        elif isinstance(value, list):
            for item in value:
                process_input(item)
        else:
            op_stack.append(value)
    else:
        raise ParseFailed(f"input {input} is not in dictionary")

def process_input(user_input):
    try:
        process_constants(user_input)
    except ParseFailed as e:
        logging.debug(e)
        try:
            lookup_in_dictionary(user_input)
        except Exception as e:
            logging.error(e)

# New Operations 
# I will implement the functions in the order they appear in the command subset document

# Stack Manipulation

def exch_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op1)
        op_stack.append(op2)
    else:
        raise TypeMismatch("exch requires at least two operands")
    
dict_stack[-1]["exch"] = exch_operation

def pop_operation():
    if len(op_stack) >= 1:
        op_stack.pop()
    else:
        raise TypeMismatch("pop requires at least one operand")
    
dict_stack[-1]["pop"] = pop_operation

def copy_operation():
    if len(op_stack) >= 1:
        n = op_stack.pop()
        if isinstance(n, int) and n >= 0:
            if len(op_stack) >= n:
                copied_elements = op_stack[-n:]
                op_stack.extend(copied_elements)
            else:
                raise TypeMismatch(f"Requires at least {n} elements to copy")
        else:
            raise TypeMismatch("copy requires a non-negative integer argument")
    else:
        raise TypeMismatch("Stack is empty, nothing to copy")

dict_stack[-1]["copy"] = copy_operation

def dup_operation():
    if len(op_stack) >= 1:
        op_stack.append(op_stack[-1])
    else:
        raise TypeMismatch("The stack needs at least one element to duplicate")

dict_stack[-1]["dup"] = dup_operation

def clear_operation():
    op_stack.clear()

dict_stack[-1]["clear"] = clear_operation

def count_operation():
    op_stack.append(len(op_stack))

dict_stack[-1]["count"] = count_operation

# Arithmetic Operations

# add predefined

def div_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        if op2 != 0:
            res = op1 / op2
            op_stack.append(res)
        else:
            raise DivisionBy0("Division by zero error")
    else:
        raise TypeMismatch("div operation requires at least to operands")

dict_stack[-1]["div"] = div_operation

def sub_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        res = op2 - op1
        op_stack.append(res)
    else:
        raise TypeMismatch("sub operations require at least to operands")

dict_stack[-1]["sub"] = sub_operation

def idiv_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op1 = int(op1) # We do this step to ensure that the values going  
        op2 = int(op2) # into idiv are also integers and not floats
        if op1 != 0:
            res = op2 // op1
            op_stack.append(res)
        else:
            raise DivisionBy0("Division by zero error")
    else:
        raise TypeMismatch("idiv requires at least two operands")

dict_stack[-1]["idiv"] = idiv_operation

def mul_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        res = op1 * op2
        op_stack.append(res)
    else:
        raise TypeMismatch("mul requires at least to operands")

dict_stack[-1]["mul"] = mul_operation

def abs_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = abs(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("abs requires at least an operand")

dict_stack[-1]["abs"] = abs_operation

def neg_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = -op1
        op_stack.append(res)
    else:
        raise TypeMismatch("neg requires at least an operand")

dict_stack[-1]["neg"] = neg_operation

def ceiling_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = math.ceil(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("ceiling requires at least an operand")

dict_stack[-1]["ceiling"] = ceiling_operation

def floor_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = math.floor(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("floor requires at least an operand")

dict_stack[-1]["floor"] = floor_operation

def round_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = round(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("roudn requires at least an operand")

dict_stack[-1]["round"] = round_operation

def sqrt_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        if op1 < 0:
            raise TypeMismatch("No real sqrt of a negative number exists")
        else:
            res = math.sqrt(op1)
            op_stack.append(res)
    else:
        raise TypeMismatch("sqrt requires at least an operand")

dict_stack[-1]["sqrt"] = sqrt_operation

# Dictionary Operations

def dict_operation():
    if len(op_stack) >= 1:
        capacity = (int)(op_stack.pop())
        if capacity <= 0:
            raise TypeMismatch("dict requires a positive integer argument for capacity")
        new_dict = {i: None for i in range(capacity)}
        op_stack.append(new_dict)
    else:
        raise TypeMismatch("dict requires at least on operand to determine the capacity")

dict_stack[-1]["dict"] = dict_operation

# This is an overlapping operation. It includes actions for both str and dict operands

def length_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        if isinstance(op1, str):
            op_stack.append(len(op1))
        elif isinstance(op1, dict):
            res = len({k: v for k, v in op1.items() if v is not None})
            op_stack.append(res)
        else:
            raise TypeMismatch("Operand must either be a string or dictionary for length operation.")
    else:
        raise TypeMismatch("length operation requires at least one operand")

dict_stack[-1]["length"] = length_operation


def maxlength_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        if isinstance(op1, dict):
            keys = list(op1.keys()) # I have opted to go with the keys method to find the max length
            if keys:
                min_key = min(keys)
                max_key = max(keys)
                capacity = max_key - min_key + 1
                op_stack.append(capacity)
            else:
                op_stack.append(0)
        else:
            raise TypeMismatch("maxlength requires a dictionary operand")
    else:
        raise TypeMismatch("maxlength operation requires at least an operand to determine the max length")

dict_stack[-1]["maxlength"] = maxlength_operation

def begin_operation():
    new_dict = {}
    dict_stack.append(new_dict)

dict_stack[-1]["begin"] = begin_operation

def end_operation():
    if len(dict_stack) > 1: # This is to prevent popping the global dictionary
        dict_stack.pop()
    else:
        raise TypeMismatch("No dictionary to end")

dict_stack[-1]["end"] = end_operation

def def_operation():
    if len(op_stack) >= 2:
        value = op_stack.pop()
        name = op_stack.pop()
        if isinstance(name, str) and name.startswith("/"):
            key = name[1:]
            dict_stack[-1][key] = value
        else:
            raise TypeMismatch("Defining requires a name starting with a '/'")
    else:
        raise TypeMismatch("def operation requires at least two operands (constant name and variable)")
    
dict_stack[-1]["def"] = def_operation

# String Operations

# length under Dictionary Operations (refer to length under dict for further info)

def get_operation():
    if len(op_stack) >= 2:
        index = op_stack.pop()
        op1 = op_stack.pop()
        if isinstance(op1, str) and isinstance(index, int):
            if 0 <= index < len(op1):
                op_stack.append(op1[index])
            else:
                raise IndexMissmatch("index not applicable to the given string")
        else:
            raise TypeMismatch("get requires a string and an integer index (in that order)")
    else:
        raise TypeMismatch("get operation requires at least two operands")

dict_stack[-1]["get"] = get_operation

def getinterval_operation():
    if len(op_stack) >= 3:
        count = op_stack.pop()
        index = op_stack.pop()
        op1 = op_stack.pop()
        if isinstance(op1, str) and isinstance(index, int) and isinstance(count, int):
            if 0 <= index < len(op1):
                op_stack.append(op1[index:index + count])
            else:
                raise IndexMissmatch("index not applicable to the given string")
        else:
            raise TypeMismatch("getinterval requires a string, an integer index, and an integer count (in that order)")
    else:
        raise TypeMismatch("getinterval operation requires at least three operands")

dict_stack[-1]["getinterval"] = getinterval_operation

def putinterval_operation():
    if len(op_stack) >= 3:
        op2 = op_stack.pop()
        index = op_stack.pop()
        op1 = op_stack.pop()
        if isinstance(op1, str) and isinstance(op2, str) and isinstance(index, int):
            if 0 <= index <= len(op1):
                op_stack.append(op1[:index] + op2 + op1[index + len(op2):]) # We do some splicing to get the desired final string
            else:
                raise IndexMissmatch("index not applicable to the string")
        else:
            raise TypeMismatch("putinterval requires two strings and an integer index (in that order)")
    else:
        raise TypeMismatch("putinterval operation requires at least three operands")

dict_stack[-1]["putinterval"] = putinterval_operation

# Bit and Boolean Operations

def eq_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()
        op_stack.append(op1 == op2)
    else:
        raise TypeMismatch("eq operation requires at least two operands")

dict_stack[-1]["eq"] = eq_operation

def ne_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()
        op_stack.append(op1 != op2)
    else:
        raise TypeMismatch("ne operation requires at least two operands")

dict_stack[-1]["ne"] = ne_operation

def ge_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            op_stack.append(op1 >= op2)
        elif isinstance(op1, str) and isinstance(op2, str):
            op_stack.append(op1 >= op2)
        else:
            raise TypeMismatch("ge operation requires operands of the same type (either both numbers or both strings)")
    else:
        raise TypeMismatch("ge operation requires at least two operands")

dict_stack[-1]["ge"] = ge_operation

def gt_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            op_stack.append(op1 > op2)
        elif isinstance(op1, str) and isinstance(op2, str):
            op_stack.append(op1 > op2)
        else:
            raise TypeMismatch("gt operation requires operands of the same type (either both numbers or both strings)")
    else:
        raise TypeMismatch("gt operation requires at least two operands")

dict_stack[-1]["gt"] = gt_operation

def le_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            op_stack.append(op1 <= op2)
        elif isinstance(op1, str) and isinstance(op2, str):
            op_stack.append(op1 <= op2)
        else:
            raise TypeMismatch("le operation requires operands of the same type (either both numbers or both strings)")
    else:
        raise TypeMismatch("le operation requires at least two operands")

dict_stack[-1]["le"] = le_operation

def lt_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            op_stack.append(op1 < op2)
        elif isinstance(op1, str) and isinstance(op2, str):
            op_stack.append(op1 < op2)
        else:
            raise TypeMismatch("lt operation requires operands of the same type (either both numbers or both strings)")
    else:
        raise TypeMismatch("lt operation requires at least two operands")

dict_stack[-1]["lt"] = lt_operation

def and_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()
        
        if isinstance(op1, bool) and isinstance(op2, bool):
            op_stack.append(op1 and op2)
        elif isinstance(op1, int) and isinstance(op2, int):
            op_stack.append(op1 & op2)
        else:
            raise TypeMismatch("and operation requires operands of (bool ,bool) or (int, int)")
    else:
        raise TypeMismatch("and operation requires at least two operands")

dict_stack[-1]["and"] = and_operation

def not_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        
        if isinstance(op1, bool):
            op_stack.append(not op1)
        elif isinstance(op1, int):
            op_stack.append(~op1)
        else:
            raise TypeMismatch("not operation requires either a boolean or an integer operand")
    else:
        raise TypeMismatch("not operation requires at least one operand")

dict_stack[-1]["not"] = not_operation

def or_operation():
    if len(op_stack) >= 2:
        op2 = op_stack.pop()
        op1 = op_stack.pop()

        if isinstance(op1, bool) and isinstance(op2, bool):
            op_stack.append(op1 or op2)
        elif isinstance(op1, int) and isinstance(op2, int):
            op_stack.append(op1 | op2)
        else:
            raise TypeMismatch("or operation requires operand sof (bool, bool) or (int, int)")
    else:
        raise TypeMismatch("or operation requires at least two operands")

dict_stack[-1]["or"] = or_operation

# True & False operations are predefined

# Flow control Operations



if __name__ == "__main__":
    repl()