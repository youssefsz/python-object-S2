def fn_dict_pair_impair(list_numbers):
    d = {}
    for n in list_numbers:
        if n % 2 == 0:
            d[n] = "pair"
        else:
            d[n] = "impair"
    return d
list_numbers = [1, 2, 3, 4, 5]
print(fn_dict_pair_impair(list_numbers))