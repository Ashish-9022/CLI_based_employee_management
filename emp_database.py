import json
class Database:
    def __init__(self, filename):
        self.filename = filename

    def add_emp(self, employee):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        dict_len = data['employees'][-1]['emp_id']
        if dict_len is None:
            dict_len = 1
        else:
            dict_len += 1
        tempdict = {
            'emp_id': dict_len,
            'name': employee.name,
            'user_type': "Employee",
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

    def update(self, update_emp_info_dict):
        with open(self.filename, 'r') as fr:
            data = json.load(fr)
        temp_list = []
        for emp in data['employees']:
            if emp['emp_id'] == update_emp_info_dict['emp_id']:
                temp_list.append(update_emp_info_dict)
            else:
                temp_list.append(emp)
        temp_dict = {'employees': temp_list}
        with open(self.filename, 'w') as fw:
            json.dump(temp_dict, fw, indent=3)

    def read_one(self, emp_id):
        with open(self.filename, 'r') as fr:
            data = json.load(fr)
        flag = 0
        for emp in data['employees']:
            if emp['emp_id'] == emp_id:
                flag += 1
                break
        if flag == 0:
            return False
        else:
            return data['employees'][emp_id]

    def delete_emp(self, delete_emp_id):
        with open(self.filename, 'r') as fr:
            data = json.load(fr)
        temp_list = []
        for emp in data['employees']:
            if emp['emp_id'] == delete_emp_id:
                pass
            else:
                temp_list.append(emp)
        temp_dict = {'employees': temp_list}
        with open(self.filename, 'w') as fw:
            json.dump(temp_dict, fw, indent=3)

    def show_all(self):
        with open(self.filename, 'r') as fr:
            data = json.load(fr)
        all_employees = []
        for emp in data['employees']:
            if emp['user_type'] == 'admin':
                continue
            else:
                all_employees.append([emp['emp_id'], emp['name']])
        return all_employees

