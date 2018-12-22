from functools import reduce

frequencies = []
with open('input.txt', 'r') as input_values:
    for frequency in input_values.readlines():
        frequencies.append(int(frequency))

product = reduce((lambda x, y: x+y), frequencies)
print(product)
