from numb3rs import validate

def test_validate():
    assert validate('269.475.254.365') == False
    assert validate('cat.dog.bird.rat') == False
    assert validate('125.745.360.987') == False
    assert validate('0.0.0.0') == True
    assert validate('0.0.0.0.0') == False

