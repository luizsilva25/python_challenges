from seasons import get_date

def test_get_date():
    assert get_date('1998-07-24') == ('1998', '07', '24')


