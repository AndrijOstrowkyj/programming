import re
import datetime
import functools

class VALIDATION:

    @staticmethod
    def validation_decorator(checkIsValid):
        def decorator(fun):
            def wrapper(*args, **kwargs):
                isValid = checkIsValid(args[1])

                if isValid is False:
                    return False
                return fun(*args)
            return wrapper
        return decorator

    @staticmethod
    def validation_decorator_with_two_arguments(checkIsValid):
        def decorator(fun):
            def wrapper(*args, **kwargs):
                isValid = checkIsValid(args[1], args[2])

                if isValid is False:
                    return False
                fun(*args)
            return wrapper
        return decorator

    @staticmethod
    def patternValidation(value, regEx):
        pattern = re.compile(regEx)
        if pattern.match(value):
            return True

        print(f'Невірне значення {value}: має відповідати регулярному виразу {regEx}')
        return False

    @staticmethod
    def validateDateString(value):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            print("Некоректний формат дати, мусить бути вигляд YYYY-MM-DD")
            return False

    @staticmethod
    def validateInteger(value):
        try:
            int(value)
            return True
        except ValueError:
            print(f'Значення {value} мусить бути цілочисельне')
            return False

    @staticmethod
    def validatePositive(value):
        if value < 0:
            print(f'Значення {value} мусить бути додатнє')
            return False

        return True

    @staticmethod
    def validateEnumValue(value, Enum):
        validValues = tuple(item.value for item in Enum)

        if value in validValues:
            return True

        print(f'Неправильні данні: {value}')
        return False

    @staticmethod
    def validateRequiredStringWithTrim(value):
        if len(value.strip()) > 0:
            return True

        print("Значення порожнє")
        return False

    @staticmethod
    def validateLowerDateInputFile(value1, value2, invalidDataMessages):
        if value1.value <= value2:
            return True
        print(invalidDataMessages)
        return False

    @staticmethod
    def validateLowerDate(value1, value2, invalidDataMessages):
        if value1 <= value2:
            return True
        print(invalidDataMessages)
        return False

    @staticmethod
    def readInteger(inputMessage, invalidDataMessages):
        data = input(inputMessage)

        try:
            data = int(data)
        except ValueError:
            print(invalidDataMessages)
            return VALIDATION.readInteger(inputMessage, invalidDataMessages)

        return data

    @staticmethod
    def readIntegerWithCheck(inputMessage, isValid, invalidInputMessage=''):
        data = input(inputMessage)

        try:
            data = int(data)
        except ValueError:
            print('Дані повинні бути представлені додатним числом!')
            return VALIDATION.readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

        if not isValid(data):
            print(invalidInputMessage)
            return VALIDATION.readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

        return data