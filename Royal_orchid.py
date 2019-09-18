#lex_auth_012727119215337472135

class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None

    def validate_flower(self):
        l1=["orchid","rose","jasmine"]
        if self.__flower_name.lower() in l1:
            return True

        return False
    def validate_stock(self,required_quantity):
        if(self.__stock_available>=required_quantity):
            return True
        else:
            return False
    def sell_flower(self,required_quantity):
        if(self.validate_flower() and self.validate_stock(required_quantity)):
            self.__stock_available=self.__stock_available-required_quantity
    def check_level(self):

        if(self.__flower_name.lower()=="orchid" and self.__stock_available<15):
            return True
        elif(self.__flower_name.lower()=="rose" and self.__stock_available<25):
            return True
        elif(self.__flower_name.lower()=="jasmine" and self.__stock_available<40):
            return True
        else:
            return False
    def set_flower_name(self,flower_name):
        f=flower_name.lower()
        self.__flower_name=f

    def get_flower_name(self):
        return self.__flower_name
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available

    def get_stock_available(self):
        return self.__stock_available
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg

    def get_price_per_kg(self):
        return self.__price_per_kg
Flower()