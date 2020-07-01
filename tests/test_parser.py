from sunrise import parser
from sunrise.actions import Action, Calculator


def test_parser():
    action = parser.parse('2 + 4')
    assert isinstance(action, Action)
    assert isinstance(action, Calculator)

