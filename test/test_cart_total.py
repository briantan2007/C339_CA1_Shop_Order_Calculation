import pytest
from src.cart_total import calculate_total

@pytest.mark.parametrize(
    "unit_price_cents, quantity, expected",
    [
        (10, 5 , 50), # Standard calculation (10 * 5)

        (3, 15, 45), # Standard calculation ( 3 * 15)
        ( 10, 0, 0  ), # return 0 
        (15, 0 , 0 ), # return 0 
    ]
)
def test_calculate_total_valid(unit_price_cents,quantity, expected):
    assert  calculate_total(unit_price_cents, quantity) == expected
    
@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        (10.3,5) , # Invalid type (Float price)
        ("3",2), # Invalid type (String price)
        (False, 2), # Invalid type (Boolean)
        ("10",  3 ), # Invalid type (String)

    ]

    )
def test_calculated_total_type_error(unit_price_cents, quantity, expected):
        with pytest.raises(TypeError):
          calculate_total(unit_price_cents, quantity)

@pytest.mark.parametrize(
        "unit_price_cents, quantity",
        [
            (-6, 2),
            (10, -5),
            (-9,  -3),
        ]
    )
def test_calculate_total_value_error(unit_price_cents, quantity):
        with pytest.raises(ValueError):
            calculate_total(unit_price_cents, quantity)