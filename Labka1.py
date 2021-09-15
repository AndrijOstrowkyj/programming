from array import *

def set_the_number():   # Функція для задання розміру
    while True:
        try:
            numbers = int(input("Введіть розмір: "))
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
            min_value = arr[1]
            for i in range(numbers):
                if a[i] < min_value:
                    min_value = a[i]
            k = int(input("Введіть елемнт k: "))
            if k < min_value:
                while k < min_value:
                    k = int(input("Елемент знаходиться поза діапазоном, спробуйте ще: "))
            y = numbers - 1
            while numbers >= 0:
                if arr[y] < k and arr[y] > -k:
                    print(arr[y])
                    print(arr.index(arr[y]))
                    break
                else:
                    y -= 1
            break
        except ValueError:
            print("НЕ вірні дані! Спробуй ще разочок")

n = set_the_number()
a = create_an_array(n)
find_the_item(n, a)