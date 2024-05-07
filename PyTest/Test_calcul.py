

def test_addition(calculator):
    calculator.push('C')
    calculator.push('4')
    calculator.push('+')
    calculator.push('7')
    result = calculator.push('=')
    assert result == "11"

def test_substruction(calculator):
    calculator.push('C')
    calculator.push('7')
    calculator.push('-')
    calculator.push('4')
    result = calculator.push('=')
    assert result == "3"