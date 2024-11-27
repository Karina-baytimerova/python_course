# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    participants_group1 = group1.split(separator)
    participants_group2 = group2.split(separator)
    common_participants = []
    for participant in participants_group1:
        if participant in participants_group2:
            common_participants.append(participant)

    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, separator=',')
print(common_participants, end='\n')
