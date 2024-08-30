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

def test_add_numbers_separated_by_comma_or_newline_but_not_both():
    result = add_string("1,2\n3")
    assert result == 6
    result = add_string("1\n2\n3,4")
    assert result == 10
    result = add_string("\n1\n2\n3,5,")
    assert result == 11

def test_should_throw_error_when_some_negative_number_is_given_as_input():
    with pytest.raises(ValueError) as err:
        add_string("1,-2,-3")
    assert str(err.value.args[0]) == 'Negative numbers not allowed -2 -3'

def test_add_support_for_different_delimiters():
        result = add_string(";\n1;2;3")
        assert result == 6
        result = add_string(";\n1\n4;3")
        assert result == 8
        result = add_string("-\n1\n4-3")
        assert result == 8
        result = add_string("|\n1\n4|3")
        assert result == 8
def test_check_if_minus_sign_is_not_picked_as_delimiter_when_it_was_not_intended_as_delimiter():
    with pytest.raises(ValueError) as err:
        add_string("-1,2,3")
    assert str(err.value.args[0]) == 'Negative numbers not allowed -1'

def test_check_error_raised_when_delimiter_is_used():
    with pytest.raises(ValueError) as err:
        add_string(";\n-1;2;3")
    assert str(err.value.args[0]) == 'Negative numbers not allowed -1'