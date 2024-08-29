def add_string(input):
    if isinstance(input, str) == False:
        raise ValueError("Expected input type is a string")
    input = input.strip()
    if input == "":
        return 0
    input = give_input_arr(input)
    return add_list_of_numbers(input)

def give_input_arr(input_str):
    return input_str.split(',')

def add_list_of_numbers(input):
    result = 0
    for i in input:
        result += int(i)
    return result