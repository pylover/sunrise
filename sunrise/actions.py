import re
import abc


class Action(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass


class Calculator(Action):
    operators = ['+', '-', '*']

    def __init__(self, operator, a, b):
        self.operator = {
            'Add': '+',
            'Sub': '-',
            'subtract': '-',
            'Div': '//',
            '/': '//',
        }[operator] if operator not in self.operators else operator
        self.numbers = [a, b]

    def execute(self):
        return str(eval(self.operator.join(self.numbers)))


patterns = [
    (
        re.compile(r'(?P<a>\d+)\s*(?P<operator>[-+/*])\s*(?P<b>\d+)'),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Add)\s*(?P<a>\d+)\s*(with|by)\s*(?P<b>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Sub|subtract)\s*(?P<b>\d+)\s*(from)\s*(?P<a>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Div)\s*(?P<b>\d+)\s*(into)\s*(?P<a>\d+)'
        ),
        Calculator
    ),
    (
        re.compile(
            r'(?P<operator>Div)\s*(?P<a>\d+)\s*(by)\s*(?P<b>\d+)'
        ),
        Calculator
    ),
]


class ParseError(Exception):
    def __init__(self, command):
        super().__init__(f'Cannot parse: {command}')


def find(command):
    for pattern, action in patterns:
        match = pattern.match(command)
        if match:
            return action, match.groupdict()

    raise ParseError(command)

