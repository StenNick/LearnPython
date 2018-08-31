#------- Словари (Объекты)

aliens = {
    "color" : "black",
    "race"  : "Alien",
    "power" : "Undead",
    "type"  : "Monster"
}

print(aliens["color"])

#--- добавим напрямую новое пара-значение для Словаря

aliens["weapon"] = "acid"
aliens["blood"] = "danger"

print(aliens)
# {'color': 'black', 'race': 'Alien', 'power': 'Undead', 'type': 'Monster', 'weapon': 'acid', 'blood': 'danger'}

#--- Удаление пар - ключ значение

del aliens["blood"]
print(aliens) # {'color': 'black', 'race': 'Alien', 'power': 'Undead', 'type': 'Monster', 'weapon': 'acid'}


favorite_languages = {
    "Sarah" : "JavaScript",
    "Bob"   : "Python",
    "Jack"  : "Lisp",
    "Greg"  : "PHP",
    "Shon"  : "Perl"
}

friends = ["Jack", "Greg", "Bob"]

#--- посмотрим все свойства словаря с помощью for

for key, value in favorite_languages.items():
    print("Key - " + key, " : value - " + value)
# Key - Sarah  value - JavaScript
# Key - Bob  value - Python
# Key - Jack  value - Lisp
# Key - Greg  value - PHP
# Key - Shon  value - Perl


#--- перебор всех КЛЮЧЕЙ в словаре

for name in favorite_languages.keys():
    print(name.title()) 
# Sarah
# Bob  
# Jack 
# Greg 
# Shon 

for name in friends:
    print(" Hi " + name.title() + " i see your favorite language is  " + favorite_languages[name] + " !") # выведет сообщение если ключ в словаре похож на свойство списка


propertyObject = {
    3 : "Car",
    2 : "Train",
    4 : "Boat",
    1 : "Bike"
}

for order in sorted(propertyObject.keys()):
    print(str(order) + " thank you for sorted list object keys!")
    # 1 thank you for sorted list object keys!
    # 2 thank you for sorted list object keys!
    # 3 thank you for sorted list object keys!
    # 4 thank you for sorted list object keys!

# -- тут мы использовали функцию sorted() для сортировки ключей в объекте


# --- перебор всех ЗНАЧЕНИЙ в словаре

for valueIbject in propertyObject.values():
    print(valueIbject + " it's value object")

# Car it's value object
# Train it's value object
# Boat it's value object
# Bike it's value object

repeatPropertes = {
    "1" :  "Flash",
    "2" :  "Superman",
    "3" :  "Spiderman",
    "4" :  "wonderwoman",
    "5" :  "Blackcat",
    "6" :  "Flash",
    "7" :  "Wolwerine",
    "8" :  "Superman",
    "9" :  "Catwoman",
    "10":  "Superman"
}

for nameSuperHeros in set(repeatPropertes.values()):
    print(nameSuperHeros)

# когда в словаре или списке много или есть дупликаты, они убираются путем отсева с помощью set() 


#---- Список словарей

alien_1 = {
    "color" :   "black",
    "speed" :   "200km\h",
    "energy":   "50"
}
alien_2 = {
    "color" :   "red",
    "speed" :   "120km\h",
    "energy":   "10"
}
alien_3 = {
    "color" :   "blue",
    "speed" :   "650km\h",
    "energy":   "90"
}
alien_4 = {
    "color" :   "purple",
    "speed" :   "700km\h",
    "energy":   "332"
}

list_aliens = [alien_1, alien_2, alien_3, alien_4]

for unit in list_aliens:
    for valueUnit in unit.values():
        print(valueUnit)

#--- Список в Словаре

pizza = {
    "cheese" : "macarela",
    "salat"  : "iceberg",
    "pepper" : "red",
    "toppings": ["mushrooms", "extra cheese", "solt", "meat"]
}

for items in pizza['toppings']:
    print("\t" + items)
        # mushrooms
        # extra cheese
        # solt
        # meat

superCars = {
    "germany" : ["BMW", "Mercedes", "Wolsvagen"],
    "USA"   : ["Ford", "Dodge"],
    "France" : ["Citroen", "Reno"],
    "Italia" : ["Buggati", "Lambordginy"]
}

for countryName, carName in superCars.items():
    print("\n" + countryName.title() + " country who makes cars")
    for itemCar in carName:
        print("\t" + itemCar.title())
# Germany country who makes cars
#         Bmw
#         Mercedes
#         Wolsvagen

# Usa country who makes cars
#         Ford
#         Dodge

# France country who makes cars
#         Citroen
#         Reno

# Italia country who makes cars
#         Buggati
#         Lambordginy



#---- Словарь в словаре 

students = {
    "Jordan" : {
        "firstName" : "Jordan",
        "lastName"  : "Morgan",
        "location"  : "New-Jercy",
        "age"   : 25
    },
    "Shon" : {
        "firstName" : "Shon",
        "lastName"  : "Andersson",
        "location"  : "New-York",
        "age"   : 12
    },
    "Bill" : {
        "firstName" : "Bill",
        "lastName"  : "Shewanian",
        "location"  : "Detroit",
        "age"   : 30
    },
    "Mayble" : {
        "firstName" : "Mayble",
        "lastName"  : "Pience",
        "location"  : "Gravity-Falls",
        "age"   : 13
    },
    "Deeper" : {
        "firstName" : "Deeper",
        "lastName"  : "Pience",
        "location"  : "Gravity-Falls",
        "age"   : 14
    }
}

#--- сделаем перебор значений у словарей в словаре

for userName, userInfo in students.items(): # перебрали свойства Главного словаря
    print("\n" + "informantion about student " + str(userName)) # вывели ключи главного словаря
    for information in userInfo.values(): # в этом цикле прошлись по всем Значениям подСловаря и вывели их
        print("\t" + str(information))
        
# informantion about student Jordan     
#         Jordan                        
#         Morgan                        
#         New-Jercy                     
#         25                            
                                      
# informantion about student Shon       
#         Shon                          
#         Andersson                     
#         New-York                      
#         12                            
                                      
# informantion about student Bill       
#         Bill                          
#         Shewanian                     
#         Detroit                       
#         30                            
                                      
# informantion about student Mayble     
#         Mayble                        
#         Pience                        
#         Gravity-Falls                 
#         13                            
                                      
# informantion about student Deeper     
#         Deeper                        
#         Pience                        
#         Gravity-Falls                 
#         14                            