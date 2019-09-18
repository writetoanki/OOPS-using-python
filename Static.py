
class Classroom:
    classroom_list=[]

    @staticmethod
    def search_classroom(class_room):
        for i in Classroom.classroom_list:
            if(i.lower()==class_room.lower()):
                return "Found"

        return -1