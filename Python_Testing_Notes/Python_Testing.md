## PYTHON-TESTING-Hyunmin Kim


> NOTE: Pytest and Unittest are two different testing frameworks.

### **Pytest** (import python)
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

> To run pytest on all test in the directory. 
> In command line: python3 -m pytest

Example:

```python
import pytest

def test_assert_equal():
    a = "hello"
    b = "hello"
    assert a == b, "Error message"

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


## Pytest Sample Codes
```python
# Using Pytest Assert WITH For Loop
def test_process_string():
    """Test for process_string function"""

    test_cases = [
        ("bes^mc*uer^xlt*a", "secret"),
        ("nas*o*veul^zit^no^pr", "solution"),
        ("zeM^un-e*0 t^a*l t^75*4a1:^s35*A,P ^2NM* ,^Mc.+GcO^ t^3*,0^2 ^5m0*x81^bes^mc*uer^xlt*a", "Meet at 5:15 PM, Oct 30, 2018secret")
    ]

    for input_string, expected_output in test_cases:
        string_processor = StringProcessor()
        string_processor.process_string(input_string)
        test_case_result = ''.join(string_processor.solution)

        assert test_case_result == expected_output, f"Expected {expected_output}, got {test_case_result}."
```
```python
# Using Pytest Assert WITHOUT For Loop
def test_process_string_combined():
    """Test for process_string function with multiple inputs."""
    string_processor = StringProcessor()
    
    # Process the first string
    string_processor.process_string("bes^mc*uer^xlt*a")
    # Assuming process_string modifies `self.solution` which needs to be joined to form a string
    test_case1_result = ''.join(string_processor.solution)
    assert test_case1_result == "secret", f"It should return the string, 'secret', but got {test_case1_result}"

    # Reset the processor or its solution attribute for a fresh start
    string_processor.solution = []

    # Process the second string
    string_processor.process_string("nas*o*veul^zit^no^pr")
    test_case2_result = ''.join(string_processor.solution)
    assert test_case2_result == "solution", f"It should return the string, 'solution', but got {test_case2_result}"

    # Reset the processor or its solution attribute for a fresh start
    string_processor.solution = []
    
    # Process the third string
    string_processor.process_string("zeM^un-e*0 t^a*l t^75*4a1:^s35*A,P ^2NM* ,^Mc.+GcO^ t^3*,0^2 ^5m0*x81^bes^mc*uer^xlt*a")
    test_case3_result = ''.join(string_processor.solution)
    assert test_case3_result == "Meet at 5:15 PM, Oct 30, 2018secret", f"It should return the string, 'solution', but got {test_case3_result}"
```


&nbsp;
#
#
# UNITTEST
#

&nbsp;

Note: import unittest required at the top of the page. <br>
Unittest also requires that you create a class. <br>
If you want to use unittest assertions OUTSIDE of a class, you have to create a instance of unittest.TestCase() and call the methods on that. 

> To run unittest on all test in the directory. 
> In command line: python3 -m unittest

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
