from watch import parse

def test_parse():
    assert parse('"http://youtube.com/embed/xvFZjo5PgG0"') == True
    assert parse('"https://youtube.com/embed/xvFZjo5PgG0"') == True
    assert parse('"https://www.youtube.com/embed/xvFZjo5PgG0"') == True
    assert parse('"www.youtube.com/embed/xvFZjo5PgG0"') == False
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == True
    assert parse('"https://www.youtube./embed/xvFZjo5PgG0"') == False
