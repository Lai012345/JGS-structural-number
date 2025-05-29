from structural_number import FocusedValue, structural_sum, focus_count

def test_structural_sum():
    items = [FocusedValue(10, True), FocusedValue(5, False)]
    assert structural_sum(items) == 10
    assert focus_count(items) == 1
