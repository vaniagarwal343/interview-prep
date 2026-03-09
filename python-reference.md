# Python Reference (for Java people)

## Variables

```python
x = 5           # no type declaration
s = "hello"     # single or double quotes both work
a, b = 1, 2     # multiple assignment
a, b = b, a     # swap
```

## If/Else

```python
if x > 0:
    print("pos")
elif x == 0:
    print("zero")
else:
    print("neg")
```

## For Loops

```python
# range
for i in range(5):        # 0, 1, 2, 3, 4
for i in range(2, 5):     # 2, 3, 4
for i in range(0, 10, 2): # 0, 2, 4, 6, 8

# iterate list
for val in nums:
    print(val)

# with index
for i, val in enumerate(nums):
    print(i, val)

# while
while left < right:
    left += 1   # no ++ operator
```

## Lists

```python
nums = [1, 2, 3]
nums.append(4)          # [1, 2, 3, 4]
nums.pop()              # removes & returns last -> 4
nums.pop(0)             # removes & returns index 0 -> 1
len(nums)               # 2
nums[0]                 # first element
nums[-1]                # last element
nums[1:3]               # slice [index 1, index 3)

# list comprehension
squares = [x * x for x in range(5)]

# init with size
dp = [0] * 10
grid = [[0] * cols for _ in range(rows)]  # 2D
```

## Dictionaries

```python
d = {}
d = {"a": 1, "b": 2}

d["c"] = 3              # set
val = d["a"]             # get (KeyError if missing)
val = d.get("z", 0)     # get with default

"a" in d                 # check key -> True

for k in d:             # iterate keys
for k, v in d.items():  # iterate key-value pairs

del d["a"]               # delete key

# counting pattern
from collections import Counter
counts = Counter("aabbc")  # {'a': 2, 'b': 2, 'c': 1}

# default dict
from collections import defaultdict
graph = defaultdict(list)
graph[0].append(1)       # no need to check if key exists
```

## Functions

```python
def add(a, b):
    return a + b

# multiple return values
def divmod(a, b):
    return a // b, a % b

q, r = divmod(7, 3)
```

## Common Gotchas

```python
# indentation IS the syntax. no braces.

# booleans are capitalized
True, False, None        # not true, false, null

# logical operators are words
if a and b:
if a or b:
if not a:

# integer division truncates toward negative infinity
7 // 2    # 3
-7 // 2   # -4  (different from Java's -3)

# infinity
float('inf')
float('-inf')

# None checks
if x is None:       # preferred
if x is not None:   # not `x != None`

# strings are immutable (like Java)
# lists are passed by reference
# `=` on a list does NOT copy it
a = [1, 2, 3]
b = a        # b points to same list
b = a[:]     # shallow copy
b = a.copy() # also shallow copy
```
