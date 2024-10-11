# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month)
# and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

def is_year_leap(year): # validação de ano bissexto
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month): # quantidade de dias em determinado mês
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year): # no caso de fevereiro, a quantidade de dias no ano bissexto será 29
        return 29
    
    return days[month - 1]

def day_of_year(year, month, day): # identificação de quantidade de dias no ano
    if year < 1582:
        return None
    elif month > 12 or month < 1:
        return None
    elif day > days_in_month(year, month) or day < 1:
        return None
    
    total_days = day # quantidade de dias no ano recebe a quantidade de dias do mês inputado
    month -= 1 # enquanto o mês decrementa 1 (pois não considera o mês "corrente")

    while month > 0: # loop passa pelos meses
        total_days += days_in_month(year, month) # quantidade de dias do ano incrementa com os dias dos meses de acordo com a função definida lá em cima
        month -= 1 # quantidade de meses vai sendo decrementado

    return total_days

print(day_of_year(2000, 12, 31))