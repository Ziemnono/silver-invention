from subtract import subtract

import pytest

def test_subtracting():
	c = subtract(30,20)
	assert(c==10)

@pytest.mark.parametrize("a,b,result", [(3, 5, -2), (-3, 4, -7), (10, -3, 13)])
def test_subtract_param(a, b, result):
	c = subtract(a,b)
	assert(c==result)
