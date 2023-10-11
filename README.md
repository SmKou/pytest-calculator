# Pytest Calculator

By: Stella Marie

Pytest sample on Calculator app

## Technologies Used

- Python
- Pytest

## Description

**Prompt:**
Develop unit tests for the given calculator application using the pytest framework. The application is a simple calculator and the class is defined below:

1. Cover the methods with test arguments for positive cases
2. Try with different negative cases

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b
```

**Requirements:** Implement tests to cover the methods

**Output:** Run the tests and see them pass, modify the code and see them detect failure.

## Complete Setup

Requires python installed (use 3.12)

To run: ```pytest```

## Known Bugs
* In development

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright © 2023 SmKou