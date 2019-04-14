"""Module with testsuite of tests for base types"""


class TestSuite:
    """Testsuite of tests for base types"""

    def test_multiply_numbers(self, case_data):
        """Number multipluing test"""
        assert 3*4 == 12

    def test_sum_numbers(self, case_data):
        """Number sum test"""
        assert (3 + 4) == 7

    def test_subtr_numbers(self, case_data):
        """Number subtraction test"""
        assert (4 - 3) == 1

    def test_strings_a_3(self, case_data):
        """String multipluing test"""
        assert "a"*3 == 'aaa'

    def test_string_concatenation(self, case_data):
        """String concatenation test"""
        assert ("aa" + "bb") == "aabb"

    def test_list_len(self, case_data):
        """List length test"""
        rang_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert len(rang_list) == 10

    def test_list_min(self, case_data):
        """Min element test"""
        numbers = [10, 20, 30, 40]
        assert min(numbers) == 10

    def test_list_max(self, case_data):
        """Max element test"""
        numbers_2 = [10, 20, 30, 40]
        assert max(numbers_2) == 40

    def test_list_sum(self, case_data):
        """List elements test"""
        numbers_3 = [10, 20, 30, 40]
        assert sum(numbers_3) == 100

    def test_dict_key(self, case_data):
        """Dict element access test"""
        beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
        assert beatles_map['Paul'] == 'Bass'

    def test_dict_pop(self, case_data):
        """Dict element pop test"""
        beatles_map_2 = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
        assert beatles_map_2.pop('Paul') == 'Bass'

    def test_set_inter(self, case_data):
        """Intersection sets test"""
        odd_set = {1, 3, 5, 7, 9}
        even_set = {0, 2, 4, 6, 8}
        intersection_set = odd_set & even_set
        assert (not intersection_set)
