from logging.config import valid_ident


my_dict = {v:v**2 for v in [1, 2, 3]}
print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dupl_list = list(set([item for item in some_list if some_list.count(item) > 1]))
print(dupl_list)