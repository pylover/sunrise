import re

from sunrise.actions import Calculator


patternslist = [
    (re.compile(r'[-+]?[0-9]+\.?[0-9]*\s*[-+*\/]\s*[-+]?[0-9]+\.?[0-9]*')
    , Calculator)
]


def parse(inputstring):
    for pattern, action in patternslist:
        if pattern.match(inputstring):
            return action

    raise ParseError(inputstring)
