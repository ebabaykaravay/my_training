my_dict = {'Egor': 1999, 'Anastasya': 1996}
my_dict['Evgenya'] = 1995
my_dict['Dmitrii'] = 2000
my_dict['Roma'] = 1998
print('Dict:', my_dict)
print('Existing value:', my_dict['Egor'])
print('Not existing value:', my_dict['Evgenya'])
del my_dict ['Dmitrii']
print('Deleted value:', my_dict)
print('Modified dictionary:', my_dict)


my_set = {1, 1, 1, 2, 3, 2, 2, 3, 3, 'string', (1, 2, 3)}
set_ = [1, 3, 4, 2, 3, 5]
print(set(set_))
my_set = set(set_)
print(my_set)
print(my_set.discard(1))
print(my_set.add(6))
print(my_set)
