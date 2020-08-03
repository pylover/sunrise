import re
from sunrise.actions import Calculator


patternslist = [
    ('[-+]?[0-9]+\.?[0-9]*\s*[-+*\/]\s*[-+]?[0-9]+\.?[0-9]*', Calculator()),
]

def parse(inputstring):
    for pattern, action in patternslist:
        if re.search(pattern, inputstring):
            return action
    raise Exception('Exception detail = The input string dose not match any pattern.')
