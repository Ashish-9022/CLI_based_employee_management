from emp_management_utils import *
from emp_database import *
from  employee import *
import logging

logging.basicConfig(filename='error.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    localdb = Database("database.json")
    password = input("Enter Password - ")
    while password != "password":
        logging.warning('Incorrect Password')
        password = input("Enter Valid Password - ")
    print("\t\t\t Employee management system \t\t\t")
    operations = """
    Enter 1 to Add Employee 
    Enter 2 to Update Employee Information
    Enter 3 to Find an Employee Information
    Enter 4 to remove an Employee
    Enter 5 to Show all Employees
    Enter 0 to Exit
    """

    while True:
        try:
            n = int(input(operations))
        except ValueError as error:
            logging.error('Value Error at line 32 Expecting integer input')
            continue
        if n == 0:
            exit()
        elif n == 1:
            name = check_string_set_none(input("Enter Name : "))
            experience = convert_to_int(input("Enter year of Experience : "))
            doj = check_string_set_none(input("Date of Joining : "))
            dob = check_string_set_none(input("Date of birth : "))
            age = convert_to_int(input("Enter age : "))
            projects = create_list(input("Enter project names seperated by , : "))
            skills = create_list(input("Enter skills Seperated by , : "))
            emp1 = Employee(name, experience, doj, dob, age, projects, skills)
            localdb.add_emp(emp1)
            print("\n Employee Added Successfully !")
        elif n == 2:
            update_empid = int(input("Enter Employess ID which has to be updated"))
            update_emp = Employee()
            status = update_emp.set_by_emp_id(localdb, update_empid)
            if not status:
                print(f"Invalid Employee ID . Employee with {update_empid} does not exists")
                continue
            print(update_emp.get_details())
            update_emp_info_dict = update_emp.get_info_dict()
            for ele in update_emp_info_dict.keys():
                if ele in ['emp_id', 'user_type']:
                    continue
                try:
                    choice = int(input(f"Enter 1 to update {ele} OR 0 to Skip"))
                except ValueError as error:
                    choice = 0
                if choice == 1:
                    if ele in ['name', 'joining_date', 'dob']:
                        update_emp_info_dict[ele] = check_string_set_none(input(f'Enter {ele} : '))
                    elif ele in ['years_of_experience', 'age']:
                        update_emp_info_dict[ele] = convert_to_int(input(f'Enter {ele} in Numbers: '))
                    elif ele in ['project_name', 'skill_set']:
  c                     update_emp_info_dict[ele] = create_list(input(f'Enter {ele} seperated by , :  '))

                else:
                    continue
            localdb.update(update_emp_info_dict)
            print("\n Updated successfully \n")
        elif n == 3:
            find_empid = int(input("Enter Employess ID to get Details : "))
            find_emp = Employee()
            status1 = find_emp.set_by_emp_id(localdb, find_empid)
            if not status1:
                print(f"Invalid Employee ID . Employee with {find_empid} does not exists")
                continue
            print(find_emp.get_details())
        elif n == 4:
            delete_empid = int(input("Enter Employess ID to delete  : "))
            delete_emp = Employee()
            status2 = delete_emp.set_by_emp_id(localdb, delete_empid)
            if not status2:
                print(f"Invalid Employee ID . Employee with {delete_empid} does not exists")
                continue
            print(delete_emp.get_details())
            if int(input("Are you sure to delete , press 1 :")) == 1:
                localdb.delete_emp(delete_empid)
                print("\n Deleted Successfully !")
        elif n == 5:
            all_employees = localdb.show_all()
            print("\t\t\tAll Employees \t\t\t")
            print("\n \t\t\t Emp ID \t\t\t Name ")
            for emp in all_employees:
                print(f"\t\t\t\t {emp[0]} \t\t\t\t\t {emp[1]}")
