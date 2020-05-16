# tests.py -- for simple_request.py

from unittest import TestCase
from unittest.mock import patch

from simple_request import do_hello, URL
from cleaner_code import gen_ran_len_lst, _diff

class FakeResult:
    text = '<title>Google</title>'

class TestSimpleRequest(TestCase):
    @patch('requests.get')
    def test_simplerequest(self, mock_get):
        mock_get.return_value = FakeResult()
        
        do_hello()
        mock_get.assert_called_with(URL)

class TestCleanerCode(TestCase):

    def test_return_gen_ran_len_lst(self):
        lst = gen_ran_len_lst()
        assert type(lst) == type(list())

    def test_len_gen_ran_len_lst(self):
        lst = gen_ran_len_lst()
        assert 0 <= len(lst) <= 500

    def test_diff_returns_set_difference(self):
        lst1 = gen_ran_len_lst()
        lst2 = gen_ran_len_lst()
        diff_return = _diff(lst1, lst2)
        set_diff = set.difference(set(lst1), set(lst2))
        assert diff_return == set_diff


if __name__ == '__main__':
    from unittest import main
    main()