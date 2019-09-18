
class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=None
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        bill_amount=0
        bill_amount+=consultation_fees
        for i in range(0,len(quantity_list)):
            bill_amount+=(quantity_list[i]*price_list[i])
        self.__bill_amount=bill_amount
    def get_bill_id(self):
        return self.__bill_id
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_amount(self):
        return self.__bill_amount