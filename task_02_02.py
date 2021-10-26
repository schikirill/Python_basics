initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(initial_list)
for element in range(len(initial_list)):
    if initial_list[element].isnumeric() and len(initial_list[element]) < 2:
        initial_list[element] = initial_list[element].replace(initial_list[element], '"0' + initial_list[element] + '"')
    if initial_list[element].isnumeric() and len(initial_list[element]) >= 2:
        initial_list[element] = initial_list[element].replace(initial_list[element], '"' + initial_list[element] + '"')
    if len(initial_list[element][1:]) < 2 and initial_list[element][0] in '+-':
        initial_list[element] = initial_list[element].replace(initial_list[element], '"' + initial_list[element][0] + '0' + initial_list[element][1:] + '"')
    if len(initial_list[element][1:]) > 1 and initial_list[element][0] in '+-':
        initial_list[element] = initial_list[element].replace(initial_list[element], '"' + initial_list[element][0] + initial_list[element][1:] + '"')

print(initial_list)
final_list = " ".join(initial_list)
print(final_list)