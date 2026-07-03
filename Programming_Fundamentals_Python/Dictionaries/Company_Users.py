def adding_employees(base: dict, company: str, id_num: str) -> dict:
    if company not in base:
        base[company] = [id_num]
    else:
        if id_num not in base[company]:
            base[company].append(id_num)
    return base


employees_in_company = {}

while (current_command := input()) != "End":

    company_name, employee_id = current_command.split(' -> ')
    employees_in_company = adding_employees(employees_in_company, company_name, employee_id)

for name_of_company, employees in employees_in_company.items():
    print(f"{name_of_company}")
    for id_number in employees:
        print(f"-- {id_number}")