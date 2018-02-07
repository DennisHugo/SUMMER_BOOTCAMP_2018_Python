count = 0

while True:
    print(count)
    count += 2
    if count == 5:   #NUNCA PARARA DEBIDO A QUE NO HABRA 5 JAMAS!!!
        break

zoo = [" ","lion", 'tiger', 'elephant']
while True:
    animal = zoo.pop()
    print(animal)
    if animal is ' ':
        break
