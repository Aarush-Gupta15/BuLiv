class Vehicle:
    wheels=0
 
    def __init__(self, wheels ):
        self.wheels=wheels

    def run(self):
        print("veficle is running" , end='')


bike = Vehicle(2)
bike.run()
print(" on ", bike.wheels)


car = Vehicle(4)
car.run()
print(" on ", car.wheels)

    