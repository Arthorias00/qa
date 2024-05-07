import pytest
from PythonSintacsis.cool_cal import Calculator
@pytest.fixture(scope='function')
def calculator():
    calc = Calculator()
    return calc
