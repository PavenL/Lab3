import price_info as Price


def test_cost_of_fruits() :
    calculated_cost=0
    estimated_value = 12.0
    calculated_cost = Price.cost_of_fruits('apple',10)

    assert (estimated_value == calculated_cost)

def test_total_cost_shopping():
    calculated_total_cost=0 
    estimated_value= 46.75
    calculated_total_cost = Price.total_cost_shopping()
    assert (estimated_value == calculated_total_cost)