from module3 import makeRedColor, informationAboutCar
# from module2 import sayHello as sayHello не сработает ИМПОРТ в силу того что модуль вызван в другом месте
makeRedColor("Ford")
informationAboutCar()
def makeLongWordAndAddMoreSome():
    name_man = {
        "1" : "Billy",
        "2" : "Mishone",
        "3" : "Colins",
        "4" : "Dammy"
    }

    array_second_name = ["Milson", "Anderson", "Fisher", "Terobbol"]

    for value in name_man.values():
        for secondName in array_second_name:
            empFirstName = []
            empFirstName.append(value)
            for second in empFirstName:
                print(second + " " + secondName)


"""
    заметка на будущее:
    Нельзя импортировать модуль в тот модуль. который уже вызван в другом модуле
    пример - модульА был вызван в модулеБ, и модульБ нельзя вызвать в модулеА
    возникает ошибка - AttributeError: module 'модуальА' has no attribute 'nameSomeFunction'
"""





