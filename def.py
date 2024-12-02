def get_matrix(n, m, value): #задаем имя функции и параметры n, m, value
    matrix = [] #создаем пустой список для дальнейшего его редактирования
    for i in range(n): #создаем цикл for в котором добавляем логику под каждый параметр n, m, value
        matrix.append([])#добавляем в matrix столбцы пустых списков
        for j in range(m):# добавляем в m, параметр изменения колличества value
            matrix[i].append(value)
    print(matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

