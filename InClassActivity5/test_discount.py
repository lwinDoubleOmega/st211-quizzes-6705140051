import pytest 
from discount import apply_discount

@pytest.mark.parametrize("price, discount, expected", [
    (100, 0 , 100), #no discount
    (100, 50, 50),  #50% discount
    (100, 100, 0),  #free
    (200, 25, 150), #25% discount
    (80, 10, 72),   #10% discount
])
def test_discount_calculation(price, discount, expected):
    assert apply_discount(price, discount) == expected