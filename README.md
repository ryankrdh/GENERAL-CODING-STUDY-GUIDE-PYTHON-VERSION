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

## 4. Set
A collection of unique elements. Example: `{1, 2, 3}`.
- **Examples**:
  | Syntax | | | | Print |
  |-|-|-|-|-|
  |`empty_set = set()`| | | | `set()`|
  |`my_set = set([1, 2, 2])`| | | | `{1, 2}` |
  |`my_set = {1, 2, 2}`| | | | `{1, 2}` |


## 5. Sequence Type
- **Strings**: A sequence of characters. Example: "hello", 'world'.
- **Tuple**: An immutable sequence of elements. Example: (1, 2, 2).
- **Examples**:
  | Syntax | | | | Print |
  |-|-|-|-|-|
  |`empty_tuple = ()`| | | | `()`|
  |`my_tuple = tuple([1, 2, 2])`| | | | `(1, 2, 2)` |
  |`my_tuple = (1, 2, 2)`| | | | `(1, 2, 2)` |

- **Examples**:
  | Syntax | | | | Print |
  |-|-|-|-|-|
  |`empty_list = []`| | | | `[]`|
  |`my_list = list([1, 2, 2])`| | | | `[1, 2, 2]` |
  |`my_list = [1, 2, 2]`| | | | `[1, 2, 2]` |


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

```python
It's pretty simple really:

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
There is also the step value, which can be used with any of the above:

a[start:stop:step] # start through not past stop, by step
The key point to remember is that the :stop value represents the first value
that is not in the selected slice. So, the difference between stop and start is
the number of elements selected (if step is 1, the default).

The other feature is that start or stop may be a negative number, which means
it counts from the end of the array instead of the beginning. So:

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
Similarly, step may be a negative number:

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
Python is kind to the programmer if there are fewer items than you ask for. For
example, if you ask for a[:-2] and a only contains one element, you get an
empty list instead of an error. Sometimes you would prefer the error, so you
have to be aware that this may happen.

Relation to slice() object
The slicing operator [] is actually being used in the above code with a slice()
object using the : notation (which is only valid within []), i.e.:

a[start:stop:step]
is equivalent to:

a[slice(start, stop, step)]
Slice objects also behave slightly differently depending on the number of
arguments, similarly to range(), i.e. both slice(stop) and slice(start, stop[,
step]) are supported. To skip specifying a given argument, one might use None,
so that e.g. a[start:] is equivalent to a[slice(start, None)] or a[::-1] is
equivalent to a[slice(None, None, -1)].

While the :-based notation is very helpful for simple slicing, the explicit use
of slice() objects simplifies the programmatic generation of slicing.
```


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