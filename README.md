# postScriptInterpreter
This is the README file for my postscript interpreter implementation for CPTS 355 mini project. Below are the explanations of the calls the interpreter natively understands.

## Functions and Operations

### REPL
- `repl` : Read-Eval-Print Loop, reads user input, processes it, repeats until `quit`.

### Error Handling
- `ParseFailed` : raised when an input token cannot be parsed.
- `TypeMismatch` : raised when an operation sees the wrong number or types of operands.
- `DivisionBy0` : raised when a division or integer-division by zero is attempted.
- `IndexMissmatch` : raised when a string index or interval is out of bounds.

### Stack Manipulation
- `add` : pop two values, push their sum.
- `exch` : swap the top two values on the stack.
- `pop` : remove the top value.
- `copy` : duplicate the top _n_ values.
- `dup` : duplicate the top value.
- `clear` : remove all values.
- `count` : push the current stack depth.

### Arithmetic
- `sub` : pop two values, push their difference.
- `mul` : pop two values, push their product.
- `div` : pop two values, push their quotient (real division).
- `idiv` : pop two values, convert to int, push integer quotient.
- `abs` : pop one value, push its absolute.
- `neg` : pop one value, push its negation.
- `ceiling` : pop one value, push ⌈_x_⌉.
- `floor` : pop one value, push ⌊_x_⌋.
- `round` : pop one value, push round(_x_).
- `sqrt` : pop one value, push √_x_ (error if _x_<0).

### Dictionary Management
- `dict` : pop an integer _n_, create a new dictionary of capacity _n_ and push it on the dict stack.
- `begin` : start a new dictionary scope.
- `end` : end the current dictionary scope.
- `def` : pop `/name` and a value, bind in the current dict.
- `length` : for strings: pop `"(…)"`, push its length; for dicts: push number of bindings.
- `maxlength` : push the capacity of the current dict.

### String Operations
- `get` : pop `"(…)"` and _i_, push the character at index _i_.
- `getinterval` : pop `"(…)"`, start index, count; push the substring.
- `putinterval` : pop `"(…)"`, start index, `"(…)"`; replace that interval and push the new string.

### Bit & Boolean
- `eq` : pop two values, push equality.
- `ne` : pop two values, push inequality.
- `gt` : pop two values (numbers or strings), push greater-than comparison.
- `ge` : pop two values (numbers or strings), push greater-than-or-equal comparison.
- `lt` : pop two values (numbers or strings), push less-than comparison.
- `le` : pop two values (numbers or strings), push less-than-or-equal comparison.
- `and` : logical AND on booleans, bitwise AND on integers.
- `or` : logical OR on booleans, bitwise OR on integers.
- `not` : logical NOT on booleans, bitwise NOT on integers.

### Flow Control
- `if` : pop `{…}` and a boolean; if true, execute the code string.
- `ifelse` : pop two `{…}` strings and a boolean; execute the first or second.
- `for` : pop starting, step, limit, `{…}`; loop _i_ from start to limit by step, executing the code each time.
- `repeat` : pop `{…}` and an integer _n_; execute the code _n_ times.

### Scoping Controls
- `dynamicon` : switch to dynamic scoping (default).
- `dynamicoff` : switch to lexical scoping.
- `scopingstatus` : print whether scoping is dynamic or lexical.

