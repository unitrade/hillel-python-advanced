def _filter(func, iter_list):
    return (item for item in iter_list if func(item))


lst = [4, 5, 7, 8]

filtered_lst = _filter(lambda x: x < 6, lst)
print(list(filtered_lst))
for i in filtered_lst:
    print(i)
