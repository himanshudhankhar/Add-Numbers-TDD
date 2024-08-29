import pytest
from source.string_adder import add_string

def test_add_check_no_error_if_input_is_string():
    try:
        add_string("123")
    except Exception as exec:
        assert False, f"Exception thrown {exec} which was not expected"

def test_add_check_error_if_input_is_not_string():
    with pytest.raises(ValueError):
        add_string(1)

def test_add_should_return_zero_for_empty_string():
    result = add_string("")
    assert result == 0

def test_add_for_should_return_same_value_for_single_digit_number():
    result = add_string("2")
    assert result == 2
    result = add_string("5")
    assert result == 5

def test_should_throw_value_error_when_input_string_is_not_int_format():
    with pytest.raises(ValueError):
        add_string("abc")

def test_add_numbers_separated_by_comma():
    result = add_string("1,2")
    assert result == 3
    result = add_string("1,2,3")
    assert result == 6