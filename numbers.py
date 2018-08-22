# целые числа и работа с ними

print (3 * 2) # 6
print (3 ** 2) # 9 возвели в степень
print ((2 + 5) - (2 * 2 + 10) * 5) # раставиои приоритет выполнения действий


# вещественные числа - дробные числа
print (0.2 + 0.5)
print (2 + 0.1 ** 0.5)


# str() превращает числа в строку
# example:
age = 23
#message = "Happy " + age + "rd Birthday!"
#print (message)
# TypeError: must be str, not int 

message = "Happy " + str(age) + "rd Birthday!"
print (message)
# Happy 23rd Birthday!

