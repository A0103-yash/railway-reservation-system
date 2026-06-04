from random import randint

class railin:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.y = None
        self.passengers = []
        self.count = int(input("Enter how many passengers are travelling: "))
        for i in range(self.count):
            name = input(f"Enter {i+1} passenger name: ")
            age = int(input(f"Enter {i+1} passengers age: "))
            self.passengers.append({
                "name" : name,
                "age" : age
            })
            if i == 0:  # Only first passenger
                if age < 18:
                    print("You are not allowed to book tickets as you are minor")
                else:
                    print ("You are Allowed to book Tickets")
    def Booking(self):
        self.a = input("Enter the boarding station: ")
        self.b = input("Enter the destination station: ")
        hour = randint(0, 23)
        minute = randint(0, 59)
        self.c = (f"{hour:02d}:{minute:02d}")
        print(self.c)
        x = (randint(12345, 54321))
        print(f"Your Train number is {x}")
        for i in range(self.count):
            seat = (randint(1,85))
            self.seat = (f"{seat:02d}")
            print(f"Seat number of {i+1} passenger is {self.seat}")
        self.y = (randint(123456789,999999999))
        print(f"Your PNR no. is {self.y}")
    def PNRChecking(self):
        PNR = int(input("Enter Your PNR No. : "))
        if PNR == self.y:
            print(self.passengers)
            print(f"Timing of your train is: {self.c}\nYour seat Number is {self.seat}\nAnd you are going from {self.a} to {self.b}")
        else:
            print("Please enter correct PNR no. ")
    def Getinfo(self):
        print(f"Passenger Name and age are: {self.passengers}")
        print(f"Boarding Station: {self.a}, Destination Station: {self.b}, Timing: {self.c}, PNR no. : {self.y}")
    def Checking(self):
        print("What do you want to check\nA = Timing of train\nB = Your seat number\nC = From where to where")
        X = input("")
        if X == "A":
            print(f"The timing of your train is {self.c}")
        elif X == "B":
            print(self.seat)
        elif X == "C":
            print(f"You are going from {self.a} to {self.b}")
        elif X == "ABC":
            print(f"Timing of your train is: {self.c}\n{self.seat}\nAnd you are going from {self.a} to {self.b}")
        else:
            print("Pick a correct option")

obj = railin()
obj.Booking()
obj.PNRChecking()
obj.Getinfo() # Getting the information
obj.Checking() # Checking Information

