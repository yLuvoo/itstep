
# class Student:
#     print("Hi!")
#     def __init__(self):
#         self.height = 160
#         print("I am alive!")
#
# first_student = Student()
#
# class Student:
#     def __init__(self, height = 160):
#         self.height = height
#
# nick = Student()
# kate = Student(height=170)
# kiril = Student(height=2033)
# print(nick.height)
# print(kate.height)
# print(kiril.height)

# class Student:
#     amount_of_students = 0
#
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#
# nick = Student()
# kate = Student(height=170)
# chiri = Student()
# print(nick.amount_of_students)
# print(Student.amount_of_students)
# print(kate.height)

# class Student():
#     height= 160
#     def __init__(self):
#         print(self.height)
#         self.height = 160
#
# nick = Student()
# kate = Student()

# class Student():
#     def __init__(self):
#         self.height = 170
#     height = 160
#
#     def printer(self):
#         print(self.height)

# x = 10
# class Locker:
#     print(x)
#     def func_1(self):
#         # x = 20
#         print(x)
#         def func_2():
#             # x = 30
#             print(x)
#         func_2()
# some_object = Locker()
# some_object.func_1()

# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
#
# nick = Student()
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)
# print(Student.amount_of_students)
# jora = Student()
# print(Student.amount_of_students)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         return f"I am a student. My name is {self.name}."
#
# nick = Student(name = "Nick")
# print(nick)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         if self.name:
#             return f"I am a student. My name is {self.name}."
#         else:
#             return f"I am a student. I dont have a name"
# alice = Student(name="Alice")
# print(alice)
# unknown_student = Student()
# print(unknown_student)

# import random
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self):
#         print("Este timpul sa invat")
#         self.progress += 0.12
#         self.gladness -= 5
#
#     def to_sleep(self):
#         print("Voi dormi")
#         self.gladness += 3
#     def to_chill(self):
#         print("Timp de odihna")
#         self.gladness += 5
#         self.progress -= 0.1
#     def is_alive(self):
#         if self.progress < - 0.5:
#             print("DEAD..")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depresie.....")
#             self.alive = False
#         elif self.progress > 5:
#             print("O murit de fericire")
#             self.alive = False
#
#     def end_of_day(self):
#         print(f"Fericire = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
#
#     def live(self, day):
#         day = " Ziua " + str(day) + " din viata lui " + self.name + " "
#         print(f"{day:=^50}")
#         live_cube = random.randint(1,3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
# nick = Student(name="Vlad")
# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)

# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, human):
#         self.passengers.append(human)
#
#     def print_passengers_names(self):
#         if self.passengers!= []:
#             print(f"In {self.brand} there are this passengers")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
# nick = Human("Nick")
# kate = Human("Kate")
# car = Auto("Mercedes")
# car.add_passenger(nick)
# car.add_passenger(kate)
# car.print_passengers_names()

import random
# Define the House class
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
# Define the Auto class
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    # Method to simulate driving the car
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False
# Define the Job class
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]
# Define the Human class
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
    # Method to get a home
    def get_home(self):
        self.home = House()
    # Method to get a car
    def get_car(self):
        self.car = Auto(brands_of_car)
    # Method to get a job
    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()
            return
    # Method for eating
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
    # Method for working
    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()
            return
    # Method for shopping
    def shopping(self, manage):
        if self.car.drive():
            if manage == "fuel":
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                self.money -= 50
                self.home.food += 50
            elif manage == "delicacies":
                self.gladness += 10
                self.satiety += 2
                self.money -= 15
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
            return
    # Method for chilling
    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    # Method for cleaning home
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    # Method for repairing the car
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    # Method to display character's indicators and state
    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")
    # Method to check if character is alive
    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
        return True
    # Method to simulate character's daily life
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)  # Move dice initialization here
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")
        return True  # Return True to indicate character is alive


# Define the list of job opportunities
job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

# Define the list of car brands with their characteristics
brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

# Create a Human object
nick = Human(name="Nick")

# Simulate one week of Nick's life
for day in range(1, 8):
    print(f"Day {day}")
    if not nick.live(day):
        break
