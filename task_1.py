numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_without_none = 0
count_without_none = 0
for num in numbers:
    if num is not None:
        sum_without_none += num
        count_without_none += 1
average_value = sum_without_none / len(numbers)
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average_value
print("Измененный список:", numbers, end='\n')
