broken_name_list =['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                   'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in range(len(broken_name_list)):
    print(f'Привет, {broken_name_list[element].split().pop().title()}!')