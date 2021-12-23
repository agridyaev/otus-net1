# flake8: noqa
import os  # noqa
import sys

# Example of pyflakes error
print('Hello!');  # noqa: E703

# Cyclomatic complexity = 3 (--max-complexity 1)
a, b, c = 5, 6, 3
if a < b:
    pass
else:
    if a > c:
        pass
    else:
        pass
