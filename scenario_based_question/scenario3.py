# # This code handles only capital letters and only one-digit numbers inside strings.
# input='A3X4Z3'
# output= 'ADXBZC'
#
# string1 = 'AD44EG2H2J1'
# list1 = []
# digit_string = ''
# latest_char = None
#
#
# def find_next_char(latest_character, int_string):
#     ord_latest = ord(latest_character)
#     ord_sum = ord_latest + int(int_string)
#     if ord_sum > ord('Z'):
#         ord_diff = ord_sum - ord('Z')
#         ord_reminder = ord_diff % 26
#         next_character = chr((ord('A') - 1) + ord_reminder)
#
#         return next_character
#     else:
#         ord_latest = ord(latest_character)
#         ord_sum = ord_latest + int(int_string)
#         next_character = chr(ord_sum)
#         return next_character
#
#
# for ele in string1:
#     if ele.isalpha():
#         if digit_string:
#             next_char = find_next_char(latest_char, digit_string)
#             list1.append(next_char)
#             digit_string = ''
#         latest_char = ele
#         list1.append(latest_char)
#
#     elif ele.isdigit():
#         digit_string += ele
#
# else:
#     if digit_string:
#         next_char = find_next_char(latest_char, digit_string)
#         list1.append(next_char)
#
# output = ''.join(list1)
# print(output)

# ----------------------------------------------------------------------------------------------------------------------
# # This code handles only capital as well as small letters and any-digit numbers inside strings.

# input='A3G4B2'
# # output= 'ADGKBD'
#
# input='A3X4Z3'
# # output= 'ADXBZC'
#

# input = 'D44j2Jm1Z1z1'
# print(input)
# output = 'DVjlJmn'
#
# list1 = []
# digit_string = ''
# latest_char = None
# case = ''
#
#
# def find_next_char(latest_character, int_string, case_check):
#     ord_latest = ord(latest_character)
#     ord_sum = ord_latest + int(int_string)
#     if case_check == 'upper':
#         ord_first, ord_last = ord('A'), ord('Z')
#     else:
#         ord_first, ord_last = ord('a'), ord('z')
#
#     if ord_sum > ord_last:
#         ord_diff = ord_sum - ord_last
#         ord_reminder = ord_diff % 26
#         next_character_ord = (ord_first - 1) + ord_reminder
#         next_character = chr(next_character_ord)
#         return next_character
#     else:
#         ord_latest = ord(latest_character)
#         ord_sum = ord_latest + int(int_string)
#         next_character = chr(ord_sum)
#         return next_character
#
#
# for ele in input:
#     if ele.isalpha():
#         if digit_string:
#             next_char = find_next_char(latest_char, digit_string, case)
#             list1.append(next_char)
#             digit_string = ''
#         latest_char = ele
#
#         if latest_char.isupper():
#             case = 'upper'
#         else:
#             case = 'lower'
#
#         list1.append(latest_char)
#
#     elif ele.isdigit():
#         digit_string += ele
#
# else:
#     if digit_string:
#         next_char = find_next_char(latest_char, digit_string, case)
#         list1.append(next_char)
#
# output = ''.join(list1)
# print(output)