from validationForTaxFree import *


class Input(object):

    def __init__(self, value, valueName, validations=[]):
        self.value = value
        self.validations = validations
        self.valueName = valueName

    def readValue(self):
        value = input(f'Введіть {self.valueName}: ')
        isValid = self.validate(value)

        if isValid:
            self.value = value
            return

        self.readValue()

    def readValue2(self):
        value = input(f'Введіть {self.valueName}: ')

        self.value = value
        return value

    def get_isValid(self):
        return self.validate(self.value)

    def validate(self, value):
        for validation in self.validations:
            if not validation(value):
                print(f'{self.valueName} - помилка')
                return False

        return True


class InputInteger(Input):

    def readValue(self):
        value = VALIDATION.readInteger(f'Введіть {self.valueName}: ', 'Значення мусить бути цілочисельне')
        isValid = self.validate(value)

        if isValid:
            self.value = value
            return

        self.readValue()


class InputDate(Input):

    def readValue(self):
        print(f'Введіть {self.valueName}: ')
        value = self.getDate()
        isValid = self.validate(str(value))

        if isValid:
            self.value = str(value)
            return

        self.readValue()

    def getDate(self):
        year = VALIDATION.readIntegerWithCheck('Введіть рік : ', lambda x: 0 < x < 2021, 'Невірні данні, спробуйте ще ')
        month = VALIDATION.readIntegerWithCheck('Введіть місяць : ', lambda x: 0 < x < 13, 'Невірні данні, спробуйте ще ')
        day = VALIDATION.readIntegerWithCheck('Введіть дату : ', lambda x: 0 < x < 31, 'Невірні данні, спробуйте ще ')
        date = datetime.date(year, month, day)
        return date