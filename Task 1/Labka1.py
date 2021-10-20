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

def create_an_array(numbers):   # Функція для створення масиву
    arr=[]
    for i in range(numbers):
        while True:
            try:
                arr.append(int(input("Введіь елемент: ")))
                break
            except ValueError:
                print("НЕ вірні дані! Спробуй ще разочок")
    return arr

def find_the_item(numbers, arr):    # Функція для знаходження останнього елементу масиву, що знаходиться в діапазоні (-k; k)
    while True:
        try:
            min_value = abs(arr[1])
            for i in range(numbers):
                if abs(arr[i]) < min_value:
                    min_value = abs(arr[i])
            k = int(input("Введіть елемнт k: "))
            if k < min_value:
                while k < min_value:
                    k = int(input("Елемент знаходиться поза діапазоном, спробуйте ще: "))
            y = numbers - 1
            while y >= 0:
                if -k < arr[y] < k:
                    print("Останній елемент масиву, який знаходиться в діапазоні (-k; k): " + str(arr[y]))
                    print("Індекс цього елементу: " + str(arr.index(arr[y])))
                    break
                else:
                    y -= 1
            break
        except ValueError:
            print("НЕ вірні дані! Спробуй ще разочок")

while True:
    n = set_the_number()
    find_the_item(n, create_an_array(n))