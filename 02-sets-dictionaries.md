# Sets and Dictionaries

Write code to answer these practice questions:

## 1. Creating Sets

1. Create a set, `set1` containing the numbers 1, 2, and 3.

2. Create a set, `set2` from the list `[ 4, 4, 1, 3, 3, 3, 7, 2, 2]`. Verify that this set does not contain duplicates.

## 2. Set Operations

1. Add the number 5 to `set1`.

2. Remove the number 2 from the set.

3. Check if the number 5 is in the set.

4. Given `set1` and `set2`, find their union, intersection, and difference.

## 3. Frozensets

1. Create a frozenset containing the numbers 1, 2, and 3.

2. Try adding the number 5 to the frozenset. What happens?

## 4. Set Comprehensions

1. From this list of numbers, create a set of their squares:

   ```python
   numbers = [1, 2, 3, 4, 5]
   ```

2. From this list of numbers, produce a set of just the positive numbers : `[-4, -2, 0, 2, 4, 6, 8]`

3. Create a set of unique tuples from these:

   ```python
   tuples = [(1, 2), (1, 2), (2, 3), (3, 4), (2, 3)]
   ```

4. Create a set of all of the uppercase characters in the string `"Present Fears Are Less Than Horrible Imaginings."`

5. Find all of the unique words in this string: `"double, double toil and trouble; fire burn and cauldron bubble."`.

   > Hint: You can start with this string:
   > "double double toil and trouble fire burn and cauldron bubble"
   > Then investigate the `strip()` function.

## 4. Dictionaries

1. Create a dictionary with keys `'a'`, `'b'`, and `'c'` and values `1`, `2`, and `3`.

2. Add a key `'d'` with the value `4` to the dictionary.

3. Remove the key `'b'` and its associated value from the dictionary.

4. Check if the key `'e'` is in the dictionary.

5. Loop through the dictionary and print each key-value pair.

6. Given these lists:

   ```python
   countries = ['France', 'Germany', 'Spain', 'Italy', 'United Kingdom', 'Netherlands', 'Belgium', 'Portugal', 'Austria', 'Greece']
   capitals = ['Paris', 'Berlin', 'Madrid', 'Rome', 'London', 'Amsterdam', 'Brussels', 'Lisbon', 'Vienna', 'Athens']
   ```

   create a dictionary containing the countries as keys and the capital cities as values.

## 5. Set and Dictionary Comprehensions

1. Use a set comprehension to create a set of all the even numbers from 0 to 20.

2. Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are the square of the keys.
