def add_string(input):
    if isinstance(input, str) == False:
        raise ValueError("Expected input type is a string")
    input = input.strip()
    if input == "":
        return 0
    delimiter, input = extract_delimiter(input)
    input = generate_input_arr(input, delimiter)
    return add_list_of_numbers(input)

def generate_input_arr(input_str, delimiter):
    input =  input_str.split(delimiter[:1])
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

def extract_delimiter(input):
    first_char = input[:1]
    if first_char == '-' and input[1:2].isnumeric():
        return ',', input
    
    if first_char.isnumeric() == False:
        delimiter = first_char
        modified_input = input[2:]
        return delimiter, modified_input
    else:
        delimiter = ','
        for i in input:
            if str(i).isnumeric() == False and str(i) != '\n':
                delimiter = i
                return delimiter, input
        return delimiter, input

    