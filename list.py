bicycles = ["treck", "stels", "merida"]
print (bicycles)

# Добавление элементов в Список
cars = ["BMW", "Mercedes", "Honda"]
bicycles.append(cars)
print (bicycles)
# ['treck', 'stels', 'merida', ['BMW', 'Mercedes', 'Honda']]
bicycles.append("new element")
print (bicycles)

# Вставка элементов в массив по индексу
new_arr = [1, 2, 3, 4, 5]
new_arr.insert(1, "some element")
print (new_arr)



# Удаление элементов из списка
del new_arr[1]
print(new_arr)

# Удаление элемента с использованием метода pop(), удалил последний элемент массива
new_arr.pop()
print(new_arr)

# Удаление определенного элемента с помощью remove()
new_arr.remove(2)
print(new_arr)

# вывод списка в обратном порядке с помощью reverse()
numbers = [5, 4, 3, 2, 1]
numbers.reverse()
print(numbers)

listNumbers = ["first", "second", "third", "four"]
listNumbers.reverse()
print(listNumbers)


# определение длины списка
lengthArray = ["Python", "JavaScript", "Java", "Swift"]
print (len(lengthArray)) # 4  4 это колличество индексов в списке (массиве)


#--------------------------- Работа со списками -------------------


# Перебор всего списка