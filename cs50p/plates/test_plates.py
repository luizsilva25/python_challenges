from plates import is_valid

def test_alphanumeric():
    assert is_valid('AAAA22') == True
    assert is_valid('AAA2.') == False

def test_starts_letters():
    assert is_valid('AA26') == True
    assert is_valid('A51') == False

def test_lenght():
    assert is_valid('hi') == True
    assert is_valid('hhhhhhh') == False

def test_number():
    assert is_valid('AA20AA') == False
    assert is_valid('AAAA20') == True

def test_zero():
    assert is_valid('AAAA02') == False
