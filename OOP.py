#OBJECT ORIENTED PROGRAMMING
#it has classes and objects 
#ie
#STUDENT as a class
#attributes come from  students ie name, age , reg no etc 
# names in an students like me, Brenda we r objects in students

#syntax of oop
#  1. creating a class #NB A class name starts with a capital letter AND in singular

#cohort class 
#class Cohort :
    #name
    #description
    #Start_date
    #end_date
    
    #  I) ADD A CONSTRACTOR FOR THE COHORT CLASS
    #  II)ADD A METHOD TO A CLASS THAT PRINTS THE COHORT NAME AND THE TOTAL NUMBER OF STUDENTS
    # III)CREATE A NEW OBJECT/INSTANCE OF A COHORT CLASS
    
    #newcohort=cohort()
    
    
    
   #class constructor 
class Cohort:
     def __init__(self, name, description, start_date, end_date, total_students):
         self.name = name
         self.description = description
         self.start_date = start_date
         self.end_date = end_date
         self.total_students= total_students 
Cohortiv= Cohort( "Birungi","PACOD I" "python class", "2024-9-24", "2025-08-31", 40)
print("cohort name:",Cohortiv.name)
print("cohort start date:",Cohortiv.start_date)
print("cohort end date:",Cohortiv.end_date)
print("cohort student number:",Cohortiv.total_students)



#ii
class Cohort:
     def __init__(self, name, total_students):
         self.name = name
         self.total_students= total_students 
Cohortiv= Cohort("Cohort four","50")  
print("\nThe cohort name is:",Cohortiv.name)
print("The total number of students is ", Cohortiv.total_students) 
        
       
        
           
         #iii
class Cohort:
     def __init__(self, name,description, start_date, end_date, total_students):
         self.name = name 
         self.description = description
         self.start_date = start_date
         self.end_date = end_date
         self.total_students= total_students
Cohortv= Cohort("Cohort five","cohort5", "2024-9-24", "2025-08-31", 60)
print(f"\ncohort name: {Cohortv.name}")
print(f"cohort start date: {Cohortv.start_date}")
print(f"cohort end date:{Cohortv.end_date}")
print(f"cohort student number: {Cohortv.total_students}")

