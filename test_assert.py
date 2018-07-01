from createDict import createDict

test_a = ['a','b','c','d']
test_b = [1,2,3,4,5]
test_result = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

assert createDict(test_a,test_b) == test_result, 'Wrong!'

test_a = []
test_b = []
test_result = {}

assert createDict(test_a,test_b) == test_result, 'Wrong!'

test_a = ['a','b','c']
test_b = [1,2,3,4,5]
test_result = {'a': 1, 'b': 2, 'c': 3}

assert createDict(test_a,test_b) == test_result, 'Wrong!'

test_a = ['a','b','c']
test_b = [1,2]
test_result = {'a': 1, 'b': 2, 'c': None}

assert createDict(test_a,test_b) == test_result, 'Wrong!'