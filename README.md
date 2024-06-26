# CODING INTERVIEW STUDY GUIDE - Hyunmin Kim 


## Key Points for Every Technical Interview

### 1. **Ask Questions and Don't Assume Anything**
Always clarify the problem statement even if it seems familiar. Don't make assumptions; explicitly confirm details to ensure understanding.

#### Example Questions You Might Need To Ask:
- Are there any constraints to the parameter or solution? (How big is the input size?)
- Will you be dealing with negative numbers? Floating points?
- Will the numbers be in string or integer form?
- Should I consider edge cases such as an empty or invalid inputs?
- Are there any time and space complexities constraints?
- What input will you give and what output is expected?
- Will there be duplicates in the input? If so, how do you want me to handle it?
- Is it okay to use built-in functions?
- What to output if no solution is found?

### 2. **If Stuck On Logic**

- Reduce the problem to a simpler version.
- Don't think about code, think what a human would do. 

Example: Imagine how you as a human will find two consecutive numbers that add to a target in an array of numbers. You would likely start at the beginning of the array and add each pair of consecutive numbers to see if they match the garget sum. If they don't you would simply move to the next pair and repeat the process until you find a match or reach the end of the array. 

After you finish your brute force completely then you can think of optimization like binary search.

### 3. **If Stuck, Return to Pseudocode**
If you find yourself struggling during the coding stage, stop everything and go back to your pseudocode, most likely your logic is not complete and you need to go back and re-think.

### 4. **Organise your thoughts, and ALWAYS coomunicate your thought process**
- Start by confirming your understanding to the interviewer.
- Explain your approach BEFORE coding/pseudo coding.
- Think ALOUD during coding.


---------------------------------------------------------------------------------

## PREP Methodology

### **Parameters**
- **Validate Input First:** Always check the inputs first to handle any edge cases.

### **Return Values**
- **Define What to Return:** Ensure you know what the function needs to return to pass the test cases.

### **Examples**
- **Work Through Examples:** Use examples to clarify edge cases and validate that your approach covers all possible scenarios.

### **Pseudocode**
- **Simplify the Coding Process:** Describe your solution in a structured way that mimics coding logic but in simplified terms.

#### Pseudocode Example
- **Prompt:** You are given a list. Order the numbers inside from least to greatest.
  ```plaintext
  1. For each index i in the list:
     a. Find the smallest number in the list from index i to the end.
     b. Swap the smallest number found with the number at index i.
  2. Return the sorted list.




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
- **Keys**: Typically, dictionary keys are strings, numbers, or tuples because these are immutable. However, you can use any object as a key if you implement an "equals" method for that object. 
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

&nbsp;
# To be added in the future:

## HEAPS (MIN HEAP, MAX HEAP): 
If you're manually adding each value to the heap, you will be doing it in O(n log n) time. However, if you're building a heap and if you have all the inputs available, you can build it in O(n) time.
top() -> O(1)
insert() -> O(log n)
remove() -> O(log n)
heapify() -> O(n)
## Linked List
## Trees
## Graphs
&nbsp;
#
#
# ALGORITHMS

#
&nbsp;
&nbsp;
# To be added in the future:




## TWO POINTERS
## SLIDING WINDOW
## BINARY SEARCH (log n)
## RECURSION:
Recursion of trees, graphs, backtracking, Dynamic programming, and more. You need to know this really well in order to not struggle with DFS & BFS
## DFS & BFS (Most of the time it is O(V + E)):
This algorithm is the building blocks for complex algorithms like Djikstra, kruskal, prims, bellman-ford, and etc.
## DIVIDE AND CONQUER
## Dijkstra
##

&nbsp;
# Not so common but we will still review:
## Bit Manipulation
## Topological Sort


&nbsp;
# Recognizing patterns in leetcode questions:

## Common Algorithms and Data Structures Guide

### 1. **Binary Search**
- **Use Case:** Effective on sorted arrays for quick element lookup.
- **Efficiency:** O(log n) time complexity by halving the search space each iteration.

### 2. **Two Pointers**
- **Use Case:** Ideal for comparing elements in arrays or linked lists without extra space.
- **Efficiency:** Achieves linear time complexity without extra space.

### 3. **Sliding Window**
- **Use Case:** Suitable for finding subarrays or substrings of a specific size with a linear scan.
- **Efficiency:** Maintains a subset of data, achieving linear time complexity.

### 4. **Breadth-First Search (BFS)**
- **Use Case:** Excellent for shortest path problems in unweighted graphs or level-order tree traversal.
- **Efficiency:** Explores all neighbors at current depth before moving to the next level.

### 5. **Depth-First Search (DFS)**
- **Use Case:** Great for exploring all paths or confirming path existence in graphs or trees.
- **Efficiency:** Goes deep down one path before backtracking.

### 6. **Recursion**
- **Use Case:** Applicable to problems where the solution involves solving smaller instances of the same problem.
- **Efficiency:** Can be less efficient and more memory intensive but simplifies complex problems.

### 7. **Backtracking**
- **Use Case:** Effective for decision space exploration, such as in puzzles or combinatorial problems.
- **Efficiency:** Allows incremental building and abandoning of solution candidates.

### 8. **Divide and Conquer**
- **Use Case:** Useful when problems can be divided into smaller, similar problems solved recursively.
- **Efficiency:** Often optimizes over simple iterative solutions, helpful in parallel processing.

### 9. **Dynamic Programming**
- **Use Case:** Best for problems with overlapping subproblems like shortest paths or optimization issues.
- **Efficiency:** Reduces time complexity at the expense of space complexity through memoization or tabulation.

### 10. **Greedy Algorithms**
- **Use Case:** Optimal for problems where local optimum choices lead to a global optimum.
- **Efficiency:** Simpler and faster than more complex algorithms like dynamic programming for certain optimization problems.

### 11. **Graph Algorithms**
- **Use Case:** Includes algorithms for shortest paths, minimum spanning trees, and cycle detection.
- **Efficiency:** Each algorithm optimizes a specific aspect of graph traversal.

### 12. **Sorting Algorithms**
- **Use Case:** Various algorithms like quicksort, mergesort, and heapsort are chosen based on data characteristics.
- **Efficiency:** The choice of algorithm affects performance, especially important in large datasets.

### 13. **Hashing**
- **Use Case:** Used for quick data retrieval, duplicate detection, and indexing.
- **Efficiency:** Provides O(1) average-case time complexity for key-based data operations.


### General Problem-Solving Tips
- **Max-Min/Min-Max Problems:** Consider using binary search if the array is sorted.
- **K-th Element Problems:** Look into using a heap for efficient retrieval of k-th smallest/largest elements.
- **Subarray Problems:** Avoid sorting as it changes the original order of elements, which is crucial for subarray integrity.
- **Small Data Sets (< 1000 elements):** Brute force approaches might be viable and simple to implement.
- **Tree or Graph Problems:** Typically start by considering Depth-First Search (DFS) or Breadth-First Search (BFS).
- **Shortest Path Problems:** Breadth-First Search (BFS) is ideal for unweighted graphs to find the shortest path.
