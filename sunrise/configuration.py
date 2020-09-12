import pymlconf


builtins = '''
'''


settings = pymlconf.DeferredRoot()


def initialise():
    settings.initialize(builtins)

