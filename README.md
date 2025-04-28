## Functions and Operations

### REPL
- `repl`: Starts the REPL, reads input, processes it, and continues until `quit`.

### Error Handling
- `ParseFailed`: Raised when input parsing fails.
- `TypeMismatch`: Raised for incorrect operand types or numbers.
- `DivisionBy0`: Raised when division by zero is attempted.
- `IndexMissmatch`: Raised when a string index is out of bounds.

### Stack Operations
- `add`: Adds the top two values on the stack.
- `exch`: Swaps the top two values.
- `pop`: Removes the top value from the stack.
- `copy`: Duplicates the top n values.
- `dup`: Duplicates the top value.
- `clear`: Clears the stack.
- `count`: Pushes the current stack size.

### Arithmetic Operations
- `sub`: Subtracts the top two values on the stack.
- `mul`: Multiplies the top two values on the stack.
- `div`: Divides the top two values on the stack.
- `idiv`: Integer division for the top two values.
- `abs`: Pushes the absolute value of the top value.
- `neg`: Negates the top value.
- `ceiling`: Pushes the ceiling of the top value.
- `floor`: Pushes the floor of the top value.
- `round`: Rounds the top value.
- `sqrt`: Pushes the square root of the top value (error if negative).

### Dictionary Operations
- `dict`: Creates a new dictionary with a given size and pushes it to the stack.
- `begin`: Starts a new dictionary scope.
- `end`: Ends the current dictionary scope.
- `def`: Defines a new binding in the current dictionary.
- `length`: Pushes the length of a string or dictionary size.
- `maxlength`: Pushes the maximum size of the current dictionary.

### String Operations
- `get`: Retrieves a character from a string at a specific index.
- `getinterval`: Retrieves a substring based on start index and length.
- `putinterval`: Replaces a substring within a string.

### Bitwise & Boolean Operations
- `eq`: Checks if the top two values are equal.
- `ne`: Checks if the top two values are not equal.
- `gt`: Checks if the first value is greater than the second.
- `ge`: Checks if the first value is greater than or equal to the second.
- `lt`: Checks if the first value is less than the second.
- `le`: Checks if the first value is less than or equal to the second.
- `and`: Performs logical AND for booleans or bitwise AND for integers.
- `or`: Performs logical OR for booleans or bitwise OR for integers.
- `not`: Performs logical NOT for booleans or bitwise NOT for integers.

### Flow Control
- `if`: Executes a code block if the condition is true.
- `ifelse`: Executes one of two code blocks based on a condition.
- `for`: Loops over a range and executes a code block for each iteration.
- `repeat`: Repeats a code block a specified number of times.

### Scoping Controls
- `dynamicon`: Enables dynamic scoping.
- `dynamicoff`: Disables dynamic scoping.
- `scopingstatus`: Displays the current scoping type (dynamic or lexical).
