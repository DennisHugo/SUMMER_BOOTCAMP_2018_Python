"""
This module contains Calculator class
"""


class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current


cal = Calculator()
cal.add(100)
print(cal.get_current())