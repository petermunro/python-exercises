## Sequences

# Write code to answer these practice questions:

# 1. Lists

# 1. Create a list of the first 10 numbers (0-9).

l1 = list(range(10))

# 2. Append the number 10 to the list.

l1.append(10)

# 3. Remove the fifth element from the list.

del l1[4]

# 4. Reverse the list.

l1.reverse()

# 5. Sort the list.

l1.sort()


# 2. Splitting and Joining

# 1. Given the string `"Python is fun"`, split it into a list of words.

words = "Python is fun".split()

# 2. Given the list `['Python', 'is', 'fun']`, join it back into a single string.

" ".join(words)

# 3. Given a string of numbers separated by commas, e.g., `"1,2,3,4,5"`, convert it into a list of integers.

num_strings = "1,2,3,4,5".split(",")
list(map(int, num_strings))


# 3. Tuples

# 1. Create a tuple with three elements.

t1 = "one", True, 3

# 2. Try to change the second element of the tuple. What happens?

t1[1] = "two"   # TypeError: 'tuple' object does not support item assignment

# 3. Convert the tuple into a list.

list(t1)


# 4. Ranges

# 1. Create a range of numbers from 0 to 10.

r1 = range(10)

# 2. Convert the range to a list.

list(r1)

# 3. Use a range to create a list of all even numbers from 0 to 20.

list(range(0, 20, 2))


# 5. Common Sequence Operations

# 1. Given the list `[1, 2, 3, 4, 5]`, find the index of the number `3`.

l1 = [1, 2, 3, 4, 5]
l1.index(3)

# 2. Check if the number `6` is in the list.

6 in l1

# 3. Count the number of `3`s in the list `[1, 2, 3, 3, 4, 5, 3]`.

[1, 2, 3, 3, 4, 5, 3].count(3)


# 6. Slicing

# 1. Given the list `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, get a slice from index `3` to `7`.

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1[3:7]

# 2. Get the last three elements of the list.

l1[-3:]

# 3. Get every second element of the list.

l1[::2]


# 7. Unpacking

# 1. Given the tuple `(1, 2, 3)`, unpack it into three variables `a`, `b`, and `c`.

a, b, c = (1, 2, 3)

# 2. Try to unpack a list of four elements into three variables. What happens?

a, b, c, d = (1, 2, 3)        # ValueError: not enough values to unpack (expected 4, got 3)


# 8. Sequence Modification Operations

# 1. Given the list `[1, 2, 3]`, change the last element to `4`.

l1 = [1, 2, 3]
l1[-1] = 4

# 2. Given the list `[1, 2, 3]`, insert `1.5` as the second element.

l1.insert(1, 1.5)

# 3. Remove the first element of the list `[1, 2, 3, 4, 5]`.

del l1[0]
