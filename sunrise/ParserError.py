class ParserError(Exception):
    def __init__(self, s):
        super().__init__(f'Cannot parse: {s}')
