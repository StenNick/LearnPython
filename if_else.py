#---------- if, else

cars = ["bmw", "audi", "subaru", "solswagen", "lada", "mercedes", "skoda"]
for item in cars:
    if item == "audi":
        print(item.upper(), ' make upper')
    else:
        print(item.title())



#---- проверка вхождения значений в список с помощью оператора - in

colors = ['red', 'blue', 'white', 'black', 'purple']
def checkColor():
    if 'red' in colors:
        print("Yes, it's true!")
    else:
        print("No")

checkColor()

#--- убедимся что значения в списке отсутствуют

numbers = [10, 546, 100, 230, 540]

def checkNumbers():
    if 888 not in numbers:
        print("888 hot have in list")
    else:
        print("888 have in list...")

checkNumbers()



#--- if elif 

age = 12

if age < 4:
    print("Your age more them is 4")
elif age < 18:
    print("Your age less them is 18")

else:
    print("good bye")



topping = ["mushrooms", "tobasco", "green papers", "cheese", "red peppers", "sauce","chicken"]
pizza = ["meat", "greenery", "tobasco", "chicken"]

for ingredients in pizza:
    if ingredients in topping:
        print("adding " + ingredients + ".")
    else:
        print("Sorry")




names = ["Franco", "Georgy", "Mikle", "Admin"]
for items in names:
    if items == "Admin":
        print("Hello Admin! Would you like to see a status report?")
    elif items != "Admin":
        print("Weclome " + items + " how are you?")
    else:
        print("Sorry, invalid password")

Weclome Franco how are you?
Weclome Georgy how are you?
Weclome Mikle how are you?
Hello Admin! Would you like to see a status report?


current_users = ["Franco", "Georgy", "Mikle", "John", "Bob"]
new_users = ["Nick", "Julia", "Mikle", "Mayble", "Jesica", "John"]
