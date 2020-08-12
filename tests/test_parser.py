from sunrise import parser
from sunrise.actions import Action, Calculator


def test_parser():
    action = parser.parse('2 + 4')
    assert issubclass(action, Action)
    assert issubclass(action, Calculator)

