#lex_auth_012737222539321344835
#Start writing your code here
#OOPR-Assgn-30
#Start writing your code here
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
    def validate_quantity(self):
        if(1<=self.get_quantity()<=5):
            return True
        else:
            return False

    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity

class Pizzaservice:
    counter=101
    def __init__(self,customer,pizza_type,additional_topping):
        self.__service_id=None
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=None
    def validate_pizza_type(self):
        if(self.get_pizza_type().lower()=="small" or self.get_pizza_type().lower()=="medium"):
            return True
        else:
            return False


    def calculate_pizza_cost(self):
        if(self.validate_pizza_type() and self.__customer.validate_quantity()):
            if(self.get_pizza_type().lower()=="small"):
                if(self.get_additional_topping()):
                    pizzacost=185*self.__customer.get_quantity()
                else:
                    pizzacost=150*self.__customer.get_quantity()
            else:
                if(self.get_additional_topping()):
                    pizzacost=250*self.__customer.get_quantity()
                else:
                    pizzacost=200*self.__customer.get_quantity()
            self.pizza_cost=pizzacost
            Pizzaservice.counter+=1
            self.__service_id=self.get_pizza_type()[0]+str(Pizzaservice.counter)
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping

class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.__delivery_charge=None
        self.__distance_in_kms=distance_in_kms
        super().__init__(customer, pizza_type, additional_topping)
    def validate_distance_in_kms(self):
        if(1<=self.get_distance_in_kms()<=10):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        Pizzaservice.calculate_pizza_cost(self)
        if(self.validate_distance_in_kms()):

            if(self.pizza_cost!=-1):
                if(self.get_distance_in_kms()<=5):
                    self.__delivery_charge=5*self.get_distance_in_kms()
                    self.pizza_cost=self.pizza_cost+self.get_delivery_charge()
                else:
                    self.__delivery_charge=7*(self.get_distance_in_kms()-5)+25
                    self.pizza_cost=self.pizza_cost+self.get_delivery_charge()
        else:
            self.pizza_cost=-1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
