import sys
from io import StringIO

import calculator


class CaptureOutput:
    def __init__(self):
        self.new_out = StringIO()
        self.new_err = StringIO()
        self.old_out = sys.stdout
        self.old_err = sys.stderr

    def __enter__(self):
        sys.stdout = self.new_out
        sys.stderr = self.new_err
        return sys.stdout, sys.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_out
        sys.stderr = self.old_err
        return True


class TestCalculator:
    def test_addition(self):
        assert 7 == calculator.add(3, 4)

    def test_subtraction(self):
        assert -4 == calculator.subtract(3, 7)

    def test_subtraction(self):
        assert 21 == calculator.multiply(3, 7)

    def test_input_addition(self):
        calculator.input = lambda _: '1 + 4'
        with CaptureOutput() as (out, err):
            calculator.runner()
        assert '5' == out.getvalue().strip()

    def test_invalid_addition(self):
        calculator.input = lambda _: 'a + 4'
        with CaptureOutput() as (out, err):
            calculator.runner()
        assert 'Invalid operation' == out.getvalue().strip()

    def test_invalid_single_addition(self):
        calculator.input = lambda _: 'a'
        with CaptureOutput() as (out, err):
            calculator.runner()
        assert 'Invalid operation' == out.getvalue().strip()