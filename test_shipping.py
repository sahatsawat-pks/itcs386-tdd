# test_shipping.py
import pytest
from shipping import shipping_fee

@pytest.mark.parametrize("weight, expected", [
    (0, pytest.raises(ValueError, match="more than 0 kg")),
    (1, 40),
    (5, 60),
    (5.2, 70)
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected