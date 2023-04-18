import pytest
from item import *
from WTF import WTF


def test_check_bad_can_take_inputs():
    item1 = ItemStack('apple', 5)
    assert item1.count == 5

    assert item1.can_take(5)  # should take 5
    assert item1.count == 0

    assert not item1.can_take(1)  # cannot take
    assert item1.can_take(0)  # can take
    with pytest.raises(NonIntegerError):  # can't take float
        item1.can_take(5.4)
    with pytest.raises(IsNegativeError):  # should not take negative value
        item1.can_take(-6)


def test_bad_can_give():
    with pytest.raises(StackabilityError):
        item1 = ItemStack('diamond sword', 10, False)
    item1 = ItemStack('diamond sword', 1, False)
    with pytest.raises(StackabilityError):
        item1.count = 10  # directly setting to invalid value should raise an error, but...
    assert not item1.can_add(10)  # ...we can still send the request (it will be false)
    assert item1.can_take(1)
    assert item1.can_add(1)
    assert item1.count == 1
    item1 = ItemStack('diamond', 10, True)
    assert item1.can_add(10)
    assert item1.count == 20

pytest.main(['test_item.py'])