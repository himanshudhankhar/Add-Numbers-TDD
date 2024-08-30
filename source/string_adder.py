def add_string(input):
    if isinstance(input, str) == False:
        raise ValueError("Expected input type is a string")
    input = input.strip()
    if input == "":
        return 0
    input = generate_input_arr(input)
    return add_list_of_numbers(input)

def generate_input_arr(input_str):
    input =  input_str.split(',')
    result = []
    for i in input:
        if i == "":
            continue
        i_arr = i.split('\n')
        result = result + i_arr
    return result
    

def add_list_of_numbers(input):
    result = 0
    negative_numbers = []
    for i in input:
        i = int(i)
        if i < 0:
            negative_numbers.append(i)
        result += i
    if len(negative_numbers) != 0:
        raise ValueError(generate_negative_numbers_err_message(negative_numbers))
    return result

def generate_negative_numbers_err_message(numbers):
    numbers = [ str(i) for i in numbers]
    return "Negative numbers not allowed " + " ".join(numbers)