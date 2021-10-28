def thesaurus(*args):
    first_letters = {}
    names_dict = {}
    for name in args:
        first_letter = name[0]
        first_letters.setdefault(first_letter)
    for letter in first_letters:
        names_list = []
        for name in args:
            if name[0] == letter:
                 names_list.append(name)
        names_dict[letter] = names_list
    return names_dict


print(thesaurus("Пафнутий", "Иван", "Мария", "Илья", "Петр", "Кирилл", "Иннокентий"))