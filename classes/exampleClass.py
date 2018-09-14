class Table():
    def __init__(self, width, height, lenght):
        self.width = width
        self.height = height
        self.lenght = lenght
        """ задаем родительский класс Стол, делаем в нем параметры которые в дальнейшем будет передавать в классы Детей """


class Desk_Table(Table): # унаследуем параметры у класса Table
    def sqaure(self):
        sqaureTable = self.width * self.height # узнаем площадь стола
        diagonal = sqaureTable / self.lenght # узнаем диагональ стола
        return "Sqaure table is " + str(sqaureTable) + " sm and diagonal table " + str(diagonal)

class Kitchen_Table(Desk_Table):
    def setPlaces(self, places):
        self.places = places 
    def getPlaces(self):
        width_lenght = self.lenght * self.width 
        if width_lenght > 3400:
            print("all places " + str(self.places))
        else:
            print("places less them 4")




my_table = Desk_Table(70, 50, 140)
print(my_table.sqaure())
new_table = Kitchen_Table(40, 25, 70)
new_table.getPlaces()



#-------------- Создадим новый класс и потомка 


class Head():
    def __init__(self, eyes, nose, mouth, hair, ears):
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth
        self.hair = hair
        self.ears = ears
    def touchHairs(self):
        print("Touch my " + self.hair + " hairs")
    def sayMouth(self):
        print("talk your " + self.mouth + " mouth")

class Ears(Head):
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.lenght = length
        self.color = "pink"
        """ инициализируем атрибуты уха человека """
    super().__init__(eyes, nose, mouth, hair, ears)
    def describeEars(self):
        super().__init__(eyes, nose, mouth, hair, ears)
        print("My ears vary small, he color is " + self.color + " height my ear " + str(self.height) + " sm" + self.nose + self.mouth)

your_head = Head("blue", "small", "wide", "brown", "big")
your_head.touchHairs()
your_head.sayMouth()

my_ears = Ears("blue", "small", "wide", "brown", "big", 10, 2, 15)
my_ears.describeEars()
    



