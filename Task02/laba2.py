def set_the_value():   # Функція для задання і перевірки значень
    while True:
        try:
            value = input()
            if value == 'exit':
                print('Програма завершила роботу')
                exit()
            else:
                return int(value)
            break
        except ValueError:
            print("НЕ вірні дані! Спробуй ще разочок")

def set_the_number_row():   # Функція для задання розміру
    print("Введіть кількість рядків у матриці:")
    numbers = set_the_value()
    if numbers <= 0:
        while numbers <= 0:
            print("Значення не може бути меншим або дорівнювати нулю!!!:")
            numbers = set_the_value()
    return numbers

def set_the_number_column():   # Функція для задання розміру
    print("Введіть кількість стовпців у матриці:")
    numbers = set_the_value()
    if numbers <= 0:
        while numbers <= 0:
            print("Значення не може бути меншим або дорівнювати нулю!!!:")
            numbers = set_the_value()
    return numbers

def create_an_matrix():   # Функція для створення матриці
    global n, m
    n = set_the_number_row()
    m = set_the_number_column()
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(m):
            print("Введіть елемент а[" + str(i + 1) + "][" + str(j + 1) + "]: ")
            element = set_the_value()
            arr[i] += [element]
    return arr

def search_special_items(arr):
    global n, m
    special = 0
    for i in range(m):
        sum = 0
        for j in range(n):
            sum += arr[j][i]
        for j in range(n):
            if arr[j][i] > sum - arr[j][i]:
                special += 1
    return special

while True:
    arr = create_an_matrix()
    sp_items = search_special_items(arr)
    print('Кількість "особливих" елементів: ' + str(sp_items))
    print("Якщо бажаєте завершити роботу програми введіть exit.")