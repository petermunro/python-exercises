# # Sets and Dictionaries

# Write code to answer these practice questions:

# ## 1. Creating Sets

# 1. Create a set, `set1` containing the numbers 1, 2, and 3.

set1 = set((1, 2, 3))
# or:
set1 = {1, 2, 3}

# 2. Create a set, `set2` from the list `[ 4, 4, 1, 3, 3, 3, 7, 2, 2]`. Verify that this set does not contain duplicates.

set2 = set([ 4, 4, 1, 3, 3, 3, 7, 2, 2])


# ## 2. Set Operations

# 1. Add the number 5 to `set1`.

set1.add(5)

# 2. Remove the number 2 from the set.

set1.remove(2)

# 3. Check if the number 5 is in the set.

5 in set1

# 4. Given `set1` and `set2`, find their union, intersection, and difference.

set1.union(set2)
set1.intersection(set2)
set1.difference(set2)


# ## 3. Frozensets

# 1. Create a frozenset containing the numbers 1, 2, and 3.

fs1 = frozenset([1, 2, 3])
# or:
fs1 = frozenset((1, 2, 3))

# 2. Try adding the number 5 to the frozenset. What happens?

fs1.add(5)        # AttributeError: 'frozenset' object has no attribute 'add'


# ## 4. Set Comprehensions

# 1. From this list of numbers, create a set of their squares:

numbers = [1, 2, 3, 4, 5]
squares = {i * i for i in numbers}

# 2. From this list of numbers, produce a set of just the positive numbers : `[-4, -2, 0, 2, 4, 6, 8]`

num_list = [-4, -2, 0, 2, 4, 6, 8]
positives = {i for i in num_list if i > 0}

# 3. Create a set of unique tuples from these:

tuples = [(1, 2), (1, 2), (2, 3), (3, 4), (2, 3)]
unique_tuples = {tuple for tuple in tuples}

# 4. Create a set of all of the uppercase characters in the string `"Present Fears Are Less Than Horrible Imaginings."`

str1 = "Present Fears Are Less Than Horrible Imaginings."
all_uppers = { char for char in str1 if char.isupper() }

# 5. Find all of the unique words in this string: `"double, double toil and trouble; fire burn and cauldron bubble."`.




# ## 4. Dictionaries

# 1. Create a dictionary with keys `'a'`, `'b'`, and `'c'` and values `1`, `2`, and `3`.

dict1 = {'a': 1, 'b': 2, 'c': 3}
# or:
dict1 = dict(a=1, b=2, c=3)

# 2. Add a key `'d'` with the value `4` to the dictionary.

dict1['d'] = 4

# 3. Remove the key `'b'` and its associated value from the dictionary.

del dict1['b']

# 4. Check if the key `'e'` is in the dictionary.

'e' in dict1

# 5. Loop through the dictionary and print each key-value pair.

for key, value in dict1.items():
    print("%s: %s" % (key, value))


# 6. Given these lists:

countries = ['France', 'Germany', 'Spain', 'Italy', 'United Kingdom', 'Netherlands', 'Belgium', 'Portugal', 'Austria', 'Greece']
capitals = ['Paris', 'Berlin', 'Madrid', 'Rome', 'London', 'Amsterdam', 'Brussels', 'Lisbon', 'Vienna', 'Athens']

#  create a dictionary containing the countries as keys and the capital cities as values.

country_capitals = dict(zip(countries, capitals))


# ## 5. Set and Dictionary Comprehensions

# 1. Use a set comprehension to create a set of all the even numbers from 0 to 20.

evens = { i for i in range(20) if i % 2 == 0}

# 2. Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are the square of the keys.

squares_dict = { i: i * i for i in range(1, 11) }
