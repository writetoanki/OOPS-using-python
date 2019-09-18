#lex_auth_012751870201536512237
#Start writing your code here
#OOPR-Assgn-19
#Start writing your code here

class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__ticket_id=None
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination

    def validate_source_destination(self):
        l1=["Mumbai","Pune","Chennai","Kolkata"]
        d="delhi"
        if(self.__source.lower()==d):
            for i in l1:
                if(i.lower()==self.__destination.lower()):
                    return True

            return False
        else:
            return False

    def generate_ticket(self):
        if(self.validate_source_destination()):
            Ticket.counter+=1
            if(Ticket.counter<10):

                self.__ticket_id=self.__source[0]+self.__destination[0]+"0"+str(Ticket.counter)
            else:

                self.__ticket_id=self.__source[0]+self.__destination[0]+str(Ticket.counter)
        else:
            self.__ticket_id=None
            print("Invalid source and destination")
    def get_ticket_id(self):
        return self.__ticket_id
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination


t=Ticket("ankita","delhi","Mumbai")
t1=Ticket("ankita","delhi","Mumbai")
t.generate_ticket()
t1.generate_ticket()
