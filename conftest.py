import pytest
from application import Gurgen

@pytest.fixture(scope="function")
def glob_fixture(request):
    fixture = Gurgen()
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default='gurgen_0')
    parser.addoption("--iteration", action="store", default='10')
    parser.addoption("--min", action="store", default='1')
    parser.addoption("--max", action="store", default='5')
