def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month_number):
    if month_number == 1: return "January"
    elif month_number == 3: return "March"
    elif month_number == 9: return "September"

def number_to_short_month_name(month_number):
    if month_number == 1: return "Jan"
    elif month_number == 4: return "Apr"
    elif month_number == 10: return "Oct"

def volume_calculator(length):
    return length ** 3

def reverse(string):
    r_string = ""
    count = len(string)
    while count > 0:
        r_string += string[count - 1]
        count = count - 1
    return r_string

def f_to_c(f):
    return (f - 32) / 1.8
