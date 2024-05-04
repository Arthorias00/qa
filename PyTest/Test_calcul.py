from PythonSintacsis.cool_cal import Calculator
cal = Calculator()
def test_addition():
    cal.push('C')
    cal.push('4')
    cal.push('+')
    cal.push('7')
    result = cal.push('=')
    assert result == "11"

def test_substruction():
    cal.push('C')
    cal.push('7')
    cal.push('-')
    cal.push('4')
    result = cal.push('=')
    assert result == "3"