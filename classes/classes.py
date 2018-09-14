class Dog():
    """ простая модель собаки """
    # создадим функцию внутри класса

    def __init__(self, name, age):
        """ Инициализиурет атрибуты name и age """
        self.name = name
        self.age = age
    def sit(self):
        """ Собака садится по команде """
        print(self.name.title() + " is now siting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


    
"""
 метода __init__(self, param1, param2) обязательный параметр в классе
 параметр self обязателен в определении метода, self - это ссылка
 на экземпляр
"""

my_dog = Dog("While", 6)
print("My dog name is " + my_dog.name.title())
print("age my dog is "  + str(my_dog.age))


your_dog = Dog("Boby", 10)
print("name your dog is " + your_dog.name.title() + " end her age " + str(your_dog.age))

your_dog.sit() # вызвали метод из класса, теперь собака по имени Boby сидит
your_dog.roll_over()


class Restaurant():
    def __init__(self, Restaurant_name):
        self.Restaurant_name = Restaurant_name
    def open_restaurant(self):
        print("Restaurant " + self.Restaurant_name + " is open!")

go_restaurant = Restaurant("Red Omar")
go_restaurant.open_restaurant()

some_restaurant = Restaurant("Burger King")
some_restaurant.open_restaurant()



class User():
    def __init__(self, firstName, lastName, color_eye, location_user):
        self.firstName = firstName
        self.lastName = lastName
        self.color_eye = color_eye
        self.location_user = location_user
    def describe_user(self):
        print("First name user is " + self.firstName + " last name user is " + self.lastName + ", he live in " + self.location_user + " end her yey is " + self.color_eye)
    def greet_user(self):
        print("Hello " + self.firstName + " " + self.lastName)


firstUser = User("Shon", "Fisher", "brown", "Moscow")
firstUser.describe_user()
firstUser.greet_user()
    




class Car():
    """ Модель авто """
    def __init__(self, make, model, year):
        """ атрибутьы авто """
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 # начальное значение одометра равно 0
    def get_name(self):
        """ Возвращает аккуратно отформатированное описание """
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    def read_odometr(self):
        """ чтение показателя одоментра """
        print("This car has " + str(self.odometer) + " miles on it") # выводим значение одометра
    def update_odometr(self, update):
        """ параметр update будет указывать заданую велечину одометра при вызове метода """
        self.odometer = update # проверяем значение одометра и выводим значение если туда что то передали
    def incriment_odometr(self, miles):
        """ Увеличивает показания одометра с заданным приращением """
        self.odometer += miles # добавляем к одометру + то значение что есть в аргументе

my_new_car = Car("Audi", "a4", 2017)
print(my_new_car.get_name())

my_new_car.update_odometr(300)
my_new_car.read_odometr()

my_new_car.incriment_odometr(450)
my_new_car.read_odometr()



""" Создание потомка класса Car, с именем ElectricCar() """

class ElectricCar(Car): # тут передаем Имя РОДИТЕЛЯ что бы связать контекст родителя и ребенка классов

    def __init__(self, make, model, year):
       """ инициализируем атрибуты класса-родителя """
       super().__init__(make, model, year)


my_tesla = ElectricCar("Tesla", "model s", 2018)
print(my_tesla.get_name())



class CoffeMachine():
    def __init__(self, liters, temperature, grain, volume, name):
        self.liters = liters
        self.temperature = temperature
        self.grain = grain
        self.name = name
        self.volume = volume
    def getCupCoffe(self):
        cup = "Add " + self.volume + " volume, " + " and add some you'r like grain coffe in coffemachine \t" + str(self.grain) + " gram, " + " and warm up the water until \t" + self.temperature
        return cup
    def drinkCoffe(self):
        print("You'r coffe complited! Enjoy  testy " + str(self.name))


testy_coffe = CoffeMachine(0.5, "80t", 30, "20", "arabica")
print(testy_coffe.getCupCoffe())
testy_coffe.drinkCoffe()



class makeAmericano(CoffeMachine):
    def getAmericano(self, sugar):
        self.sugar = sugar
        print("add some sugar " + self.sugar)

americano = makeAmericano(0.90, "40t", 2, "60", "americano")
print(americano.getCupCoffe())
americano.getAmericano("2 spons")


