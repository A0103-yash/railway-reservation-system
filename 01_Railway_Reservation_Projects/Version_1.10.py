# Making an Railway Reservation System in Python

from random import randint
from random import choice

class Createaccount():
    def __init__(self):
        self.s = input('''Hey Welcome to Booking Centre
Do You have an account
If not Enter NA for new account
If you have then OA here: ''')
        if self.s == "NA":
            self.New_Account()
            self.User_Login()
        else:
            self.User_Login()
        if self.Login:
            print("Thank You for Choosing Us")

    def New_Account(self):
        self.name = input("Enter your name here: ")
        self.DOB = input(f"Write in the form DDMMYYYY\nEnter your Birth date here: ")
        self.email = input("Enter your email here: ")
        self.password = input("Enter your password here: ")
        self.User_Id = (randint(12345,55555))
        print(f"Your User_Id is {self.User_Id}")
        
        self.save_info()

    def save_info(self):
        with open ("Personal_Detail.txt" , "a") as f:
            f.write(f"Your name is {self.name}\n")
            f.write(f"Your Date of Birth is {self.DOB}\n")
            f.write(f"Your Email Id is {self.email}\n")
            f.write(f"Your User_id is: {self.User_Id}\n")
            f.write(f"Your Password is: {self.password}\n")
        return

    def User_Login(self):
        user_id = input("Enter your User ID here: ")
        with open ("Personal_Detail.txt" , "r") as f :
            data = f.read()
            if user_id in data:
                password = input("Enter your password here: ")
                if password in data:
                    print("Login successful")
                    self.Login = True
                    self.Menu()
                else:
                    print("Incorrect password")
                    self.Login = False
                    return
            else:
                print("User Not found")

    def Menu(self):
        print("Hey , Should we help you in your Journey...!")
        B = "To new booking enter B"
        C = "To check your details enter C"
        X = "To Cancel ticket enter X"
        print(B)
        print(C)
        print(X)
        userinput = input("Enter here: ")
        if userinput == "B" :
            class railin():
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
                            "Shimla" , "Ranchi" , "Bengaluru" , "Thiruvananthapuram" , "Bhopal" , "Mumbai" , "Imphal" , "Shillong" , "Aizawl" , "Kohima" ,
                        "Bhubaneswar" , "Jaipur" , "Gangtok" , "Chennai" , "Hyderabad" , "Agartala" , "Lucknow" , "Dehradun" , "Kolkata"]
                    print(lst)
                    self.Board = input("Enter your Boarding Station: ")
                    self.Desti = input("Enter your Destination Station: ")

                def get_region(self , city):

                    self.captl = ["Delhi"]
                    self.north = ["Shimla" , "Chandigarh" , "Dehradun" ,  "Lucknow" ]
                    self.south = ["Amrawati" , "Bengaluru" , "Thiruvananthapuram" , "Chennai" , "Hyderabad" , "Panaji" ]
                    self.west = ["Mumbai" , "Gandhinagar" , "Jaipur" ]
                    self.central = ["Bhopal" , "Raipur" ]
                    self.east = ["Patna" , "Ranchi" , "Bhubaneswar" , "Kolkata" , "Dispur" , "Itanagar" , "Shillong" ,
                                    "Aizawl" , "Kohima" , "Agartala" , "Imphal" , "Gangtok"]

                    if city in self.north:
                        return "north"
                    elif city in self.south:
                        return "south"
                    elif city in self.east:
                        return "east"
                    elif city in self.west:
                        return "west"
                    elif city in self.central:
                        return "central"
                    elif city in self.captl:
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

                    self.train_name, self.train_no = trains[(board_region, dest_region)]

                    print(
                        f"Your Train is: {self.train_name} "
                        f"and Train Number: {self.train_no}"
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
                    ttlseatsf = (randint(1500,1700)) # If you want to check the working of waiting list then change the range to (1699, 1700)
                    ttlseatsr = (1700 - ttlseatsf)
                    print(f"Total remaining seats are {ttlseatsr}")
                    if self.count < ttlseatsr :
                        for passenger in self.passengers:
                            passenger["seat"] = randint(1,85)
                            print(
                                f"Seat number and compartment of "
                                f"{passenger['name']} is "
                                f"{self.cmp},{passenger['seat']:02d}"
                            )
                        self.remain = True
                    elif self.count >= ttlseatsr:
                        for passenger in self.passengers:
                            passenger["waiting.seat"] = f"(WL {randint(1,85)})"
                            print(
                                f"Their is no seat available "
                                f"{passenger['name']} has "
                                f"{passenger["waiting.seat"]} in waiting list"
                            )
                        self.remain = False
                    self.y = (randint(123456789,999999999))
                    print(f"Your PNR no. is {self.y}")

                def pricing(self):
                    print("Your Ticket price is 600 per person")
                    self.f =  "Your Total Ticket fare is: " , int(600*self.count)
                    print(self.f)
                def save_booking(self):
                    with open("Details.txt", "a") as f:
                        f.write(f"\nPNR No. : {self.y}\n")
                        f.write(f"Boarding: {self.Board}\n")
                        f.write(f"Destination: {self.Desti}\n")
                        f.write(f"Train Name and Number: {self.train_name}:{self.train_no}\n")
                        f.write(f"Total Ticket Fare: {self.f}\n")
                        for passenger in self.passengers:
                            if self.remain == True:
                                f.write(
                                    f"{passenger['name']} "
                                    f"{passenger['age']} "
                                    f"{self.cmp},{passenger['seat']:02d}\n"
                                    f"{self.c}\n"
                                )
                            else:
                                f.write(
                                    f"{passenger['name']} "
                                    f"{passenger['age']} "
                                    f"{passenger['waiting.seat']}\n"
                                    f"{self.c}\n"
                                )
            obj = railin()
            if getattr(obj, "allowed" , False):
                obj.get_train()
                obj.Booking()
                obj.pricing()
                obj.save_booking()

        elif userinput == "C":
            class DetailChecking():
                def PNRChecking(self):
                    PNR = input("Enter Your PNR No. : ")
                    with open ("Details.txt" , "r") as f:
                        data = f.read()
                        if PNR in data:
                            print(data)
                        else:
                            print("Not found")

            obj = DetailChecking()
            obj.PNRChecking()

        elif userinput == "X":
            class Cancellation():
                def PNRCancellation(self):
                    PNR = input("Enter your PNR No. : ")
                    with open ("Details.txt" , "r") as f:
                        data = f.read()
                        if PNR in data:
                            print(data)
                            print("Enter Y if you want to cancel ticket")
                            print("Enter N if you don\'t want to cancel your ticket")
                            finaldecision = input("Enter here what do you want to do: ")
                            if finaldecision == "Y":
                                print("Your Ticket has been Cancelled")
                                print("Your amount will be credited in your account")
                                with open ("Details.txt" , "w") as f:
                                    f.write(" ")
                            elif finaldecision == "N":
                                print("Your Ticket is NOT cancelled")
                        else:
                            print("There is no data")

            obj = Cancellation()
            obj.PNRCancellation()

obj = Createaccount()
# else:
#     print("Login Details Are Incorrect")

# return

# obj = Procedure()