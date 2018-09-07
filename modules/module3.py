def makeRedColor(car):
    print (str(car + ' have red color') )


def informationAboutCar():
    
    while True:
        markCar = input("mark is your's car ")
        maxSpeed = input("max speed your car ")
        colorCar = input("color is your car ")
        question = input("Do you want end? ")
        if question == "yes":
            break
    objectCar = {
        1 : markCar,
        2 : maxSpeed,
        3 : colorCar
    }
    for items in objectCar.items():
        print(items)
    return objectCar




