# You are developing a simple application to manage different types of vehicles. Define a base class Vehicle with methods start() and stop(). Implement two subclasses, Car and Motorcycle, each overriding the start() and stop() methods. Additionally, create a function drive(vehicle) that takes an instance of Vehicle and calls its methods.


class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


class Car:
    def start(self):  # override start method
        print("Car started")

    def stop(self):  # override stop method
        print("Car stopped")


class MotorCycle:
    def start(self):
        print("MotorCycle started")

    def stop(self):
        print("MotorCycle stopped")


def drive(Vehicle):  # takes Vehicle class' instance
    Vehicle.start()
    Vehicle.stop()


car = Car()
motor_cycle = MotorCycle()

drive(car)
drive(motor_cycle)
