import Lab2.bmi as bmi

print ("Test Lab2")

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.7,60)==0

def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.6,75)==1

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.9,50)==-1