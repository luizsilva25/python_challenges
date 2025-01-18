from twttr import shorten
import pytest

def test_shorten():
    assert shorten('TWITTERtwitter123.') == 'TWTTRtwttr123.'

def test_shorten_str():
    with pytest.raises(TypeError):
        shorten(1)


