"""This program has a run-time complexity of Big-Oh of n -> O(n)"""

import csv


class Student:
    def __init__ (self,name,regNum,accessNum,course,day_of_the_week,hasEaten):
        self.name = name
        self.regNum = regNum
        self.accessNum = accessNum
        self.course = course
        self.hasEaten = hasEaten
        self.day_of_the_week=day_of_the_week
  
# Search whether student has eaten      
def linear_search(student_meal_list,regNum,days) :
    for day in student_meal_list:
        
        if day.day_of_the_week==days and day.regNum == regNum:
            
                if (day.hasEaten==True ):
                    return "Student has already eaten"
                return "Student can get food" 
        if day.day_of_the_week!=days and  day.regNum==regNum:
            return "Wrong day"
        if day.day_of_the_week == days and day.regNum != regNum :
            return "Wrong Registration Number"
        if day.day_of_the_week != days and day.regNum != regNum :
            return "Wrong Registration Number and day"
#list data structure hold student's meal routine-data                    
student_meal_list=[]

student_meal_list.append(Student("Q","S21B23/010", "A94163","B23","WEDNESDAY",False))         # O(1)
student_meal_list.append(Student("S","S21B23/020", "A95581","B10","THURSDAY",True))
student_meal_list.append(Student("A","S21B23/001", "A94156","B13","THURSDAY",True))


print(linear_search(student_meal_list,"S21B23/010","WEDNESDAY"))