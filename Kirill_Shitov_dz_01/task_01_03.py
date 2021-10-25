text_1 = "процент"
text_2_4 = "а"
text_5_0 = "ов"
for i in range(1, 101):
    if i % 10 in range(5, 10) or i % 10 == 0:
        print(i, text_1 + text_5_0)
    if i % 10 == 1 and i != 11:
        print(i, text_1)
    else:
        if i == 11:
            print(i, text_1 + text_5_0)
    if i % 10 in range(2, 5) and not 12 <= i <= 14:
        print(i, text_1 + text_2_4)
    else:
        if 12 <= i <= 14:
            print(i, text_1 + text_5_0)