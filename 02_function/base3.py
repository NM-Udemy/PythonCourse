# グローバル変数

def printAnimal():
    global animal
    animal = 'Cat'
    print('関数内animal = {}, id = {}'.format(animal, id(animal)))

# animal = 'Dog'
printAnimal()
print('関数外animal = {}, id = {}'.format(animal, id(animal)))