# test_kitchen.py
from src.kitchen import Quantity, Converter, grams, ounces

def test_multiplication():
    flour = Quantity(200, "g")
    assert flour.times(3) == grams(600)

def test_multiplication_by_two():
    flour = Quantity(200, "g")
    assert flour.times(2) == grams(400)

def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200, "g")
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)

def test_equality():
    assert grams(200) == Quantity(200, "g")
    assert grams(200) != Quantity(300, "g")

def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")

def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)

def test_reduce_same_unit_needs_no_rate():
    converter = Converter()
    assert converter.reduce(grams(500), "g") == grams(500)

def test_mixed_addition():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    total = grams(200).plus(ounces(1))
    assert converter.reduce(total, "g") == grams(228)
    assert converter.reduce(ounces(2), "g") == grams(56)

def test_sum_times():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    total = grams(200).plus(ounces(1)).times(2)
    assert converter.reduce(total, "g") == grams(456)