import employee_info as info

def test_get_employees_by_age_range():
    calcualted_value=0
    estimated_value=[{'age': 30, 'department': 'Sales', 'name': 'John', 'salary': 50000}]
    calcualted_value=info.get_employees_by_age_range(25,32)

    assert(calcualted_value == estimated_value)

def test_calculate_average_salary():
    calculated_value=0
    estimated_value=60166.67
    calculated_value=info.calculate_average_salary()

    assert(calculated_value == estimated_value)

def test_get_employees_by_dept():
    calculated_value=0
    estimated_value = [ {"name": "John", "age": 30, "department": "Sales", "salary": 50000},{'age': 40, 'department': 'Sales', 'name': 'Peter', 'salary': 60000}]
    calculated_value = info.get_employees_by_dept("Sales")

    assert(calculated_value == estimated_value)