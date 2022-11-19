# input = 'h2g3k1'
# output = 'hhgggk'

input_string = 'h3g1k11'
lst = []
latest_char = None
string_digit = ''


def string_digit_conversion(latest_character, string_digit_input):
    int_digit = int(string_digit_input)
    return (int_digit - 1) * latest_character


for char in input_string:

    if char.isalpha():
        if string_digit:
            char_multiply = string_digit_conversion(latest_char, string_digit)
            lst.append(char_multiply)
            string_digit = ''

        latest_char = char
        lst.append(latest_char)

    elif char.isdigit():
        string_digit += char

else:
    if string_digit:
        char_multiply = string_digit_conversion(latest_char, string_digit)
        lst.append(char_multiply)
        string_digit = ''

output_string = ''.join(lst)
print(output_string)
