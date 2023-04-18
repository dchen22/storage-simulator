from typing import Annotated
from WTF import *


class Item:
    """ Item class

    i_id: item id
    count: number of items in this stack
    """
    i_id: str
    _count: Annotated[int, '>= 0']

    def __init__(self, i_id: str, _count: int=0) -> None:
        self.i_id = i_id
        self._count = _count

    @property
    def count(self) -> int:
        """ Getter for <_count> """
        return self._count

    @count.setter
    def count(self, new_count: int):
        """ Setter for <_count> """
        if not isinstance(new_count, int):
            raise TypeError('Item.count is set to non-integer')
        if new_count < 0:
            raise ValueError('Item.count is set to negative')
        self._count = new_count

    def can_take(self, num: int) -> bool:
        """ Use this function whenever you attempt to remove <num> items.

        - Return True if the removal of <num> items was successful
        - Return False if there are fewer than <num> items in total, or if
          <num> is negative
        - Raise a TypeError if <num> is not an integer
        """
        if num < 0:
            raise ValueError('Value must be at least 0')
            # it is also possible that <value> is a float; negative property
            # is caught first
        try:
            self.count -= num
            return True
        except ValueError as err:
            if str(err) == 'Item.count is set to negative':
                return False
            else:
                raise WTF
        except TypeError as err:
            if str(err) == 'Item.count is set to non-integer':
                raise TypeError('Value must be an integer')
            else:
                raise WTF

