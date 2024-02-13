class Vehicle:
    wheels = 4 # default class variable

    def __init__(self,make,model,year,color):
        self.make = make    #instance variables
        self.model = model  #instance variables
        self.year = year    #instance variables
        self.color = color  #instsnce variables


    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")