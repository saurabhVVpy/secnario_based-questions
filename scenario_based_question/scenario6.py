# sample_data = [{'item': 'item1', 'amount': 400},
#               {'item': 'item2', 'amount': 300},
#               {'item': 'item1', 'amount': 750}]
#
# new_dict = {}
#
# item = [a['item'] for a in sample_data]
# amount = [a['amount'] for a in sample_data]
# print(item)
# print(amount)
#
# item_list = list(set(item))
# for i in item_list:
#     sum = 0
#     counter = 0
#     for j in item:
#         if i == j:
#             sum += amount[counter]
#         counter += 1
#     new_dict[i] = sum
#
# print(new_dict)
# -----------------------------------------------------------------------------------------------------------------------

sample_data = [{'item': 'item1', 'amount': 400},
              {'item': 'item2', 'amount': 300},
              {'item': 'item1', 'amount': 750}]

new_dict = {}

list_dict = []

item = [a['item'] for a in sample_data]
amount = [a['amount'] for a in sample_data]
print(item)
print(amount)

item_list = list(set(item))
item_list.sort()

for i in item_list:
    sum = 0
    counter = 0
    for j in item:
        if i == j:
            sum += amount[counter]
        counter += 1
    new_dict[i] = sum

for key, value in new_dict.items():
    new_dict2 = {'item': key, 'amount': value}
    list_dict.append(new_dict2)
print(list_dict)
