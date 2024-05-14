import employee_info as info


def test_calculate_average_salary():
    calculated_value=0
    estimated_value=60166.67
    calculated_value=info.calculate_average_salary()

    assert(calculated_value == estimated_value)
