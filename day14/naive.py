from collections import Counter

def read_input(input_file):
    with open(input_file, 'r') as f:
        # template = Chain(element for element in next(f).strip())
        template = next(f).strip()
        insertion_rules = {}
        for line in f.read().strip().splitlines():
            pair, insertion = line.split(' -> ')
            insertion_rules[pair] = pair[0] + insertion + pair[1]
        return template, insertion_rules

def simulate_polymerization(polymer, insertion_rules, steps=10):
    for step in range(steps):
        polymer = apply_insertion_rules(polymer, insertion_rules)
    
    counts = Counter(str(element) for element in polymer).most_common()
    print(counts)
    result = counts[0][1] - counts[-1][1]
    return result

def apply_insertion_rules(polymer, insertion_rules):
    previous_element = polymer.head
    next_element = polymer.head.next
    while next_element:
        pair = f"{previous_element}{next_element}"
        print(pair)
        inserted_element = Link(insertion_rules[pair])
        previous_element.insert_after(inserted_element)
        previous_element = next_element
        next_element = next_element.next

    return polymer



class Chain:
    def __init__(self, items):
        items = iter(items)
        self.head = Link(next(items))
        previous = self.head
        for item in items:
            previous = self.insert(Link(item), previous=previous)
        
        self.tail = previous
    
    def insert(self, link, previous=None):
        if previous is None:
            previous = self.tail
        
        previous.next = link
        link.previous = previous
        return link
    
    def iter_pairs(self):
        for element in self:
            first = element
            second = element.next
            if second is None:
                break
            else:
                yield first, second
    
    def __iter__(self):
        yield from self.head



class Link:
    def __init__(self, content):
        self.content = content
        self.next = None
        self.previous = None
    
    def insert_after(self, link):
        old_next = self.next
        self.next = link
        link.previous = self
        link.next = old_next
        if old_next is not None:
            old_next.previous = link
        
        return link

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next
    
    def __next__(self):
        if self.next is None: 
            raise StopIteration
        else:
            return self.next
    
    def __repr__(self):
        return f"Link({self.content})"

    def __str__(self):
        return str(self.content)

if __name__ == '__main__':
    polymer, insertion_rules = read_input('input.txt')
    result = simulate_polymerization(polymer, insertion_rules, steps=40)
