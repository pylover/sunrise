class ParseError(Exception):
    def __init__(self, command):
        super().__init__(f'Cannot parse: {command}')
