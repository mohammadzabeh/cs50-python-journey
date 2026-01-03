# pytest library
# python -m pip install pytest

from square_calculator import square

def test_square1():
        assert square(2) == 4
        assert square(3) == 9
        assert square(-2) == 4
        assert square(-3) == 9
        assert square(0) == 0
    
# using pytest fileName.py for testing this test file


def test_square2():
    # List of test inputs to the square function
    numbers = [1, 4, -4, 0, 5, -5]

    # Expected results: squares of the numbers above
    expected_results = [1, 16, 16, 0, 25, 25]

    # Iterate over pairs of (input, expected output)
    # zip makes a tuple out of iterables
    zipped = zip(numbers, expected_results)

    for n, expected in zipped:
        # Assert that the square function's output equals the expected result
        assert square(n) == expected


test_square2()

# pytest fileName.py for testing the test file


