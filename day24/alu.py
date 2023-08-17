import re
from operator import add, mul, mod, eq, floordiv

NULL_PATTERNS = (r"add \w 0", r"(mul|div) \w 1")

class Programme:
    OPERATORS = {
        'add': add,
        'mul': mul,
        'mod': mod,
        'eql': eq,
        'div': floordiv
    }
    def __init__(self, instructions):
        self.digit_iter = None
        self.variables = {}  # {var: 0 for var in ('w', 'x', 'y', 'z')}
        self.mutations = [
            self.interpret(instruction) for instruction in instructions
            # if not self.is_null_operation(instruction) 
        ]
    
    @classmethod
    def from_instruction_file(cls, file_path):
        with open(file_path, 'r') as f:
            instructions = f.read().splitlines()
            return cls(instructions)
    
    def interpret(self, instruction):
        line = instruction.split()
        if len(line) == 2:  # Input statement
            self.variables[line[-1]] = 0
            result = self.inp(line[-1])
        else:
            op, store_var, value = line
            try:
                value = int(value)
            except ValueError as e:
                self.variables[value] = 0                
            self.variables[store_var] = 0
            result = self.mutation(op, store_var, value)
        return result
    def is_null_operation(self, instruction):
        result = False
        for null_pattern in NULL_PATTERNS:
            if re.match(null_pattern, instruction):
                result = True
                break
        else:
            line = instruction.split()
        return False
    def reset(self):
        self.variables = {key: 0 for key in self.variables}
    def inp(self, var):
        print('Setting up inp')
        def inner():
            self.variables[var] = next(self.digit_iter)
        return inner
        
    def mutation(self, op, var, value):
        print(f"Setting up mutation({op}, {var}, {value})")
        def inner():
            val = value if isinstance(value, int) else self.variables[value]
            operation = self.OPERATORS[op]
            self.variables[var] = int(operation(self.variables[var], val))
        return inner
    
    def __call__(self, number):
        self.digit_iter = (int(i) for i in str(number))
        for mutation in self.mutations:
            try:
                mutation()
            except StopIteration as e:
                raise ValueError('Input not long enough for programme')
        return self.variables

def find_lowest_input(rng):
    monad = Programme.from_instruction_file('cleaned_input.txt')
    for number in rng:
        print(f"Trying {number}")
        monad.reset()
        vars = monad(number)
        if vars['z'] == 0:
            print(f"Number {number} is valid")
            return number

if __name__ == '__main__':
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        results = []
        minimum = 99999819710267
        while minimum > 9999999999999:
            maximum = minimum -1
            minimum = maximum - 9999999999999 - 1
            rng = range(maximum, minimum, -1)
            result = executor.submit(find_lowest_input, rng)
            results.append(result)

    for r in results:
        print(r)