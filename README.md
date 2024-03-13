# PYTHON-STUDY-GUIDE- Hyunmin Kim 

&nbsp;
#
#

# DATA STRUCTURES

#
&nbsp;
#
# DATA STRUCTURES: Basic Data Types
&nbsp;

>There are 5 main basic data types.

## 1. Numeric
- **Integer**: A whole number without a decimal point. Example: 5, -12, 0.
- **Float**: A number with a decimal point. Example: 3.14, -0.5, 2.0.
- **Complex Number**: A number that has both a real part (like regular numbers) and an imaginary part (like numbers with 'i' in math). For example, 2+3i or -1-2i.

## 2. Dictionary
A collection of key-value pairs. Example: `{'apple': 2, 'banana': 3}`.
- **Keys**: Strings, numbers, and tuples. Immutable data types.
- **Values**: Any types can be a value.
- **Examples**:
    | Syntax | | | | Print |
    |-|-|-|-|-|
    |`empty_dict = {}`| | | | `{}`|
    |`my_dict = dict([('a', 1), ('b', 2)])`| | | | `{'a': 1, 'b': 2}` |
    |`my_dict = {'a': 1, 'b': 2}`| | | | `{'a': 1, 'b': 2}` |

## 3. Boolean
A data type that can only have two values: True or False.
- **Examples**:
  | Syntax | | Description | | Print |
  |-|-|-|-|-|
  |`bool('Hello')`| |Evaluate a string| | `True`|
- **Examples**:
  | Syntax | | Description | | Print |
  |---|---|---|---|---|
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


## 4. Set
- **Sets**: Unordered, immutable, and do NOT allow duplicate values.
- **Examples**:
  | Syntax | | Description | | Print |
  |-|-|-|-|-|
  |`empty_set = set()`| |Initialize an empty set| | `set()`|
  |`my_set = {1, 2}`| |Initialize a set with elements| | `{1, 2}` |
  |`my_set = set([1, 2, 2])`| |Change list into set| | `{1, 2}` |


## 5. Sequence Type
- **Strings**: Ordered, immutable, and allow duplicate values.
  | Syntax | |Description| | Print |
  |-|-|-|-|-|
  |`string = 'Hello`| |Initilize a variable with a string| | `Hello`|
  |`string[1]`| |Locate and return a string by INDEX| | `e`|
- **Tuple**: Ordered, immutable, and allow duplicate values.
- **Examples**:
  | Syntax | | | | Print |
  |-|-|-|-|-|
  |`empty_tuple = ()`| |Initialize an empty tuple| | `()`|
  |`my_tuple = (1, 2, 2)`| |Initialize a tuple with elements| | `(1, 2, 2)` |
  |`my_tuple = tuple([1, 2, 2])`| |Change list into tuple| | `(1, 2, 2)` |
- **List**: Ordered, mutable, and allow duplicate values.
- **Examples**:
  | Syntax | |Description| | Print |
  |-|-|-|-|-|
  |`empty_list = []`| |Initilize an empty list| | `[]`|
  |`my_list = [1, 2, 2]`| |Initialize a list with elements| | `[1, 2, 2]` |
  |`my_list = list([1, 2, 2])`| |Change tuple into list| | `[1, 2, 2]` |



### Python Facts: 
# --------------------------------------------------------------------
&nbsp;
#
# DATA STRUCTURES: Lists
&nbsp;
## List Methods (Most Commonly Used)
*Notice how some methods need to be saved to a variable because they return a result instead of directly changing the list.*

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


# --------------------------------------------------------------------
&nbsp;
#
# DATA STRUCTURES: List or String Slicing in Python
&nbsp;


Python slicing allows you to select parts of an array (or list) with ease. Here's a breakdown:

- **Basic Slicing**:
  - `a[start:stop]`: Gets items from index `start` to `stop-1`.
  - `a[start:]`: Gets items from `start` to the end.
  - `a[:stop]`: Gets items from the beginning to `stop-1`.
  - `a[:]`: Copies the whole array.

- **Advanced Slicing with Step**:
  - `a[start:stop:step]`: Gets items from `start` to `stop-1`, skipping items by `step`.

**Key Points**:
- The `stop` index isn't included in the selection.
- Default `step` is 1, selecting consecutive items.
- Negative `start` or `stop` counts from the end.
- Negative `step` reverses the direction.

**Negative Indices Examples**:
- `a[-1]`: Last item.
- `a[-2:]`: Last two items.
- `a[:-2]`: Everything except the last two items.
- `a[::-1]`: All items, reversed.

**Python's Forgiveness**:
- If a slice exceeds array bounds, it adjusts without errors.

**Slice Object**:
- `a[start:stop:step]` is shorthand for `a[slice(start, stop, step)]`.
- `slice()` is useful for dynamic slicing. For skipped parameters, use `None`.

**Examples**:
- `a[slice(start, None)]` equals `a[start:]`.
- `a[slice(None, None, -1)]` equals `a[::-1]`.

Using `slice()` allows for flexibility and programmability in slicing operations.




# --------------------------------------------------------------------
&nbsp;
#
# DATA STRUCTURES: Basic Data Types
&nbsp;




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