from random import randint
from random import choice

class railin:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.y = None
        self.Board = None
        self.Desti = None
        self.passengers = []
        self.count = int(input("Enter how many passengers are travelling: "))
        for i in range(self.count):
            name = input(f"Enter {i+1} passenger name: ")
            age = int(input(f"Enter {i+1} passengers age: "))
            self.passengers.append({
                "name" : name,
                "age" : age,
                "seat" : None
            })
            if i == 0:  # Only first passenger
                if age > 18:
                    print ("You are Allowed to book Tickets")
                    self.allowed = True
                else:
                    print("You are not allowed to book tickets")
                    self.allowed = False
                    return
                
    def Booking(self):
        self.a = input("Enter the boarding station: ")
        self.b = input("Enter the destination station: ")
        hour = randint(0, 23)
        minute = randint(0, 59)
        self.c = (f"{hour:02d}:{minute:02d}")
        print(self.c)
        x = (randint(12345, 54321))
        print(f"Your Train number is {x}")
        Comp = ["C1" , "C2" , "C3" ,
                "D1" , "D2" , "D3" , "D4" ,
                "D5" , "D6" , "D7" , "D8" , 
                "D9" , "D10" , "D11" , "D12" ,
                "D13" , "D14" , "D15" , "D16" , "D17"]
        # As C and D categories contains 85 seats each coach
        coach = (choice(Comp))
        self.cmp = (coach)
        ttlseatsf = (randint(250,1700))
        ttlseatsr = (1700 - ttlseatsf)
        print(f"Total remaining seats are {ttlseatsr}")
        if ttlseatsr > self.count:
            for passenger in self.passengers:
                passenger["seat"] = randint(1,85)
                print(
                    f"Seat number and compartment of "
                    f"{passenger['name']} is "
                    f"{self.cmp},{passenger['seat']:02d}"
                )
            self.y = (randint(123456789,999999999))
            print(f"Your PNR no. is {self.y}")
            self.remain = True
        else:
            print("There are no Seats left")
            self.remain = False

    def PNRChecking(self):
        PNR = int(input("Enter Your PNR No. : "))
        if (self.remain , True):
            if PNR == self.y:
                print(self.passengers)
                print(f"Timing of your train is: {self.c}")
                print(f"You are going from {self.a} to {self.b}")
                for passenger in self.passengers:
                    print(f"Your seat Number is {self.cmp},{passenger["seat"]}")
            else:
                print("Please enter correct PNR no. ")
        else:
            print("No Information found")

    def Getinfo(self):
        if (self.remain, True):
            print(f"Passenger Name and age are: {self.passengers}")
            print(f"Boarding Station: {self.a}, Destination Station: {self.b}, Timing: {self.c}, PNR no. : {self.y}")
            for passenger in self.passengers:
                print(f"Your seat Number is {self.cmp},{passenger["seat"]}")
        else:
            print("NO Information found")

    def Checking(self):
        if (self.remain, True):
            print("What do you want to check\nA = Timing of train\nB = Your seat number\nC = From where to where")
            X = input("")
            if X == "A":
                print(f"The timing of your train is {self.c}")
            elif X == "B":
                for passenger in self.passengers:
                    print(f"Your seat Number is {self.cmp},{passenger["seat"]}")
            elif X == "C":
                print(f"You are going from {self.a} to {self.b}")
            elif X == "ABC":
                print(f"Timing of your train is: {self.c}\nAnd you are going from {self.a} to {self.b}")
                for passenger in self.passengers:
                    print(f"Your seat Number is {self.cmp},{passenger["seat"]}")
            else:
                print("Pick a correct option")
        else:
            print("No Information found")
                
obj = railin()
if getattr(obj, "allowed" , False):
    obj.Booking()
    obj.PNRChecking()
    obj.Getinfo() # Getting the information
    obj.Checking() # Checking Information

