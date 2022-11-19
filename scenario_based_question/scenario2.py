# data = [
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {'dsi': 'test', 'asv': 'us1'},
#     {'dsi': 'test', 'asv': 'us2'}
# ]
#
# new_data, final_list = [], []
# [new_data.append(a) for a in data if a not in new_data]
# print(new_data)
# print()
# for i in range(len(new_data)):
#     dummy_list_dsi, dummy_list_asv, dummy_dict = [], [], {}
#     for j in range(len(new_data)):
#         if new_data[i]['dsi'] == new_data[j]['dsi']:
#             dummy_list_asv.append(new_data[j]['asv'])
#
#     if len(dummy_list_asv) == 1:
#         asv_str = ''.join(dummy_list_asv)
#         dummy_dict['dsi'] = new_data[i]['dsi']
#         dummy_dict['asv'] = asv_str
#     else:
#         dummy_dict['dsi'] = new_data[i]['dsi']
#         dummy_dict['asv'] = dummy_list_asv
#
#     if dummy_dict not in final_list:
#         final_list.append(dummy_dict)
#
# print(final_list)

# ----------------------------------------------------------------------------------------------------------------------
#
# data = [
#     {'dsi': 'test', 'asv': 'NY1'},
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {"dsi": 'uk1', 'asv': 'abc'},
#     {"dsi": 'abc', 'asv': 'uk1'},
#     {'dsi': 'test', 'asv': 'us1'},
#     {'dsi': 'test', 'asv': 'us2'},
#     # {'dsi': 'test', 'asv': 'NY1'},
#     {'dsi': 'pqr', 'asv': 'NY1'},
#     {'dsi': 'xyz', 'asv': 'NY1'},
#     {'dsi': 'rst', 'asv': 'NY3'}
# ]
# data = [{'dsi': '1', 'asv': '2'},
#         {'dsi': '1', 'asv': '3'},
#         {'dsi': '4', 'asv': '2'}
#         ]

# new_data, final_list = [], []
# dsi_value, asv_value = [], []
# [new_data.append(a) for a in data if a not in new_data]
# print(new_data)
# print()
# for i in range(len(new_data)):
#     dummy_list_dsi, dummy_list_asv, dummy_dict, dummy_dict2 = [], [], {}, {}
#     for j in range(len(new_data)):
#         if new_data[i]['dsi'] == new_data[j]['dsi']:
#             dummy_list_asv.append(new_data[j]['asv'])
#
#         if new_data[i]['asv'] == new_data[j]['asv']:
#             dummy_list_dsi.append(new_data[j]['dsi'])
#
#     if len(dummy_list_asv) == 1:
#
#         asv_str = ''.join(dummy_list_asv)
#         dummy_dict['dsi'] = new_data[i]['dsi']
#         dummy_dict['asv'] = asv_str
#     else:
#         dummy_dict['dsi'] = new_data[i]['dsi']
#         dummy_dict['asv'] = dummy_list_asv
#         dsi_value.append(new_data[i]['dsi'])
#
#     if len(dummy_list_dsi) == 1:
#
#         dsi_str = ''.join(dummy_list_dsi)
#         dummy_dict2['dsi'] = dsi_str
#         dummy_dict2['asv'] = new_data[i]['asv']
#     else:
#         dummy_dict2['dsi'] = dummy_list_dsi
#         dummy_dict2['asv'] = new_data[i]['asv']
#         asv_value.append(new_data[i]['asv'])
#
#     if dummy_dict not in final_list and (new_data[i]['asv'] not in asv_value):
#         final_list.append(dummy_dict)
#
#     if dummy_dict2 not in final_list and (new_data[i]['dsi'] not in dsi_value):
#         final_list.append(dummy_dict2)
#
# print(final_list)
