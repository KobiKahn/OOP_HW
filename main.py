import math
import random
# 1

p1 = False
if p1:
    class Rocket():
        def __init__(self,  x = 0, y = 0, x_end = 25, y_end = 35, crew_size = 0, captain = 'NONE', height = 25, speed = 20000000000000):
            self.crew_size = crew_size
            self.captain = captain
            self.height = height
            self.speed = speed
            self.x_end = x_end
            self.y_end = y_end
            self.x = x
            self.y = y
        def move_rocket(self):
            self.x += self.x_end
            self.y += self.y_end
            print(self.x, self.y)
            return (self.x, self.y)

        def get_dist(self, other_rocket):

            self.distance = math.sqrt((self.x - other_rocket.x)**2+(self.y - other_rocket.y)**2)
            print(self.distance)
            if self.distance >= 20:
                print('You are all safe')
            elif self.distance > 0 and self.distance < 20:
                print('TOO CLOSE BACK OFF')
            else:
                print('CRASHHHHH')

        def attributes(self):
            print(f'Crew_size: {self.crew_size}\nCaptain: {self.captain}\nHeight: {self.height}m\nSpeed: {self.speed}lightyears/sec')

        def launch(self):
            if self.captain != 'NONE':
                print(f'{self.captain} has TAKEN OFF')
            else:
                print('TAKEOFF')

        def land_rocket(self):
            print(self.x, self.y)
            self.x, self.y = 0, 0
            print(self.x, self.y)







    rocket1 = Rocket()
    rocket2 = Rocket(20, 30, 40, 20, 30, 'JOJO', 30, 2)
    rocket3 = Rocket(60, 40, 15, 25, 20, 'BOB', 20, 3)
    rocket4 = Rocket(100, 80, -35, -30, 30, 'JOHN', 50, 3.5)
    # rocket_fleet = [rocket1, rocket2, rocket3, rocket4]

    # rocket1.move_rocket()
    # rocket2.move_rocket()
    # rocket3.move_rocket()
    # rocket4.move_rocket()
    #
    # rocket1.get_dist(rocket2)
    # rocket1.get_dist(rocket4)
    # rocket2.get_dist(rocket3)
    # rocket4.get_dist(rocket3)

    # rocket1.attributes()
    # rocket2.attributes()
    # rocket3.attributes()
    # rocket4.attributes()

    # rocket1.launch()
    # rocket2.launch()
    #
    # rocket3.land_rocket()
    # rocket4.land_rocket()

# 2
p2 = False
if p2:
    class Person():
        def __init__(self, name, age, height, place_birth):
            self.name = name
            self.age = age
            self.height = height
            self.place_birth = place_birth

        def introduction(self):
            if self.height >= 6:
                print(f'Hi my name is {self.name} and I am very tall')
            else:
                print(f'Hi my name is {self.name} and I am {self.age}')

        def older(self):
            self.age += 1
            print(self.age)

        def place_of_birth(self):
            print(f'I was born in {self.place_birth} {self.age} years ago')

    person1 = Person('Kobi', 16, 6.7, 'Maine')

    person1.introduction()
    person1.older()
    person1.place_of_birth()

#3
p3 = True
if p3:
    


