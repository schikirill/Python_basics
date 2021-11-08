import sys

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'John', 'William', 'Elvis']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def tut_klass(tutors, klasses):
    if len(tutors) > len(klasses):
        while len(tutors) > len(klasses):
            klasses.append('None')
        for tutors, klasses in zip(tutors, klasses):
            yield tutors, klasses


excess_tutors = tut_klass(tutors, klasses)
print(type(excess_tutors), sys.getsizeof(excess_tutors))  # <class 'generator'> 104 - ЧТД
print(next(excess_tutors))  # ('Иван', '9А')
print(next(excess_tutors))  # ('Анастасия', '7В')
print(next(excess_tutors))  # ('Петр', '9Б')
print(next(excess_tutors))  # ('Сергей', '9В')
print(next(excess_tutors))  # ('Дмитрий', '8Б')
print(next(excess_tutors))  # ('Борис', '10А')
print(next(excess_tutors))  # ('Елена', '10Б')
print(next(excess_tutors))  # ('John', '9А')
print(next(excess_tutors))  # ('William', 'None')
print(next(excess_tutors))  # ('Elvis', 'None')
print(next(excess_tutors))  # StopIteration
