import json


class Employee:
    def __init__(self, emp_name=None, emp_experience=None,
                 date_of_joining=None,
                 date_of_birth=None,
                 emp_age=None,
                 project_name=None,
                 emp_skills=None,
                 user_type="Employee",
                 emp_id=None
                 ):
        self.emp_id = emp_id
        self.name = emp_name
        self.experience = emp_experience
        self.date_of_joining = date_of_joining
        self.date_of_birth = date_of_birth
        self.age = emp_age
        self.project_name = project_name
        self.skills = emp_skills
        self.user_type = user_type
        self.info_dict = {}

    def get_details(self):
        return (f'\n Employee Details '
              f'\n Employee ID :{self.emp_id} '
              f'\n Employee Name : {self.name}'
              f'\n Experiance : {self.experience}'
              f'\n Date of joining : {self.date_of_joining}'
              f'\n Date of Birth : {self.date_of_birth}'
              f'\n Age : {self.age}'
              f'\n Projects : {self.project_name}'
              f'\n Skills : {self.skills}\n')

    def set_by_emp_id(self, db, emp_id):
        temp_dict = db.read_one(emp_id)
        self.emp_id = emp_id
        self.name = temp_dict['name']
        self.experience = temp_dict['years_of_experience']
        self.date_of_joining = temp_dict['joining_date']
        self.date_of_birth = temp_dict['dob']
        self.age = temp_dict['age']
        self.project_name = temp_dict['project_name']
        self.skills = temp_dict['skill_set']
        self.user_type = temp_dict['user_type']

    def get_info_dict(self):
        self.info_dict['emp_id'] = self.emp_id
        self.info_dict['user_type'] =self.user_type
        self.info_dict['name'] = self.name
        self.info_dict['years_of_experience'] = self.experience
        self.info_dict['joining_date'] = self.date_of_joining
        self.info_dict['dob'] = self.date_of_birth
        self.info_dict['age'] = self.age
        self.info_dict['project_name'] = self.project_name
        self.info_dict['skill_set'] = self.skills
        return self.info_dict

class Database:
    def __init__(self, filename):
        self.filename = filename

    def add_emp(self, employee):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        dict_len = len(data['employees'])
        tempdict = {
            'emp_id': dict_len+1,
            'name': employee.name,
            'user_type': employee.user_type,
            'years_of_experience': employee.experience,
            'joining_date': employee.date_of_joining,
            'dob': employee.date_of_birth,
            'age': employee.age,
            'project_name': employee.project_name,
            'skill_set': employee.skills
        }
        data['employees'].append(tempdict)
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)

    def update(self,update_emp_info_dict):
        with open(self.filename, 'r') as fr:
            data = json.load(fr)
        temp_list = []
        for emp in data['employees']:
            if emp['emp_id'] == update_emp_info_dict['emp_id']:
                temp_list.append(update_emp_info_dict)
            else:
                temp_list.append(emp)
        temp_dict={}
        temp_dict['employees']=temp_list
        with open(self.filename, 'w') as fw:
            json.dump(temp_dict, fw, indent=3)

    def read_one(self, emp_id):
        with open(self.filename, 'r') as fr:
            data = json.load(fr)
        for i, emp in enumerate(data['employees']):
            if i == emp_id:
                break
        return data['employees'][i]


if __name__ == "__main__":
    localdb = Database("database.json")
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
            emp1 = Employee(name, experience, doj, dob, age, projects, skills)
            localdb.add_emp(emp1)
        elif n == 2:
            update_empid = int(input("Enter Employess ID which has to be updated"))
            update_emp = Employee()
            update_emp.set_by_emp_id(localdb,update_empid)
            print(update_emp.get_details())
            update_emp_info_dict = update_emp.get_info_dict()
            for ele in update_emp_info_dict.keys():
                if ele in ['emp_id','user_type']:
                    continue
                choice=int(input(f"Enter 1 to update {ele} OR 0 to Skip"))
                if choice == 1:
                    update_emp_info_dict[ele]=input(f'Enter {ele} : ')
                else:
                    continue
            localdb.update(update_emp_info_dict)

