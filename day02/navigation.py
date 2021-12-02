
class Submarine:
    """Models the navigation of a Submarine"""
    INPUT_FILE = 'input.txt'

    def __init__(self, horizontal=0, depth=0, aim=0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def read_orders(self, order_file=INPUT_FILE):
        with open(order_file, 'r') as f:
            for line in f:
                order, value = line.split()
                yield order, int(value)

    def update_position_simple(self, order, value):
        print(order, type(order).__name__, value, type(value).__name__)
        if order == 'forward':
            self.horizontal += value
        elif order == 'up':
            self.depth -= value
        elif order == 'down':
            self.depth += value

    def update_position(self, order, value):
        print(order, value)
        if order == 'forward':
            self.horizontal += value
            self.depth += (self.aim * value)
        elif order == 'up':
            self.aim -= value
        elif order == 'down':
            self.aim += value

    def multiply_position(self):
        return self.horizontal * self.depth
    
    def __repr__(self) -> str:
        attrs = ('horizontal', 'depth', 'aim')
        attr_strings = (f"{name}={getattr(self, name)}" for name in attrs)
        return f"Submarine({', '.join(attr_strings)})"

if __name__ == '__main__':
    sub = Submarine()
    print('Initial', sub)
    for order, value in sub.read_orders():
        sub.update_position(order, value)
        print(sub)
    
    print(sub.multiply_position())