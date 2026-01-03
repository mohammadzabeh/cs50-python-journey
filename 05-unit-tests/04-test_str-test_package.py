from hello_exTest import hello


def test_default():
    """
    Test the default behavior of hello().

    When no argument is passed, the function should
    return the default greeting.
    """
    assert hello() == "Hello, World"


def test_argument():
    """
    Test hello() with a custom argument.

    When a name is provided, the function should
    include that name in the greeting.
    """
    assert hello("David") == "Hello, David"


"""
NOTES ABOUT PYTEST AND TEST FOLDERS:

1. Pytest automatically discovers test files if:
   - The file name starts with `test_` OR ends with `_test.py`
   - Test functions start with `test_`

2. If you place your tests inside a folder (e.g. `tests/`),
   you DO NOT need an __init__.py file for pytest to work.
   Pytest can discover tests without treating the folder
   as a Python package.

3. An __init__.py file is only required if:
   - You want to import modules using package-style imports
   - You want Python to treat the folder explicitly as a package

4. Running:
       pytest
   will automatically find and run ALL tests it can discover
   in the current directory and its subdirectories.
"""
