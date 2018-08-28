bicycles = ["treck", "stels", "merida"]
#print (bicycles)

# Добавление элементов в Список
cars = ["BMW", "Mercedes", "Honda"]
bicycles.append(cars)
print (bicycles)
# ['treck', 'stels', 'merida', ['BMW', 'Mercedes', 'Honda']]
bicycles.append("new element")
#print (bicycles)

# Вставка элементов в массив по индексу
new_arr = [1, 2, 3, 4, 5]
new_arr.insert(1, "some element")
#print (new_arr)



# Удаление элементов из списка
del new_arr[1]
#print(new_arr)

# Удаление элемента с использованием метода pop(), удалил последний элемент массива
new_arr.pop()
#print(new_arr)

# Удаление определенного элемента с помощью remove()
new_arr.remove(2)
#print(new_arr)

# вывод списка в обратном порядке с помощью reverse()
numbers = [5, 4, 3, 2, 1]
numbers.reverse()
#print(numbers)

listNumbers = ["first", "second", "third", "four"]
listNumbers.reverse()
#print(listNumbers)


# определение длины списка
lengthArray = ["Python", "JavaScript", "Java", "Swift"]
#print (len(lengthArray)) # 4  4 это колличество индексов в списке (массиве)


#--------------------------- Работа со списками -------------------


# Перебор всего списка, с помощью цикла for переберм каждый элемент массива и выведем их
magicPeople = ["David", "John", "Mary", "Bob", "Bruce", "Bill", "Sten", "Mikle"]

#for item in magicPeople:
  #  print (item + " work on monday") # "David", "John", "Mary", "Bob", "Bruce", "Bill", "Sten", "Mikle"



# функция range(numbers) 
for value in range(1, 5):
    print(value) # 1 2 3 4 - отсчет идет от 0, сдвиг, 5ка не берется в расчет, потому и вывод 4 числа


# использование range() для создания числового списка
someNumbers = list(range(1, 11))
print(someNumbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if len(someNumbers) >= 5:
    print ("numbers greater than 10")
else:
    print("numbers less than 10")


addTwo = list(range(2, 11, 2))
print(addTwo)
# двойка в конце говорит о том, что бы при создании чисел,
#  от 2й в начале, мы прибавляли каждый раз по "2ке" до тех пор,
#  пока не достигнем 11ти если это возможно в данном примере
# [2, 4, 6, 8, 10]


# возведем спислк квадартных целых чисел до 1 до 10 с помощью ** который возводт в степень
emptyList = []
for value in range(1, 11):
    number = value ** 2 # пройдя по списку от 1 до 10,
    # мы возводим во 2ю степень каждое число из списка и вкладываем его в пустой список
    # каждое новое число переумножается на 2 и мы получаем результат [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    emptyList.append(number) # вкладываем переменную number в пустой массив каждый раз при возведении в степень
print(emptyList)


# узнать минимум, максимум и сумму чисел в Списке с помощью min(), max(), sum()

digital = [1, 2, 3, 4, 5]
print(int(min(digital)), " minimal number") # 1
print(max(digital), " max number") # 5
print(sum(digital), " summ numbers") # 15



# -------- Генераторы списков
squaresNumber = [itemNumber ** 2 for itemNumber in range(1, 5)]
print(squaresNumber) # [1, 4, 9, 16]

#-------- срезы списков, метод slice()

players = ["Charlies", "Mishone", "Karl", "Billy", "Li", "Klementina"]
print(players) # "Charlies", "Mishone", "Karl", "Billy", "Li", "Klementina"
copy_players = players[:]
print(copy_players) # "Charlies", "Mishone", "Karl", "Billy", "Li", "Klementina"  создали копию списка
# если указать так [0:3] скопирует от 1го эл до 3го, если так [1:] то от 2го то последнего, если так [:] то весь список

players.append("new player")
copy_players.append("your friend join to Game")
print(players, " player list", copy_players," copy list players")