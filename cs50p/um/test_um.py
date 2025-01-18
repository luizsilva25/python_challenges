from um import count

def test_for_ums_alone():
    assert count('um') == 1

def test_for_ums_ponctuation():
    assert count('um?') == 1

def test_for_ums_in_words():
    assert count('Um, thanks for the album') == 1

def test_for_multiple_ums():
    assert count('Um, thanks, um...') == 2
