import Lab2.Lab2 as Lab2

def test_find_min_max() :
    result = [] 
    input_array = [5,10,15]
    expected_result = [5,15]
    result = Lab2.find_min_max(input_array)

    assert (result == expected_result)

def test_calc_average_temperature():
    result = 0
    input_array = [5,10,15]
    expected_result = 10
    result = Lab2.calc_average_temperature(input_array)

    assert (result == expected_result)

def test_calc_median_temperature():
    result=0
    input_array = [0,1,2,3,4,5,6,7]
    expected_result = 3.5
    result = Lab2.calc_median_temperature(input_array)

    assert (result == expected_result)