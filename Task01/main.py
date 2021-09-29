def set_the_number():   # Функція для задання розміру
    while True:
        try:
            numbers = input("Введіть кількість елементів у масиві: ")
            if numbers == 'exit':
                print('Програма завершила роботу')
                exit()
            else:
                numbers = int(numbers)
                if numbers <= 0:
                    while numbers <= 0:
                        numbers = int(input("Масив не може бути меншим або дорівнювати нулю!!!: "))
                return numbers
                break
        except ValueError:
            print("НЕ вірні дані! Спробуй ще разочок")

def create_an_array():   # Функція для створення масиву
    numbers = set_the_number()
    arr=[]
    for i in range(numbers):
        while True:
            try:
                arr.append(int(input("Введіь елемент: ")))
                break
            except ValueError:
                print("НЕ вірні дані! Спробуй ще разочок")
    return arr

def enter_range(arr):       # Функція для задання діапазону (-k; k)
    while True:
        try:
            min_value = abs(arr[1])
            for i in range(len(arr)):
                if abs(arr[i]) < min_value:
                    min_value = abs(arr[i])
            k = int(input("Введіть елемнт k: "))
            if k < min_value:
                while k < min_value:
                    k = int(input("Елемент знаходиться поза діапазоном, спробуйте ще: "))
            return k
        except ValueError:
            print("НЕ вірні дані! Спробуй ще разочок")

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
    c = create_an_array()
    a =find_the_item(c, enter_range(c))
    print("Останній елемент масиву, який знаходиться в діапазоні (-k; k): " + a[0])
    print("Індекс цього елементу: " + a[1])