import pytest
@pytest.mark.regress
@pytest.mark.skip(reason="Jira-123")
def test_addition(calculator):
    #calculator.push('C') - в фикстуре
    calculator.push('4')
    calculator.push('+')
    calculator.push('7')
    result = calculator.push('=')
    assert result == "11"

@pytest.mark.regres
def test_substruction(calculator):
    #calculator.push('C') - в фикстуре
    calculator.push('7')
    calculator.push('-')
    calculator.push('4')
    result = calculator.push('=')
    assert result == "3"

#тест проходит если упал, если он пройдет то будет ошибка
@pytest.mark.xfail(strict=True)
def test_first_error(calculator):
    #calculator.push('C') - в фикстуре
    calculator.push('4')
    calculator.push('+')
    calculator.push('7')
    result = calculator.push('=')
    assert result == "15"