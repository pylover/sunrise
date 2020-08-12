import re

from sunrise import actions


patterns = [
    (
        re.compile(r'[-+]?[0-9]+\.?[0-9]*\s*[-+*\/]\s*[-+]?[0-9]+\.?[0-9]*'), 
        actions.Calculator
    ),
]


def parse(command):
    for pattern, action in patterns:
        if pattern.match(command):
            return action

    raise ParseError(command)
