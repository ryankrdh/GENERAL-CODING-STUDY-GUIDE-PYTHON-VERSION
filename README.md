# PYTHON-STUDY-GUIDE- Hyunmin Kim 

&nbsp;
#
#

# DATA STRUCTURES

#
&nbsp;
#
# DATA STRUCTURES: Basic Data Types
>There are 5 main basic data types.

&nbsp;
## 1. Numeric
- **Integer**: A whole number without a decimal point. Example: 5, -12, 0.
- **Float**: A number with a decimal point. Example: 3.14, -0.5, 2.0.
- **Complex Number**: A number that has both a real part (like regular numbers) and an imaginary part (like numbers with 'i' in math). For example, 2+3i or -1-2i.

&nbsp;
## 2. Dictionary
A collection of key-value pairs. Example: `{'apple': 2, 'banana': 3}`.
- **Keys**: Strings, numbers, and tuples. Immutable data types.
- **Values**: Any types can be a value.
- **Examples**:
    | Syntax | | | | Returns |
    |-|-|-|-|-|
    |`empty_dict = {}`| | | | `{}`|
    |`my_dict = dict([('a', 1), ('b', 2)])`| | | | `{'a': 1, 'b': 2}` |
    |`my_dict = {'a': 1, 'b': 2}`| | | | `{'a': 1, 'b': 2}` |

&nbsp;
## 3. Boolean
- **Boolean**: A data type that can only have two values: True or False.
    - Values that evaluate to **False** are considered **Falsy**.
    - Values that evaluate to **True** are considered **Truthy**.

### Falsy Values Include:

1. **Sequences and Collections**:
   - Empty lists `[]`
   - Empty tuples `()`
   - Empty dictionaries `{}`
   - Empty sets `set()`
   - Empty strings `""`
   - Empty ranges `range(0)`

2. **Numbers**: Zero of any numeric type.
   - Integer: `0`
   - Float: `0.0`
   - Complex: `0j`

3. **Constants**:
   - `None`
   - `False`

### Truthy Values Include:

- Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
- Numeric values that are not zero.
- Constant: `True`

&nbsp;
- **Examples**:
  | Syntax | | Description | | Returns |
  |---|---|---|---|---|
  |`bool('Hello')`| |Evaluate a string| | `True`|
  |`bool(7)`| |Evaluate an integer (non-zero)| | `True`|
  |`bool(0)`| |Evaluate zero| | `False`|
  |`bool([])`| |Evaluate an empty list| | `False`|
  |`bool({7,4})`| |Evaluate a non-empty set| | `True`|
  |`bool(-4)`| |Evaluate a negative integer| | `True`|
  |`bool(0.0)`| |Evaluate zero as a float| | `False`|
  |`bool(None)`| |Evaluate `None`| | `False`|
  |`bool(1)`| |Evaluate integer one| | `True`|
  |`bool(range(0))`| |Evaluate an empty range| | `False`|
  |`bool(set())`| |Evaluate an empty set| | `False`|
  |`bool([1,2,3,4])`| |Evaluate a non-empty list| | `True`|

&nbsp;
## 4. Set
- **Sets**: Unordered, immutable, and do NOT allow duplicate values.
- **Examples**:
  | Syntax | | Description | | Returns |
  |-|-|-|-|-|
  |`empty_set = set()`| |Initialize an empty set| | `set()`|
  |`my_set = {1, 2}`| |Initialize a set with elements| | `{1, 2}` |
  |`my_set = set([1, 2, 2])`| |Change list into set| | `{1, 2}` |

&nbsp;
## 5. Sequence Type
- **Strings**: Ordered, immutable, and allow duplicate values.
  | Syntax | |Description| | Returns |
  |-|-|-|-|-|
  |`string = 'Hello`| |Initilize a variable with a string| | `Hello`|
  |`string[1]`| |Locate and Returns a string by INDEX| | `e`|
- **Tuple**: Ordered, immutable, and allow duplicate values.
- **Examples**:
  | Syntax | | | | Returns |
  |-|-|-|-|-|
  |`empty_tuple = ()`| |Initialize an empty tuple| | `()`|
  |`my_tuple = (1, 2, 2)`| |Initialize a tuple with elements| | `(1, 2, 2)` |
  |`my_tuple = tuple([1, 2, 2])`| |Change list into tuple| | `(1, 2, 2)` |
- **List**: Ordered, mutable, and allow duplicate values.
- **Examples**:
  | Syntax | |Description| | Returns |
  |-|-|-|-|-|
  |`empty_list = []`| |Initilize an empty list| | `[]`|
  |`my_list = [1, 2, 2]`| |Initialize a list with elements| | `[1, 2, 2]` |
  |`my_list = list([1, 2, 2])`| |Change tuple into list| | `[1, 2, 2]` |

&nbsp;
#
# DATA STRUCTURES: Lists
&nbsp;
## List Methods (Most Commonly Used)
*Notice how some methods CAN be saved to a variable because they return a result instead of directly changing the list.*

| Operation | | Description | | Returns |
  |-|-|-|-|-|
|`nums = [1, 3, 2, 3]`||Initialize list named nums `[1, 3, 2, 3]`||`[1, 3, 2, 3] (Original List)`|
|`nums.append(2)`||Adds an element to the end of the list||`[1, 3, 2, 3, 2]`|
|`nums.extend([4, 5])`||Extends the list by appending elements from the iterable||`[1, 3, 2, 3, 4, 5]`|
|`nums.insert(1,5)`||Inserts `5` at the INDEX `1`||`[1, 5, 3, 2, 3]`|
|`nums_res = nums.pop()`||Removes and returns the last item in the list||`3`|
|`nums.pop()`||Removes the last item in the list||`[1, 3, 2]`|
|`nums.pop(0)`||Removes the item at INDEX `0` in the list||`[3, 2, 3]`|
|`nums.remove(3)`||Removes the first VALUE of `3`||`[1, 2, 3]`|
|`nums_res = nums.index(2)`||Returns the INDEX of the first VALUE of `2`||`2`|
|`nums.sort()`||Sorts the items of the list in place||`[1, 2, 3, 3] (Sorted)`|
## List Methods (Least Commonly Used)
| Operation | | Description | | Returns |
  |-|-|-|-|-|
|`nums_res = nums.count(3)`||Returns the number of times `3` is present in the list||`2`|
|`nums_res = nums.copy()`||Returns a copy of the list||`[1, 3, 2, 3]`|
|`nums.reverse()`||Reverses the elements of the list in place||`[3, 2, 3, 1]`|
|`nums.clear()`||Removes all the elements from the list||[]|
|`nums_res = nums.clear()`||Removes all the elements from the list||None|

NOTE:
    
- Python's `sort()` method uses Tim Sort, which is a combination of both merge sort and insertion sort. That is why the time complexity is O(n log n) when you use the `sort()` method.

- `list.sort()` changes the list itself to be sorted, but it doesn't return anything useful. 
- On the other hand, `sorted()` makes a new sorted list without changing the original list. Also, `sorted()` can sort any type of collection, while `list.sort()` only works on lists.
## Closer look at .sort() and sorted()
| Operation | | Description | | Returns |
  |-|-|-|-|-|
|`nums.sort()`||Sorts the items of the list in place||`[1, 2, 3, 3] (Sorted)`|
|`nums_res = nums.sort()`||Sorts the items of the list in place BUT no returns||`Returns None (Original list is sorted)`|
|`sorted(nums)`||returns a sorted list of the specified iterable object.||`[1, 3, 2, 2] (Original list is NOT sorted)`|
|`nums = sorted(nums)`||returns a sorted list of the specified iterable object.||`[1, 2, 3, 3] (Sorted)`|



## Time Complexities for List Methods
>NOTE: Amortized analysis ensures that over a series of operations, the average cost per operation remains low, even if a few operations are expensive.

![Untitled](https://user-images.githubusercontent.com/47276307/172330098-1c5f0a6e-7f80-4f4f-9be6-1d734e2c70cd.jpg)

## Array vs List in Python

### Array
- **Definition**: An array is a collection of items stored at contiguous memory locations. In Python, arrays are specifically used to store elements of the *SAME* data type.
- **Import**: Requires importing the `array` module or `numpy` for more functionality.
- **Performance**: Generally faster for numerical operations and large datasets due to fixed data type.
- **Use cases**: Suitable for mathematical operations and where memory efficiency is critical.

### List
- **Definition**: A list is a collection of items which can be of *DIFFERENT* data types. Lists are built-in data structures in Python.
- **Import**: No need to import any module to use lists.
- **Performance**: Slower compared to arrays when dealing with large datasets or numerical operations.
- **Use cases**: Perfect for general use cases where a collection of diverse items is needed.

&nbsp;
#
# DATA STRUCTURES: List or String Slicing in Python
&nbsp;

Python slicing allows you to select parts of an array (or list) with ease. Here's a breakdown:

- **Basic Slicing**:
  - `a[start:stop]`: Gets items from index `start` to `stop - 1`.
  - `a[start:]`: Gets items from `start` to the end.
  - `a[:stop]`: Gets items from the beginning to `stop - 1`.
  - `a[:]`: Copies the whole array.

- **Advanced Slicing with Step**:
  - `a[start:stop:step]`: Gets items from `start` to `stop - 1`, skipping items by `step`.

**Key Points**:
- The `stop` index isn't included in the selection.
- Default `step` is 1, selecting consecutive items.
- Negative `start` or `stop` counts from the end.
- Negative `step` reverses the direction.

&nbsp;
- **Negative Indices Examples**:
  >`a = [4, 2, 6, 8, 2, 3]`

  >`b = ['a', 'b', 'c', 'd', 'e', 'f']`

| Syntax | Description | Returns |
|--------|-------------|-------|
| `a[1:3]` | Select items from index 1 to 2 (end exclusive) | `[2, 6]` |
| `a[2:6]` | Select items from index 2 to 5 | `[6, 8, 2, 3]` |
| `a[2:6:2]` | Select items from index 2 to 5 with step 2 | `[6, 2]` |
| `a[0:8:3]` | Select items from index 0 to 7 with step 3 | `[4, 8]` |
| `a[:-2]` | Select everything except the last two items | `[4, 2, 6, 8]` |
| `a[:-2:2]` | Select every second item, stopping before the last two | `[4, 6]` |
| `a[::4]` | Select every fourth item from start to end | `[4, 2]` |
| `a[2:-2]` | Select from the 3rd item to the second from last item | `[6, 8]` |
| `b[2:-2]` (with strings) | From 3rd character to the second from last | `['c', 'd']` |
| `a[-2:]` | Select the last two characters (for strings) or items | `[2, 3]` |
| `a[2:3]` | Slicing a list gives a list, even for a single item | `[6]` |
| `a[2]` | Indexing gives the element itself | `6` |
| `b[2:3]` (with strings) | Slicing a list of strings | `['c']` |
| `b[2]` (with strings) | Indexing a list of strings | `c` |
| `a[::-1]` | Reverse the list with step -1 | `[3, 2, 8, 6, 2, 4]` |
| `a[::-2]` | Reverse the list with step -2 | `[3, 8, 2]` |
| `a[1::-1]` | The first two items, reversed | `[2, 4]` |
| `a[3::-1]` | The first four items, reversed | `[8, 6, 2, 4]` |
| `a[3:1:-1]` | The first four items, starting at last two reversed | `[8, 6]` |
| `a[:-3:-1]` | The last two items, reversed | `[3, 2]` |
| `a[:-5:-1]` | The last four items, reversed | `[3, 2, 8, 6]` |
| `a[3:-5:-1]` | The last four items, starting at index 3 reversed | `[8, 6]` |
| `a[-3::-1]` | Everything except the last two items, reversed | `[8, 6, 2, 4]` |

&nbsp;
## Python Slicing Facts:
**Python's Forgiveness**:
- If a slice exceeds array bounds, it adjusts without errors.

**Slice Object**:
- `a[start:stop:step]` is shorthand for `a[slice(start, stop, step)]`.
- `slice()` is useful for dynamic slicing. For skipped parameters, use `None`.

**Examples**:
- `a[slice(start, None)]` equals `a[start:]`.
- `a[slice(None, None, -1)]` equals `a[::-1]`.

Using `slice()` allows for flexibility and programmability in slicing operations.


&nbsp;
#
# DATA STRUCTURES: Dictionary
&nbsp;

## Dictionary Methods (Most Commonly Used)

| Operation | | Description | | Returns |
|-----------|-|-------------|-|---------|
|`dict = {'a':1,'b':2,'c':3}`||Initialize dictionary named dict||`{'a':1,'b':2,'c':3}`|
|`dict.keys()`||Returns list of keys of dictionary||List of keys `['a', 'b', 'c']`|
|`dict.values()`||Returns list of values of dictionary||List of values `[1, 2, 3]`|
|`dict.get('a')`||Returns value for any corresponding key 'a'||`1`|
|`dict.items()`||Returns list of key-value pairs||List of tuples `[('a', 1), ('b', 2), ('c', 3)]`|
|`dict.pop('a')`||Pops key-value pair with key 'a'||Value of popped key `1`. `dict = {'b':2,'c':3}`|
|`dict.popitem()`||Removes the most recent pair added||Last key-value pair as tuple popped `('c', 3)`. `dict = {'a': 1, 'b': 2}`|
|`dict.update({'b': 5})`||Inserts {'e': 5} into dict; overrides if 'e' exists||Updated dict with `'b': 5`. `dict = {'a': 1, 'b': 5, 'c': 3}`|

&nbsp;
## Dictionary Methods (Least Commonly Used)
*You will need to import a module to use defaultdict. `
from collections import defaultdict`*

*Dictionary's methods `setdefault` and `defaultdict` can be manually coded. Up to you if you want to use the methods. Always a good idea to confirm with the interviewer if you can use certain methods.*

&nbsp;
| Operation | | Description | | Returns |
|-----------|-|-------------|-|---------|
|`dict.copy()`||Returns a copy of the dictionary||Copy of dict `{'a':1,'b':2,'c':3}`|
|`defaultdict(list)`||Ensures access to non-existent keys creates a new list entry||A default list for new keys|
|`dict.setdefault('d', 4)`||If 'd' exists, returns its value; otherwise, sets 'd' to 4 and returns 4||`{'a': 1, 'b': 2, 'c': 3, 'd': 4}`|

&nbsp;
## Time Complexities for Dictionary Methods
>NOTE: Amortized analysis ensures that over a series of operations, the average cost per operation remains low, even if a few operations are expensive.

![Untitled](https://user-images.githubusercontent.com/47276307/172330107-e68e3228-1c76-4bfb-bb38-04d18f94d5b9.jpg)

# --------------------------------------------------------------------
&nbsp;
#
# DATA STRUCTURES: Basic Data Types
&nbsp;




# --------------------------------------------------------------------
"""
DATA STRUCTURES: 
"""




# --------------------------------------------------------------------
# ---------------------------- ALGORITHMS ----------------------------
# --------------------------------------------------------------------