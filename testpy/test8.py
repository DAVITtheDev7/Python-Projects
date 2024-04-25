class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

class Employee:
    def __init__(self, profession, monthly_salary, working_hours):
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

class Doctor(Person, Employee):
    def __init__(self, firstname, lastname, age, profession, monthly_salary, working_hours):
        Person.__init__(self, firstname, lastname, age)
        Employee.__init__(self, profession, monthly_salary, working_hours)

    def get_hourly_rate(self):
        hourly_rate = self.monthly_salary / (self.working_hours * 4)
        return hourly_rate


firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
age = int(input("Enter age: "))


profession = input("Enter profession: ")
monthly_salary = int(input("Enter monthly salary: "))
working_hours = int(input("Enter working hours: "))

doctor = Doctor(firstname, lastname, age, profession, monthly_salary, working_hours)


print(f"\nFirstname - {doctor.firstname}")
print(f"Lastname - {doctor.lastname}")      
print(f"Age - {doctor.age}")      
print(f"Profession - {doctor.profession}")      
print(f"Monthly salary - {doctor.monthly_salary}")      
print(f"Working hours - {doctor.working_hours}")     
hourly_rate = doctor.get_hourly_rate()
print(f"Hourly salary - {hourly_rate:.2f}\n")
