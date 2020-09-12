from sunrise import settings
from sunrise import configuration

def test_settings():
    configuration.builtins = '''
    foo:
      bar: baz
    '''

    configuration.initialise()
    assert settings.foo.bar == 'baz'

