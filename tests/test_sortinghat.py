import pytest
from sortinghat.sorting_hat import SortingHat

class TestSortingHat(object):
    def test_when_no_overflow(self):
        x ="""init12
        reg 1 B V
        reg 2 A V
        reg 3 A V
        reg 4 B NV
        reg 5 B V
        reg 6 A NV
        reg 7 A V
        reg 8 A NV
        reg 9 B NV
        reg 10 B V
        reg 11 A NV
        reg 12 B NV 
        fin
        """
        obj = SortingHat()
        assert obj.boarding_house_allocation(x) == {'AV': [2, 3, 7], 'BV': [1, 5, 10], 'ANV': [6, 8, 11],
                                                   'BNV': [4, 9, 12], 'NA': []}, "testfail"

    def test_with_overflow(self):
        x ="""init12
        reg 1 B V
        reg 2 A V
        reg 3 A V
        reg 4 B NV
        reg 5 B V
        reg 6 A NV
        reg 7 A V
        reg 8 A NV
        reg 9 B NV
        reg 10 B V
        reg 11 A NV
        reg 12 B NV
        reg 14 B NV
        fin
        """
        obj = SortingHat()
        assert obj.boarding_house_allocation(x) == {'AV': [2, 3, 7], 'BV': [1, 5, 10], 'ANV': [6, 8, 11],
                                                    'BNV': [4, 9, 12], 'NA': [14]}, "testfail"

    def test_when_roll_number_valueerror(self):
        x ="""init12
        reg 1 B V
        reg 2 A V
        reg 3 A V
        reg 4 B NV
        reg 5 B V
        reg  A NV
        reg 7 A V
        reg 8 A NV
        reg 9 B NV
        reg 10 B V
        reg 11 A NV
        reg 12 B NV
        reg 13 A NV
        reg 123 A NV
        reg 34 A NV
        fin
        """
        obj = SortingHat()
        with pytest.raises(ValueError) as excinfo:
            obj.boarding_house_allocation(x)
        assert "('Data format is not correct for roll number or is missing value:', 'reg  A NV')" in str(excinfo.value)

    def test_when_class_option_wrong(self):
        x = """init12
        reg 1 B V
        reg 2 A V
        reg 3 A V
        reg 4 B NV
        reg 5 B V
        reg 6 A NV
        reg 7 A V
        reg 8 A NV
        reg 9 B NV
        reg 10 C V
        reg 11 A NV
        reg 12 B NV
        reg 13 A NV
        reg 123 A NV
        reg 34 A NV
        fin
        """
        obj = SortingHat()
        with pytest.raises(ValueError) as excinfo:
            obj.boarding_house_allocation(x)
        assert "('Data format is not correct for class A|B or is missing value:', 'reg 10 C V')" in str(excinfo.value)

    def test_when_food_option_wrong(self):
        x = """init12
        reg 1 B V
        reg 2 A V
        reg 3 A V
        reg 4 B NV
        reg 5 B V
        reg 6 A NV
        reg 7 A V
        reg 8 A NV
        reg 9 B NV
        reg 10 B NNV
        reg 11 A NV
        reg 12 B NV
        reg 13 A NV
        reg 123 A NV
        reg 34 A NV
        fin
        """
        obj = SortingHat()
        with pytest.raises(ValueError) as excinfo:
            obj.boarding_house_allocation(x)
        assert "('Data format is not correct for food V|NV or is missing value:', 'reg 10 B NNV')" in str(excinfo.value)
