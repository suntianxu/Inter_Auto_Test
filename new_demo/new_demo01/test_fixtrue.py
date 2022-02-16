import pytest


@pytest.fixture()
def username():
    print('打印usname')
    username = '123'
    assert username=='123'
    return username

@pytest.fixture()
def psw():
    print('打印pwd')
    psw = 123
    assert psw == 123
    return psw

def test_loing(username,psw):
    print(username,psw)
    assert username=='123'
    assert psw == 123


if __name__ == '__main__':
    pytest.main(['-s','test_fixtrue.py'])

