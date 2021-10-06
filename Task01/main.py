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

def set_the_number():   # Функція для задання розміру
    print("Введіть кількість елементів у масиві:")
    numbers = set_the_value()
    if numbers <= 0:
        while numbers <= 0:
            print("Масив не може бути меншим або дорівнювати нулю!!! Спробуй ще:")
            numbers = set_the_value()
    return numbers

def create_an_array():   # Функція для створення масиву
    numbers = set_the_number()
    arr = []
    for i in range(numbers):
        print("Введіь елемент масиву " + str(i + 1) + ":")
        element = set_the_value()
        arr.append(element)
    return arr

def enter_range(arr):       # Функція для задання діапазону (-k; k)
    min_value = abs(arr[1])
    for i in range(len(arr)):
        if abs(arr[i]) < min_value:
            min_value = abs(arr[i])
    print("Введіть елемнт k:")
    k = set_the_value()
    if k < min_value:
        while k < min_value:
            print("Елемент знаходиться поза діапазоном, спробуйте ще:")
            k = set_the_value()
    return k

def find_the_item(arr, k):    # Функція для знаходження останнього елементу масиву, що знаходиться в діапазоні (-k; k)
    y = len(arr) - 1
    while y >= 0:
        if -k < arr[y] < k:
            result = [str(arr[y]), str(arr.index(arr[y]))]
            return result
            break
        else:
            y -= 1

while True:
    arr = create_an_array()
    k = enter_range(arr)
    a =find_the_item(arr, k)
    print("Останній елемент масиву, який знаходиться в діапазоні (-k; k): " + a[0])
    print("Індекс цього елементу: " + a[1])