lst_1 = [1, 3, [1, 2, 3]]
lst_2 = lst_1[::]
print(lst_1,lst_2)
#lst_1[-1] = 1
# lst_1[-1] = [1, 2, 3]
# print(lst_1,lst_2)
lst_1[-1][0] = 2
print(lst_1,lst_2)

../87


