from random import randint

class railin:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.m = input("Enter your name here: ")
        self.n = int(input("Enter your age here: "))
        if (self.n <= 12) :
            print("You are not eligible to book ticket. ")
        elif (self.n > 13 and self.n < 100) :
            print(f"Your age is {self.n}")
        else:
            print("Please enter a valid age...")
    def Booking(self):
        self.a = input("Enter the boarding station: ")
        self.b = input("Enter the destination station: ")
        hour = randint(0, 23)
        minute = randint(0, 59)
        self.c = (f"{hour:02d}:{minute:02d}")
        print(self.c)
        x = (randint(12345, 54321))
        print(f"Your Train number is {x}")
    def Checking(self):
        print("What do you want to check\nA = Timing of train\nB = Your seat number\nC = From where to where")
        X = input("")
        if X == "A":
            print(f"The timing of your train is {self.c}")
        elif X == "B":
            print("Seat number information is not available.")
        elif X == "C":
            print(f"You are going from {self.a} to {self.b}")
        elif X == "ABC":
            print(f"Timing of your train is: {self.c}\nYour seat Number is not shown yet\nAnd you are going from {self.a} to {self.b}")
        else:
            print("Pick a correct option")
    def Getinfo(self):
        print(f"Passenger Name: {self.m}\n Passenger Age: {self.n}")
        print(f"Boarding Station: {self.a}, Destination Station: {self.b}, Timing: {self.c}")

obj = railin()
obj.Booking()
obj.Getinfo() # Getting the information
obj.Checking() # Checking Information

