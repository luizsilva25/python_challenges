from bank import value

def test_value():
    assert value('hi') == 20
    assert value('hello') == 0
    assert value('sei la') == 100
    assert value('sei la hello') == 100
    assert value('Hello') == 0


