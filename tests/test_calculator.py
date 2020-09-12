from sunrise import do


def test_parser():
    assert '6' == do('2 + 4')
    assert '6' == do('Add 2 by 4')
    assert '2' == do('subtract 2 from 4')
    assert '2' == do('4 - 2')
    assert '2' == do('4 / 2')
    assert '2' == do('Div 4 by 2')
    assert '2' == do('Div 2 into 4')
