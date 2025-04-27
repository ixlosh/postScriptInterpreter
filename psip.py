import logging
logging.basicConfig(level = logging.INFO)

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
        raise TypeMismatch("Operand stack is empty! Nothing to copy")

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

def div_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        if op2 != 0:
            res = op1 / op2
            op_stack.append(res)
        else:
            raise TypeMismatch("Division by zero error")
    else:
        raise TypeMismatch("div operation requires at least to operands")

dict_stack[-1]["div"] = div_operation


if __name__ == "__main__":
    repl()