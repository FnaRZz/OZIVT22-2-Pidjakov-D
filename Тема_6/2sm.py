# для вывода текущего времени
import datetime
import random
a = datetime.datetime.now()
print (a)

# основной код
def remove_first_occurrence(tuple, element):
    try:
        tuple = tuple[:tuple.index(element)] + tuple[tuple.index(element) + 1:]
    except ValueError:
        pass
    return tuple


test_cases = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9),
]

for tuple, element in test_cases:
    modified_tuple = remove_first_occurrence(tuple, element)
    print(f"{tuple=}, обновленный: {modified_tuple}")