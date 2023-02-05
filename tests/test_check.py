import pytest


def test_check():
    c = 5
    print('Hello world' * c)
    assert c == 5


@pytest.mark.xfail
def test_check_wrong():
    c = 5
    print('Hello world' * c)
    assert c == 6
