def sanitize_input(input_string):
    harmful_chars = [';', "'", '"', '<', '>', '|', '&']
    for char in harmful_chars:
        input_string = input_string.replace(char, '')
    return input_string
