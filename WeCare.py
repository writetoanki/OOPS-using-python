
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
        
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
        
    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def get_vehicle_id(self):
        return self.__vehicle_id
    
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    
    def get_premium_amount(self):
        return self.__premium_amount
    
    def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            self.__premium_amount=.02*self.__vehicle_cost
        elif(self.__vehicle_type=="Four Wheeler"):
            self.__premium_amount=.06*self.__vehicle_cost
        else:
            print("Invalid vehicle type")    
        
    def display_vehicle_details(self):
        print((self.__vehicle_id)," / ",self.__vehicle_type," / ",str(self.__vehicle_cost)," / ",str(self.__premium_amount))

v1=Vehicle()
v1.set_vehicle_cost(10000)
v1.set_vehicle_id(101)
v1.set_vehicle_type("Two Wheeler")
v1.calculate_premium()
v1.display_vehicle_details()