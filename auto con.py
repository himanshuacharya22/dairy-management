import mysql.connector as sqltor
import pandas as pd
my=sqltor.connect(host='localhost',
user='root',password='1234',
database='cow_dairy_management')
c=my.cursor()
class Authentication(object):
    def __init__(self, username = ''):
        self.username = username

    def __lower(self):
        lower = any(c.islower() for c in self.username)
        return lower

    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        return upper

    def __digit(self):
        digit = any(c.isdigit() for c in  self.username)
        return digit

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)

        report =  lower and upper and digit and length >= 6

        if report:
            print("Username passed all checks ")
            return True

        elif not lower:
            print("You didnt use Lower case letter")
            return False

        elif not upper:
            print("You didnt userUpper case letter")
            return False

        elif length <6:
            print("username should Atleast have 6 character")
            return False

        elif not digit:
            print("You didnt use Digit")
            return False
        else:
            pass

C = Authentication("ga1Agdf")
print(C.validate())

select_customer="select distinct(customer_id),customer_name from sales_record"
print(C.username)
print(C.)
# print("-"*80)
# print(execute_select_customer.to_string(index=False))
# print("-"*80)
