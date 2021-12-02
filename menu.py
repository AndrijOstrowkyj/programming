from collectionTaxFree import TaxFreeCollection

collectionTaxFree = TaxFreeCollection()

def menu():
    while True:
        option = input('Ведіть:\n1 -  якщо ви хочете додати елемент до файлу\n'
                       '2 - якщо ви хочете сортувати файл\n'
                       '3 - якщо ви хочете знайти елемент\n'
                       '4 - якщо ви хочете видалити елемент по його ID\n'
                       '5 - якщо ви хочете змінити елемент по його ID\n'
                       '6 - якщо ви хочете побачити весь файл\n'
                       '7 - якщо ви хочете вийти\n')

        if option == '1':
            collectionTaxFree.addNew()
            collectionTaxFree.saveChanges()
        elif option == '2':
            collectionTaxFree.sort()
            collectionTaxFree.display()
        elif option == '3':
            collectionTaxFree.find()
        elif option == '4':
            collectionTaxFree.deleteByID()
            collectionTaxFree.saveChanges()
            collectionTaxFree.display()
        elif option == '5':
            collectionTaxFree.edit()
            collectionTaxFree.display()
        elif option == '6':
            collectionTaxFree.display()
            collectionTaxFree.saveChanges()
        elif option == '7':
            print('Програма завершилася...')
            exit()
        else:
            print('Будь ласка, введіть одне із значень доступних в меню!')
            menu()

menu()