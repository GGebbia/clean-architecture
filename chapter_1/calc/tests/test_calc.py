from calc.calc import Calc
import pytest

def test_add_two_numbers():
    
    c = Calc()
    res = c.add(4, 5)
    
    assert res == 9

def test_add_three_numbers():
    
    c = Calc()
    res = c.add(4, 5, 6)

    assert res == 15

def test_add_many_numbers():
    s = range(100)
    c = Calc()

    res = c.add(*s)

    assert res == 4950

def test_sub_two_numbers():

    c = Calc()
    res = c.sub(9,5)

    assert res == 4

def test_mult_many_numbers():

    c = Calc()
    res = c.mul(*[2,3,4])
    
    assert res == 24

def test_div_two_numbers():

    c = Calc()
    res = c.div(13, 2)
    
    assert res == 6.5

def test_div_by_zero_returns_inf():

    c = Calc()
    res = c.div(5, 0)

    assert res == 'inf'

def test_mult_by_zero_raises_exception():
    c = Calc()

    with pytest.raises(ValueError):
        c.mul(3, 0)

def test_avg_correct_average():
    c = Calc()

    res = c.avg([2,3,4])

    assert res == 3

def test_avg_removes_upper_outliers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=90)
    
    assert res == c.avg([2,5,12])

def test_avg_removes_lower_outliers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], lt = 10)

    assert res == c.avg([12,98])

def test_avg_upper_threshold_is_included():
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=98)
    assert res == 29.25

def test_avg_empty_list():
    c = Calc()
    res = c.avg([])
    
    assert res == 0

def test_avg_manages_empty_list_after_outlier_removal():
    c = Calc()
    res = c.avg([12,98], lt=15, ut=90)

    assert res == 0

def test_avg_manages_empty_list_before_outlier_removal():
    c = Calc()
    res = c.avg([], lt=15, ut=90)

    assert res == 0
