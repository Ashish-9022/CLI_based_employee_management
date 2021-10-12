
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
        self.__user_type = user_type
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
        if not temp_dict:
            return False
        self.emp_id = emp_id
        self.name = temp_dict['name']
        self.experience = temp_dict['years_of_experience']
        self.date_of_joining = temp_dict['joining_date']
        self.date_of_birth = temp_dict['dob']
        self.age = temp_dict['age']
        self.project_name = temp_dict['project_name']
        self.skills = temp_dict['skill_set']
        self.__user_type = temp_dict['user_type']
        return True

    def get_info_dict(self):
        self.info_dict['emp_id'] = self.emp_id
        self.info_dict['user_type'] = self.__user_type
        self.info_dict['name'] = self.name
        self.info_dict['years_of_experience'] = self.experience
        self.info_dict['joining_date'] = self.date_of_joining
        self.info_dict['dob'] = self.date_of_birth
        self.info_dict['age'] = self.age
        self.info_dict['project_name'] = self.project_name
        self.info_dict['skill_set'] = self.skills
        return self.info_dict

