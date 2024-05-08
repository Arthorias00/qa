import pytest
from PythonSintacsis.cool_cal import Calculator
#применяется к каждой функции
@pytest.fixture(scope='function')
def calculator():
    calc = Calculator()
    #Как return но мы можем дальше действия выполнять
    yield calc
    calc.push('C')
