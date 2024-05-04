# это крутой калькулятор
class Calculator:
    BUTTONS = '1234567890+-*/C='
    def __init__(self):
        self._expression = ''
    def push(self, button):
        if button not in self.BUTTONS:
            raise CalculationError("invalid button '%s' . " % button)
        if button == "=":
            self._expression = self._calculate(self._expression)
        elif button == "C":
            self._expression = ""
        elif button == "/":
            self._expression += "//"  #integer division also in Python 3
        else:
            self._expression += button
        return self._expression

    def _calculate(self, expression):
        try:
            return str(eval(expression))
        except SyntaxError:
            raise CalculationError("Invalid exprassion . ")
        except ZeroDivisionError:
            raise CalculationError("Division by zero . ")

class CalculationError(Exception):
        pass



