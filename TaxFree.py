import enum
from Inputs import *
from Input import *
from datetime import datetime
from validationForTaxFree import *

class TAX_FREE(object):

    def __init__(self, ID=None, Company=None, Country=None, vat_rate=None, date_of_purchase=None, vat_code=None,
             date_of_tax_free_registration=None):
        self.ID = Input(ID, 'ID', [VALIDATION.validateInteger, VALIDATION.validatePositive])
        self.Company = Input(Company, 'Company', [VALIDATION.validateRequiredStringWithTrim])
        self.Country = Input(Country, 'Country (Italy or Germany or France)',
                             [lambda value: VALIDATION.validateEnumValue(value, CountryEnum)])
        self.vat_rate = InputInteger(vat_rate, "Vat rate", [lambda x: 0 < x < 41])
        self.date_of_purchase = InputDate(date_of_purchase, "Date of purchase", [VALIDATION.validateDateString])
        self.vat_code = Input(vat_code, "Vat code (in kind VA***_**_***)",
                              [lambda x: VALIDATION.patternValidation(x, "^VA.{3,3}_.{2,2}_.{3,3}$")])
        self.date_of_tax_free_registration = InputDate(date_of_tax_free_registration,
                                                       "Date of tax free registration",
                                                       [VALIDATION.validateDateString,
                                                        lambda x: VALIDATION.validateLowerDateInputFile(
                                                            self.date_of_purchase, x,
                                                            "Date of tax free registration must be more date of purchase")])

        self.inputValues = Inputs([
            self.ID,
            self.Company,
            self.Country,
            self.vat_rate,
            self.date_of_purchase,
            self.vat_code,
            self.date_of_tax_free_registration])

    def validate(self):
        self.inputValues.validate()

    def checkIsValid(self):
        return self.inputValues.get_isValid()

    def get_ID(self):
        return self.ID.value

    def get_Company(self):
        return self.Company.value

    def get_Country(self):
        return self.Country.value

    def get_vat_rate(self):
        return self.vat_rate.value

    def get_date_of_purchase(self):
        return self.date_of_purchase.value

    def get_vat_code(self):
        return self.vat_code.value

    def get_date_of_tax_free_registration(self):
        return self.date_of_tax_free_registration.value

    def enterCompany(self):
        value = input(f'Введіть назву комапнії: ')
        if self.set_Company(value) is False:
            self.enterCompany()


    def set_Company(self, value):
        self.Company.value = value
        if VALIDATION.validateRequiredStringWithTrim is True:
            self.Company.value = value
            return True
        else:
            return False

    def enterCountry(self):
        value = input(f'Введіть назву країни: (Italy або Germany або France): ')
        if self.set_Country(value) is False:
            self.enterCountry()

    def set_Country(self, value):
        if VALIDATION.validateEnumValue(value, CountryEnum) is True:
            self.Country.value = value
            return True
        else:
            return False

    def enterVat_Rate(self):
        value = input(f'Введіть ставку ПДВ: ')
        if self.set_vat_rate(value) is False:
            self.enterVat_Rate()


    def set_vat_rate(self, value):
        if VALIDATION.validateInteger(value) and (0 < int(value) < 41) is True:
            self.vat_rate.value = int(value)
            return True
        else:
            return False

    def enterDate_of_tax_free_registration(self):
        value = input(f'Введіть дату неоподатковуваної реєстрації у форматі РРРР-ММ-ДД:')
        if self.set_Date_of_tax_free_registration(value, self.date_of_purchase.value) is False:
            self.enterDate_of_tax_free_registration()


    def set_Date_of_tax_free_registration(self, value, date_of_purchase):
        self.date_of_tax_free_registration.value = value
        if VALIDATION.validateDateString(value) and VALIDATION.validateLowerDate(datetime.strptime(date_of_purchase, '%Y-%m-%d'), datetime.strptime(value, '%Y-%m-%d'), "Дата реєстрації початку податкування має бути більше дати покупки") is True:
            self.date_of_tax_free_registration.value = value
            return True
        else:
            return False

    def enterVat_code(self):
        value = input(f'Введіть КОД ПДВ: ')
        if self.set_vatCode(value) is False:
            self.enterVat_code()

    def set_vatCode(self, value):
        if VALIDATION.patternValidation(value, "^VA.{3,3}_.{2,2}_.{3,3}$") is True:
            self.vat_code.value = value
            return True
        else:
            return False

    def enterDate_of_purchase(self):
        value = input(f'Введіть дату покупки у форматі РРРР-ММ-ДД: ')
        if self.set_Date_of_purchase(value) is False:
            self.enterDate_of_purchase()

    def set_Date_of_purchase(self, value):
        if VALIDATION.validateDateString is True:
            self.date_of_purchase.value = value
            return True
        else:
            return False

    def toJson(self):
        return {
            "ID": self.ID.value,
            "Company": self.Company.value,
            "Country": self.Country.value,
            "vat_rate": self.vat_rate.value,
            "date_of_purchase": str(self.date_of_purchase.value),
            "vat_code": self.vat_code.value,
            "date_of_tax_free_registration": str(self.date_of_tax_free_registration.value)
        }

    def display(self):
        print(self.toJson())


class CountryEnum(str, enum.Enum):
    Germany = "Germany"
    Italy = "Italy"
    France = "France"