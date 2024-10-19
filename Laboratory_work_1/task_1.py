numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

all_elements_sum = 0 #Сумма всех элементов != None
none_index = 0 #индекс элемента со значением None

for i in range(len(numbers)):
    if numbers[i] != None:
        all_elements_sum += numbers[i]
    else:
        none_index = i

numbers[none_index] = all_elements_sum / len(numbers)


print("Измененный список:", numbers)
