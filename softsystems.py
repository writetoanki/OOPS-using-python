from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification
    def get_job_band(self):
        return self.__job_band
    def get_employee_name(self):
        return self.__employee_name
    def get_basic_salary(self):
        return self.__basic_salary
    def get_qualification(self):
        return self.__qualification
    @abstractmethod
    def validate_job_band(self):
        pass
    def validate_basic_salary(self):
        if(self.get_basic_salary()>3000):
            return True
        else:
            return False
    def validate_qualification(self):
        if(self.__qualification=="Bachelors" or self.__qualification =="Masters"):
            return True
        else:
            return False

    @abstractmethod
    def calculate_gross_salary(self):
        pass

class Graduate(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,cgpa):
        self.__cgpa=cgpa
        super().__init__(job_band, employee_name, basic_salary, qualification)
    def get_cgpa(self):
        return self.__cgpa
    def validate_job_band(self):
        if(self.get_job_band()=="A" or self.get_job_band()=="B" or self.get_job_band()=="C"):
            return True
        else:
            return False
    def calculate_gross_salary(self):
        if(self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band()):
            pf=0.12*self.get_basic_salary()
            if(4<=self.get_cgpa()<=4.25):
                tpi=1000
            elif(4.26<=self.get_cgpa()<=4.5):
                tpi=1700
            elif(4.51<=self.get_cgpa()<=4.75):
                tpi=3200
            elif(4.76<=self.get_cgpa()<=5):
                tpi=5000
            if(self.get_job_band()=="A"):
                incentive=0.04*self.get_basic_salary()
            elif(self.get_job_band()=="B"):
                incentive=0.06*self.get_basic_salary()
            elif(self.get_job_band()=="C"):
                incentive=0.1*self.get_basic_salary()
            gross_salary=self.get_basic_salary()+pf+tpi+incentive
            return gross_salary

        else:
            return -1

class Lateral(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
        self.__skill_set=skill_set
        super().__init__(job_band, employee_name, basic_salary, qualification)
    def get_skill_set(self):
        return self.__skill_set
    def validate_job_band(self):
        if(self.get_job_band()=="D"or self.get_job_band()=="E" or self.get_job_band()=="F"):
            return True
        else:
            return False
    def calculate_gross_salary(self):
        if(self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band()):
            pf=0.12*self.get_basic_salary()

            if(self.get_skill_set()=="AGP"):
                SME=6500
            elif(self.get_skill_set()=="AGPT"):
                SME=8200
            elif(self.get_skill_set()=="AGDEV"):
                SME=11500
            else:
                SME=0

            if(self.get_job_band()=="D"):
                incentive=0.13*self.get_basic_salary()
            elif(self.get_job_band()=="E"):
                incentive=0.16*self.get_basic_salary()
            elif(self.get_job_band()=="F"):
                incentive=0.2*self.get_basic_salary()
            gross_salary=self.get_basic_salary()+pf+SME+incentive
            return gross_salary

        else:
            return -1
