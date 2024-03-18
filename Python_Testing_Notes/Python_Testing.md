## PYTHON-TESTING-Hyunmin Kim


> NOTE: Pytest and Unittest are two different testing frameworks.

### **Pytest** 
    A testing framework that requires installation. It emphasizes simplicity, scalability and ease of use, making it a favored choice among developers.

### **Unittest** (import unittest)
    A built-in Python testing framework that does NOT require installation (part of Python's statndard library). It emphasizes simplicity and compatibility with older versions of Python.

&nbsp;
#
#
# PYTEST
#

&nbsp;

Note: import pytest may be required at the top of the page. <br>
Unlike Unittest, Pytest does not require a class-based structure.

Example:

```python
import pytest

def test_assert_equal():
    a = "hello"
    b = "hello"
    assert a == b

# Type this in command line to test:
python -m pytest
```

> You may put in AssertionError message for all the Pytest assert methods. <br>

> EX: <br>
> assert a == b, "The value of a should be equal to b" <br>
> assert a % 2 == 0, "value was odd, should be even"
## Most Commonly Used Pytest Methods
| Method                | Checks that         | Code Example                                       |
|-----------------------|---------------------|----------------------------------------------------|
| `assert a == b`       | `a == b`            | `assert 1 + 1 == 2`                                |
| `assert a != b`       | `a != b`            | `assert 2 * 2 != 5`                                |
| `assert x`            | `bool(x) is True`   | `assert 'FOO'.isupper()`                           |
| `assert not x`        | `bool(x) is False`  | `assert not 'Foo'.isupper()`                       |
| `assert a in b`       | `a in b`            | `assert 3 in [1, 2, 3]`                            |
| `assert a not in b`   | `a not in b`        | `assert 4 not in [1, 2, 3]`                        |
| `assert x is None`    | `x is None`         | `assert None is None`                              |
| `assert x is not None`| `x is not None`     | `assert 42 is not None`                            |

## Least Commonly Used Pytest Methods
| Method                    | Checks that            | Code Example                                   |
|---------------------------|------------------------|------------------------------------------------|
| `assert a is b`           | `a is b`               | `assert None is None`                         |
| `assert a is not b`       | `a is not b`           | `assert None is not 42`                       |
| `assert isinstance(a, b)` | `isinstance(a, b)`     | `assert isinstance('hello', str)`             |
| `assert not isinstance(a, b)` | `not isinstance(a, b)` | `assert not isinstance(42, str)`             |

&nbsp;
### Pytest Parametrize
@pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class. 

Note: Import pytest IS required at the top of the page. <br>

Example:

```python
import pytest
from your_module import Multiplier

# Define test cases as tuples: (number, factor, expected_product)
test_cases_multiply = [
    (2, 3, 6),
    (5, 0, 0),
    (-1, 10, -10),
    (3, -3, -9),
    (0, 0, 0),
]

@pytest.mark.parametrize("number, factor, expected_product", test_cases_multiply)
def test_multiply(number, factor, expected_product):
    """Test Multiplier.multiply method with various inputs."""
    multiplier = Multiplier()
    assert multiplier.multiply(number, factor) == expected_product

```

&nbsp;
## Pytest Parametrize Test Samples

| Number | Factor | Expected Product | Description                     |
|--------|--------|------------------|---------------------------------|
| 2      | 3      | 6                | Simple multiplication           |
| 5      | 0      | 0                | Multiplying by zero             |
| -1     | 10     | -10              | Negative number                 |
| 3      | -3     | -9               | Negative factor                 |
| 0      | 0      | 0                | Zero times zero                 |




&nbsp;
#
#
# UNITTEST
#

&nbsp;

Note: import unittest required at the top of the page. <br>
Unittest also requires that you create a class. <br>
If you want to use unittest assertions OUTSIDE of a class, you have to create a instance of unittest.TestCase() and call the methods on that. 

Example:

```python
import unittest

tc = unittest.TestCase()
tc.assertEqual(a, b)

# Type this in command line to test:
python -m unittest
```

## Most Commonly Used Unittest Methods
| Method                | Checks that         | Code Example                                               |
|-----------------------|---------------------|------------------------------------------------------------|
| `assertEqual(a, b)`   | `a == b`            | `self.assertEqual(1 + 1, 2)`                              |
| `assertNotEqual(a, b)`| `a != b`            | `self.assertNotEqual(2 * 2, 5)`                           |
| `assertTrue(x)`       | `bool(x) is True`   | `self.assertTrue('FOO'.isupper())`                        |
| `assertFalse(x)`      | `bool(x) is False`  | `self.assertFalse('Foo'.isupper())`                       |
| `assertIn(a, b)`      | `a in b`            | `self.assertIn(3, [1, 2, 3])`                             |
| `assertNotIn(a, b)`   | `a not in b`        | `self.assertNotIn(4, [1, 2, 3])`                          |
| `assertIsNone(x)`     | `x is None`         | `self.assertIsNone(None)`                                 |
| `assertIsNotNone(x)`  | `x is not None`     | `self.assertIsNotNone(42)`                                |

&nbsp;
## Least Commonly Used Unittest Methods
| Method                      | Checks that            | Code Example                                               |
|-----------------------------|------------------------|------------------------------------------------------------|
| `assertIs(a, b)`            | `a is b`               | `self.assertIs(None, None)`                               |
| `assertIsNot(a, b)`         | `a is not b`           | `self.assertIsNot(None, 42)`                              |
| `assertIsInstance(a, b)`    | `isinstance(a, b)`     | `self.assertIsInstance('hello', str)`                     |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | `self.assertNotIsInstance(42, str)`                       |
