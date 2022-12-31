"""the runnning complexity of this algorithm is O(n^2)"""
import csv
class Student:
    def __init__(self,name,reg_Num,access_Num,course,has_eaten):
        self.name=name
        self.reg_Num = reg_Num
        self.access_Num = access_Num
        self.course=course
        self.has_eaten=has_eaten

class DailyAttendace:
    def __init__ (self,day_of_the_week,stud_meal_list):
        self.day_of_the_week = day_of_the_week
        self.stud_meal_list = stud_meal_list

def linear_search(cafe_list, reg_Num, day_of_the_week):

    for day in cafe_list:
        if(day.day_of_the_week == day_of_the_week):
            for student in day.stud_meal_list:
                if(reg_Num == student.reg_Num):
                    if(not student.has_eaten):
                        return True
    return False



def main():
            
    serve_student = []

    stud_meal_list = []

    stud_meal_list.append(Student("Q","S22B23/004","A98597","B23",False));
    stud_meal_list.append(Student("A","S24B13/060","A94446","B13",True));
    stud_meal_list.append(Student("S","S21B13/023","A93581","B13",True));

    serve_student.append(DailyAttendace("Monday",stud_meal_list))


    print(linear_search(serve_student,"S21B23/019","Wednesday"))

    
main()