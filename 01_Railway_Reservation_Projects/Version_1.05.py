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
                
    def Place(self):
        lst = ["Amrawati" , "Itanagar" , "Dispur" , "Patna" , "Raipur" , "Panaji" , "Gandhinagar" , "Chandigarh" , "Delhi" , 
                    "Shimla" , "Ranchi" , "Bengaluru" , "Thiruvanathapuram" , " Bhopal" , "Mumbai" , " Imphal" , " Shillong" , "Aizawl" , "Kohima" ,
                    "Bhubaneswar" , "Jaipur" , "Gangtok" , "Chennai" , "Hyderabad" , "Agartala" , "Lucknow" , "Dehradun" , "Kolkata"]
        print(lst)
        self.Board = input("Enter your Boarding Station: ")
        self.Desti = input("Enter your Destination Station: ")

        lst1 = ["Amrawati" , "Itanagar" , "Dispur" , "Patna" , "Raipur" , "Panaji" , "Gandhinagar" , "Chandigarh" , 
                        "Shimla" , "Ranchi" , "Bengaluru" , "Thiruvanathapuram" , " Bhopal" , "Mumbai" , " Imphal" , " Shillong" , "Aizawl" , "Kohima" ,
                        "Bhubaneswar" , "Jaipur" , "Gangtok" , "Chennai" , "Hyderabad" , "Agartala" , "Lucknow" , "Dehradun" , "Kolkata"]
        lst2 = ["Delhi"]
        RJD = int(10295)

        north = ["Shimla" , "Chandigarh" , "Dehradun"]
        NEE = int(20159)
        ENE = int(20160)
        NWE = int(42013)
        WNE = int(42014)
        NCE = int(55021)
        CNE = int(55022)
        NSE = int(80251)
        SNE = int(80252)
        NIE = int(10015)
        south = ["Amaravati" , "Bengaluru" , "Thiruvananthapuram" , "Chennai" , "Hyderabad" , "Panaji" ]
        SCE = int(59021)
        CSE = int(59022)
        SWE = int(56042)
        WSE = int(56041)
        SEE = int(89026)
        ESE = int(89025)
        SIE = int(88099)
        west = ["Mumbai" , "Gandhinagar" , "Jaipur" ]
        WCE = int(54041)
        CWE = int(54042)
        WIE = int(56064)
        central = ["Bhopal" , "Raipur" ]
        CIE = int(42014)
        east = ["Patna" , "Ranchi" , "Bhubaneswar" , "Kolkata" , "Dispur" , "Itanagar" , "Shillong" ,
                        "Aizawl" , "Kohima" , "Agartala" , "Imphal" , "Gangtok"]
        ECE = int(22055)
        CEE = int(22056)
        EWE = int(21004)
        WEE = int(21005)
        EIE = int(22022)


        if ((self.Board in lst1 and self.Desti in lst2) or
            (self.Board in lst2 and self.Desti in lst1)):
            print(f"Your train: Rajdhani Express and Train number: {RJD}")
        if (self.Board in north and self.Desti in south):
            print(f"Your Train is: North-South Express and Train number: {NSE}")
        elif(self.Board in south and self.Desti in north):
            print(f"Your Train is: South-North Express and Train number: {SNE}")
        elif(self.Board in north and self.Desti in east):
            print(f"Your Train is: North-East Express and Train number: {NEE}")
        elif(self.Board in east and self.Desti in north):
            print(f"Your Train is: East-North Express and Train number: {ENE}")
        elif(self.Board in north and self.Desti in west):
            print(f"Your Train is: and Train number: {NWE}")
        elif(self.Board in west and self.Desti in north):
            print(f"Your Train is: West-North Express and Train number: {WNE}")
        elif(self.Board in north and self.Desti in central):
            print(f"Your Train is: North-Central Express and Train number: {NCE}")
        elif(self.Board in central and self.Desti in north):
            print(f"Your Train is: Central-North Express and Train number: {CNE}")
        elif(self.Board in north and self.Desti in north):
            print(f"Your Train is: North-Intercity Express and Train number: {NIE}")
        elif(self.Board in south and self.Desti in central):
            print(f"Your Train is: South-Central Express and Train number: {SCE}")
        elif(self.Board in central and self.Desti in south):
            print(f"Your Train is: Central-South Express and Train number: {CSE}")
        elif(self.Board in south and self.Desti in west):
            print(f"Your Train is: South-West Express and Train number: {SWE}")
        elif(self.Board in west and self.Desti in south):
            print(f"Your Train is: West-South Express and Train number: {WSE}")
        elif(self.Board in east and self.Desti in south):
            print(f"Your Train is: East-South Express and Train number: {ESE}")
        elif(self.Board in south and self.Desti in east):
            print(f"Your Train is: South-East Express and Train number: {SEE}")
        elif(self.Board in south and self.Desti in south):
            print(f"Your Train is: South-Intercity Express and Train number: {SIE}")
        elif(self.Board in west and self.Desti in central):
            print(f"Your Train is: West-Central Express and Train number: {WCE}")
        elif(self.Board in central and self.Desti in west):
            print(f"Your Train is: Central-West Express and Train number: {CWE}")
        elif(self.Board in west and self.Desti in west):
            print(f"Your Train is: West-Intercity Express and Train number: {WIE}")
        elif(self.Board in central and self.Desti in central):
            print(f"Your Train is: Central-Intercity Express and Train number: {CIE}")
        elif(self.Board in east and self.Desti in central):
            print(f"Your Train is: East-Central Express and Train number: {ECE}")
        elif(self.Board in central and self.Desti in east):
            print(f"Your Train is: Central-East Express and Train number: {CEE}")
        elif(self.Board in east and self.Desti in west):
            print(f"Your Train is: East-West Express and Train number: {EWE}")
        elif(self.Board in west and self.Desti in east):
            print(f"Your Train is: West-East Express and Train number: {WEE}")
        elif(self.Board in east and self.Desti in east):
            print(f"Your Train is: East-Intercity Express and Train number: {EIE}")

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
                
obj = railin()
if getattr(obj, "allowed" , False):
    obj.Place()
    obj.Booking()
    obj.PNRChecking()
    obj.Getinfo() # Getting the information
    obj.Checking() # Checking Information

