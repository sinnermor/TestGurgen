from application import Gurgen
import pytest


# Tests
#
#
#
#
#
#
#
#
#

def test_params():
    Gurgen(10, 1, 5)


test_data_incorrect = [{10, 0, 10}, {10, 0, 0}, {0, 1, 5}, {0, 0, 0}]


@pytest.mark.parametrize('name, count, min_c, max_c', test_data_incorrect)
def test_incorrect_param(name, count, min_c, max_c):
    pass
