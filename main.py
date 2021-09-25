import json


class Employee:
    def __init__(self, name, experience=None,
                 date_of_joining=None,
                 date_of_birth=None,
                 age=None,
                 project_name=None,
                 skills=None,
                 user_type="Employee"
                 ):
        self.name = name
        self.experience = experience
        self.date_of_joining = date_of_joining
        self.date_of_birth = date_of_birth
        self.age = age
        self.project_name = project_name
        self.skills = skills
        self.user_type = user_type


class Database:
    def __init__(self, filename):
        self.filename = filename

    def add_emp(self, employee):
        tempdict = {
            'name': employee.name,
            'user_type': employee.user_type,
            'years_of_experience': employee.experience,
            'joining_date': employee.date_of_joining,
            'dob': employee.date_of_birth,
            'age': employee.age,
            'project_name': employee.project_name,
            'skill_set': employee.skills
        }
        with open(self.filename, 'r') as f:
            data = json.load(f)
        data['employees'].append(tempdict)
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)


if __name__ == "__main__":
    localdb=Database("database.json")
    password = input("Enter Password - ")
    while password != "password":
        password = input("Enter Valid Password - ")
    print("\t\t\t Employee management system \t\t\t")
    operations = """
    Enter 1 to Add Employee 
    Enter 2 to Update Employee Information
    Enter 3 to Find an Employee Information
    Enter 4 to remove an Employee
    Enter 0 to Exit
    """

    while True:
        n = int(input(operations))
        if n == 0:
            exit()
        elif n == 1:
            name = input("Enter Name : ")
            experience = int(input("Enter year of Experience : "))
            doj = input("Date of Joining : ")
            dob = input("Date of birth : ")
            age = int(input("Enter age : "))
            projects = input("Enter project names seperated by , : ").split(',')
            skills = input("Enter skills Seperated by , : ").split(',')
            emp1=Employee(name, experience, doj, dob ,age, projects, skills)
            localdb.add_emp(emp1)
