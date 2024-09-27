# %%
# Anything iterable can be iterated over with a for loop
# Observe that:
# - list content don't matter
# - that the iterator will always be overwritten by the next item
for i in ['a','b','c',1,2,3,[1,2,3],1.5,2.7]:
    print(f'"i" has the value "{i}" and type "{type(i)}"')

# Iterate over two or more list (with the same length)
# e.g. iterate over a list of coordinates
import numpy as np
image = np.random.randint(0,255,100).reshape(10,10)
x_coordinates = range(10)
y_coordinates = range(10)
for y,x in zip(y_coordinates,x_coordinates):
    print(f'At position x: {x} and y: {y} the intensity value is: {image[y,x]}.')

# %%
# list comprehension
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)
# use list comprehension
squares = [i**2 for i in range(10)]
print(squares)

# usefull for creating an filepath iterable
from pathlib import Path
[file for file in Path().cwd().iterdir()]

# %%
# for loop with if
for x in range(10):
    if x != 0:
        print(f'X: {x}, 1/X: {1/x}')

# for loop with if and else
for x in range(10):
    if x == 0:
        print(f'X: {x}, 1/X: Division by {x} not defined.')
    else:
        print(f'X: {x}, 1/X: {1/x}')

# %%
# for loop with continue and break
# Usage:
# - skip files/data for processing
# - debugging
# continue
for x in range(10):
    if x==0:
        continue
    print(f'X: {x}, 1/X: {1/x}')

# break
for x in range(10):
    if x==3:
        break
    print(x)

# %%
# Nested loops
for x in range(1,4):
    for y in range(1,4):
        print(f'X: {x}, Y: {y}, X*Y: {x*y}')

# Nested lists
for sublist in [[1,2,3],[4,5,6],[7,8,9]]:
    for i in sublist:
        print(i)

# np.array
# Observe that you iterate only over the first dimension when using simple loop
array = np.random.randint(0,10,100).reshape(10,10)
print(array.shape)
for i in array:
    print(i)

for row in array:
    for i in row:
        print(i)

# %%
# Looping over pandas DataFrame
# Observe that
# - looping with iterrows always gives an index
# - the second variable will always be a pandas Series object
import pandas as pd
df = pd.DataFrame({
    'a':[1,2,3],
    'b':[4,5,6]})
print(df)
for i,row in df.iterrows():
    print(type(row))
    value_a = row['a']
    value_b = row['b']
    print(f'Row index {i}\nColumn value "a": {value_a} and Column value "b": {value_b}')