from utils import is_prime, is_power_of_5, is_power_of_2

number = 17
if is_prime(number):
    print(f"{number} є простим числом")
else:
    print(f"{number} не є простим числом")

number = 125
if is_power_of_5(number):
    print(f"{number} є степенем 5")
else:
    print(f"{number} не є степенем 5")

number = 16
if is_power_of_2(number):
    print(f"{number} є степенем 2")
else:
    print(f"{number} не є степенем 2")

