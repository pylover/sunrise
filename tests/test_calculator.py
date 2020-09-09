from sunrise import do


def test_parser():
    assert '6' == do('2 + 4')
    assert '6' == do('Add 2 by 4')


