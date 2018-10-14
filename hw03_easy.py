# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    rounded = number // 1
    idx = 1
    while(ndigits >= 0):
        digit = ((10**idx)*number % 10) // 1
        if ndigits != 0 :
            rounded += digit / (10**idx)
        elif digit >= 5 :
            rounded += 1 / (10**(idx - 1))
        ndigits -= 1
        idx += 1
    return rounded

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    first_digits = ticket_number // 1000
    last_digits = ticket_number % 1000
    def sum_of_digits(number):
        sum = 0
        while number != 0:
            digit = number % 10
            sum += digit
            number = number // 10
        return sum
    return sum_of_digits(first_digits) == sum_of_digits(last_digits)

print(lucky_ticket(123006))
print(lucky_ticket(123121))
print(lucky_ticket(436751))
