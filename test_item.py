import pytest
from item import *


def test_check_negative_count():
    item1 = Item('apple', 5)
    assert item1.count == 5

    assert item1.can_take(5)  # should take 5
    assert item1.count == 0

    assert not item1.can_take(1)  # cannot take
    assert item1.can_take(0)  # can take
    with pytest.raises(TypeError):  # can't take float
        item1.can_take(5.4)
    with pytest.raises(ValueError):  # should not take negative value
        item1.can_take(-6)


pytest.main(['test_item.py'])