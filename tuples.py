#---- Кортежи

# --- кортежи это списки, только их нельзя изменить после их создания
dimensions = (200, 50)
print(dimensions[0], dimensions[1])
#dimensions[0] = 300 # TypeError: 'tuple' object does not support item assignment


old_tuples = (100, 200)
for item in old_tuples:
    print (item) # 100, 200

old_tuples = (400, 500)
for item in old_tuples:
    print(item) # 400, 500 переопределили Кортеж и его переменную
    