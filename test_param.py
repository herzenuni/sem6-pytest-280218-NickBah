import pytest
from createDict import createDict

@pytest.fixture(scope="function", params=[
        (['a','b','c','d'], [1,2,3,4,5], {'a': 1, 'b': 2, 'c': 3, 'd': 4}),
        ([], [], {}),
        (['a','b','c'], [1,2,3,4,5], {'a': 1, 'b': 2, 'c': 3}),
        (['a','b','c'], [1,2], {'a': 1, 'f': 2, 'c': None})],
        ids = ['First test','Second test','Third test','Fourth test'])

def param_test(request):
    return request.param

def test_our_func(param_test):
    (key,value,expected_result) = param_test
    calculated_result = createDict(key,value)
    print("input: {0}, output: {1}, expected: {2}".format([key,value], calculated_result, expected_result))
    assert createDict(key,value) == expected_result

if __name__ == '__main__':
    param_test()