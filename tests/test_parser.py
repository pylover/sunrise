from sunrise.actions import find, Action, Calculator


def test_parser():
    action, params = find('2 + 4')
    assert issubclass(action, Action)
    assert issubclass(action, Calculator)
    assert params == {
        'a': '2',
        'operator': '+',
        'b': '4'
    }

