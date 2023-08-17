class SnailfishNumber:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def magnitude(self):
        a = self.left if self.is_left_regular else self.left.magnitude
        b = self.right if self.is_right_regular else self.right.magnitude
        return 3*a + 2*b

    @property
    def is_right_regular(self):
        return isinstance(self.right, int)

    @property
    def is_left_regular(self):
        return isinstance(self.left, int)
    
    @property
    def depth(self):
        result = 1
        if not self.is_left_regular:
            result = 1 + self.left.depth
        if not self.is_right_regular:
            result = max(result, 1 + self.right.depth)
        return result
    
    def explode(self):
        pass

    def split(self):
        pass

    @classmethod
    def parse(cls, line):
        pass

    def __add__(self, other):
        return self.__class__(self, other)


def read_input(input_file):
    pass

def parse_list_of_lists_string(line):
    pass