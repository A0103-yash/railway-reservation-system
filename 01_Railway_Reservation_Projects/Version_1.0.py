class railin:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def Booking(self):
        self.a = input("Enter the boarding station: ")
        self.b = input("Enter the destination station: ")
        self.c = input("Enter the timing of the train: ")
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
        print(f"Boarding Station: {self.a}, Destination Station: {self.b}, Timing: {self.c}")

obj = railin()
obj.Booking()
obj.Getinfo() # Getting the information
obj.Checking() # Checking Information

# Made a program to Book, Check and Get Information of the reservation By user input just a basic working program
