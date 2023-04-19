from typing import Annotated
from WTF import *


class ItemStack:
    """ One stack of items

    _id: item id
    _count: number of items in this stack // NOTE: we can have 0 items
    _stackable: whether this item can be stacked (like minecraft🧀🧀🧀🧀)
    """
    _id: str
    _count: Annotated[int, '> 0']
    _stackable: bool

    def __init__(self, _id: str, _count: int = 1, _stackable: bool = True) -> None:
        self._id = _id
        self._count = _count
        self._stackable = _stackable
        if not self._stackable and self._count > 1:
            raise StackabilityError

    @property
    def count(self) -> int:
        """ Getter for <_count> """
        return self._count

    @count.setter
    def count(self, new_count: int):
        """ Setter for <_count> """
        if not isinstance(new_count, int):
            raise NonIntegerError
        if new_count < 0:
            raise IsNegativeError
        if not self._stackable and new_count > 1:  # can still be 0
            raise StackabilityError
        self._count = new_count

    def can_take(self, num: int) -> bool:
        """ Use this function whenever you attempt to remove <num> items.

        - Return True if the removal of <num> items was successful
        - Return False if there are fewer than <num> items in total, or if
          <num> is negative
        - Raise a TypeError if <num> is not an integer
        """
        if num < 0:
            raise IsNegativeError
            # it is also possible that <value> is a float; negative property
            # is caught first
        try:
            self.count -= num
            return True
        except IsNegativeError as err:
            return False
        except NonIntegerError as err:
            raise NonIntegerError
        except Exception:
            raise WTF

    def can_add(self, num: int) -> bool:
        """ Return whether <num> items can be added to this stack. """
        try:
            self.count += num
            return True
        except StackabilityError:
            return False
        except NonIntegerError:
            raise NonIntegerError
        except Exception:
            raise WTF

    def get_id(self) -> str:
        """ Return this item's id """
        return self._id

    def get_count(self) -> int:
        """ Return this number of items in this stack """
        return self._count

class BasicItemErrors(Exception):
    pass


class NonIntegerError(BasicItemErrors):
    def __str__(self):
        return 'Value must be an integer'


class IsNegativeError(BasicItemErrors):
    def __str__(self):
        return 'Value must be at least 0'


class StackabilityError(BasicItemErrors):
    def __str__(self):
        return 'Item is not stackable'
