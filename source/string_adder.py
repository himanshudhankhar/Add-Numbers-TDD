def add_string(input):
    if isinstance(input, str) == False:
        raise ValueError("Expected input type is a string")
    input = input.strip()
    if input == "":
        return 0
    return int(input)