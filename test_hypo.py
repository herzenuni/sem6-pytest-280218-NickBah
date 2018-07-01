from createDict import createDict
import hypothesis.strategies as st
from hypothesis import given
import unittest

class TestEncoding(unittest.TestCase):
    @given(st.lists(st.integers()),st.lists(st.integers()))
    def test_dict(self,first,second):
        result = createDict(first, second)
        expected = self.expectedResult(first,second)
        print(result)
        assert(result == expected)

    def expectedResult(self,keys,values):
        res = {}
        border = len(values)

        for i in range(len(keys)):
            if (i >= border):
                res.update({keys[i]: None})
            else:
                res.update({keys[i]: values[i]})

        return res

if __name__ == '__main__':
    unittest.main()