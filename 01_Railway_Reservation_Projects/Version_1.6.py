from random import randint
from random import choice
class railin:
    def __init__(self):
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
        lst = ["Amrawati" , "Itanagar" , "Dispur" , "Patna" , "Raipur" , "Panaji" , "Gandhinagar" , "Chandigarh" , "Delhi" , 
                "Shimla" , "Ranchi" , "Bengaluru" , "Thiruvanathapuram" , " Bhopal" , "Mumbai" , " Imphal" , " Shillong" , "Aizawl" , "Kohima" ,
            "Bhubaneswar" , "Jaipur" , "Gangtok" , "Chennai" , "Hyderabad" , "Agartala" , "Lucknow" , "Dehradun" , "Kolkata"]
        print(lst)
        self.Board = input("Enter your Boarding Station: ")
        self.Desti = input("Enter your Destination Station: ")

    def get_region(self , city):

        captl = ["Delhi"]
        north = ["Shimla" , "Chandigarh" , "Dehradun" ,  "Lucknow" ]
        south = ["Amrawati" , "Bengaluru" , "Thiruvananthapuram" , "Chennai" , "Hyderabad" , "Panaji" ]
        west = ["Mumbai" , "Gandhinagar" , "Jaipur" ]
        central = ["Bhopal" , "Raipur" ]
        east = ["Patna" , "Ranchi" , "Bhubaneswar" , "Kolkata" , "Dispur" , "Itanagar" , "Shillong" ,
                        "Aizawl" , "Kohima" , "Agartala" , "Imphal" , "Gangtok"]

        if city in north:
            return "north"
        elif city in south:
            return "south"
        elif city in east:
            return "east"
        elif city in west:
            return "west"
        elif city in central:
            return "central"
        elif city in captl:
            return "capital"
    

    def get_train(self):
        trains = {
            ("capital", "north"): ("Rajdhani Express", 12059),
            ("capital", "south"): ("Rajdhani Express", 12059),
            ("capital", "east"): ("Rajdhani Express", 12059),
            ("capital", "west"): ("Rajdhani Express", 12059),
            ("capital", "central"): ("Rajdhani Express", 12059),
            ("north", "south"): ("North-South Express", 80251),
            ("south", "north"): ("South-North Express", 80252),

            ("north", "east"): ("North-East Express", 20159),
            ("east", "north"): ("East-North Express", 20160),

            ("north", "west"): ("North-West Express", 42013),
            ("west", "north"): ("West-North Express", 42014),

            ("north", "central"): ("North-Central Express", 55021),
            ("central", "north"): ("Central-North Express", 55022),

            ("north", "north"): ("North-Intercity Express", 10015),

            ("south", "central"): ("South-Central Express", 59021),
            ("central", "south"): ("Central-South Express", 59022),

            ("south", "west"): ("South-West Express", 56042),
            ("west", "south"): ("West-South Express", 56041),

            ("south", "east"): ("South-East Express", 89026),
            ("east", "south"): ("East-South Express", 89025),

            ("south", "south"): ("South-Intercity Express", 88099),

            ("west", "central"): ("West-Central Express", 54041),
            ("central", "west"): ("Central-West Express", 54042),

            ("west", "west"): ("West-Intercity Express", 56064),

            ("central", "central"): ("Central-Intercity Express", 42014),

            ("east", "central"): ("East-Central Express", 22055),
            ("central", "east"): ("Central-East Express", 22056),

            ("east", "west"): ("East-West Express", 21004),
            ("west", "east"): ("West-East Express", 21005),

            ("east", "east"): ("East-Intercity Express", 22022)
        }
        board_region = self.get_region(self.Board)
        dest_region = self.get_region(self.Desti)

        train_name, train_no = trains[(board_region, dest_region)]

        print(
            f"Your Train is: {train_name} "
            f"and Train Number: {train_no}"
        )

    def Booking(self):
        hour = randint(0, 23)
        minute = randint(0, 59)
        self.c = (f"{hour:02d}:{minute:02d}")
        print(self.c)
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
                print(f"You are going from {self.Board} to {self.Desti}")
                for passenger in self.passengers:
                    print(f"Your seat Number is {self.cmp},{passenger["seat"]}")
            else:
                print("Please enter correct PNR no. ")
        else:
            print("No Information found")

    def Getinfo(self):
        if (self.remain, True):
            print(f"Passenger Name and age are: {self.passengers}")
            print(f"Boarding Station: {self.Board}, Destination Station: {self.Desti}, Timing: {self.c}, PNR no. : {self.y}")
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
                print(f"You are going from {self.Board} to {self.Desti}")
            elif X == "ABC":
                print(f"Timing of your train is: {self.c}\nAnd you are going from {self.Board} to {self.Desti}")
                for passenger in self.passengers:
                    print(f"Your seat Number is {self.cmp},{passenger["seat"]}")
            else:
                print("Pick a correct option")
        else:
            print("No Information found")
                
    def save_booking(self):
        with open("Filename.txt", "a") as f:
            f.write(f"\nPNR: {self.y}\n")
            f.write(f"Boarding: {self.Board}\n")
            f.write(f"Destination: {self.Desti}\n")
            for passenger in self.passengers:
                f.write(
                    f"{passenger['name']} "
                    f"{passenger['age']} "
                    f"{self.cmp},{passenger['seat']:02d}\n"
                    f"{self.c}\n"
                )

def getrun():
    obj = railin()
    if getattr(obj, "allowed" , False):
        obj.get_train()
        obj.Booking()
        obj.save_booking()
        obj.PNRChecking()
        obj.Getinfo() # Getting the information
        obj.Checking() # Checking Information

getrun()
