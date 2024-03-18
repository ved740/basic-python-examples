def print_three_things(**kwargs):
    print(f"First: {kwargs['first']}")
    print(f"Second: {kwargs['second']}")
    print(f"Third: {kwargs['third']}")
arguments={'first': 'Ice Cream', 'second': 'Pizza', 'third': 'Burger'}
print_three_things(**arguments)
