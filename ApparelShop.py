

class Apparel:
    counter=100
    def __init__(self,price,item_type):
        Apparel.counter+=1
        self.__item_id=item_type[0]+str(Apparel.counter)
        self.__price=price
        self.__item_type=item_type

    def calculate_price(self):
        self.__price=self.__price*1.05
    def get_item_id(self):
        return self.__item_id
    def get_price(self):
        return self.__price
    def get_item_type(self):
        return self.__item_type
    def set_price(self,price):
        self.__price=price

class Cotton(Apparel):
    def __init__(self, price,discount):
        self.__discount=discount
        super().__init__(price,"Cotton")

    def calculate_price(self):
        super().calculate_price()
        price=super().get_price()*(100-self.__discount)/100
        price=price*1.05
        super().set_price(price)

    def get_discount(self):
        return self.__discount

class Silk(Apparel):
    def __init__(self,price):
        self.__points=None
        super().__init__(price,"Silk")
    def calculate_price(self):
        super().calculate_price()
        if(super().get_price()>10000):
            self.__points=10
        else:
            self.__points=3
        super().set_price(super().get_price()*1.1)
    def get_points(self):
        return self.__points

