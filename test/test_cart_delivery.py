import pytest
from src.cart_delivery import qualifies_free_delivery

@pytest.mark.parametrize(
    "total_cents, expected_eligibility",
    [
        (0, False), # Zero boundary condition
        (4999, False), 
        (5000, True),
        (7500, True),
    ]
)
def test_qualifies_free_delivery_valid(total_cents,expected_eligibility):
    assert qualifies_free_delivery(total_cents) == expected_eligibility

@pytest.mark.parametrize(
    "total_cents",
    [
        (-1),
        (-5000),
    ]

)
def test_qualifies_free_delivery_value_error(total_cents):

    with pytest.raises(ValueError):
        qualifies_free_delivery(total_cents)

@pytest.mark.parametrize(
    "total_cents",
    [
        (5000.0),
        ("5000"),
        (True),
    ]
)
def test_qualifies_free_delivery_type_error(total_cents):
    with pytest.raises(TypeError):
        qualifies_free_delivery(total_cents)