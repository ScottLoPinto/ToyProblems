from switch_sort import switch_sort

def test_first():
    assert switch_sort([1, 2, 4, 3]) == 1

def test_second():
    assert switch_sort([1, 2, 3, 4]) == 0

def test_third():
    assert switch_sort([3, 4, 2, 1]) == 3

def test_fourth():
    assert switch_sort([1, 3, 4, 2]) == 2

def test_five():
    assert switch_sort([3, 1, 2]) == 2

def test_six():
    assert switch_sort([4, 3, 2, 1]) == 2

def test_seven():
    assert switch_sort([5, 4, 3, 2, 1]) == 2

def test_eight():
    assert switch_sort([2, 1]) == 1

def test_nine():
    assert switch_sort([5, 3, 4, 1, 2]) == 4

def test_ten():
    assert switch_sort([5, 4, 3, 1, 2]) == 3

def main():
    test_first()
    test_second()
    test_third()
    test_fourth()
    test_five()
    test_six()
    test_seven()
    test_eight()
    test_nine()
    test_ten()

if __name__ == '__main__':
    main()