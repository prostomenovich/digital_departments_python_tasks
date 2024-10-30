# TODO Напишите функцию find_common_participants

def find_common_participants(first_string, second_string, separator=","):
    first_group_set = set(first_string.split(separator))
    second_group_array = second_string.split(separator)

    return sorted(list(first_group_set.intersection(second_group_array)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))
