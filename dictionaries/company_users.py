# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add
# each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
company_dict = {}

while True:
    info = input()
    if info == "End":
        break
    company_name, employee_id = info.split(" -> ")
    if company_name not in company_dict:
        company_dict[company_name] = []
    if employee_id in company_dict[company_name]:
        continue
    company_dict[company_name].append(employee_id)

for key in company_dict.keys():
    print(key)
    for value in company_dict[key]:
        print(f"-- {value}")



