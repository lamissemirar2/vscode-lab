from sum_positive import sum_positive

def test_sum_positive():
    assert sum_positive([1, 2, 3]) == 6
    assert sum_positive([0, 5, 10]) == 15
    try:
        sum_positive([1, -2, 3])
    except ValueError as e:
        assert str(e) == "Negative number detected"
