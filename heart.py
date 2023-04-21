from __future__ import annotations
from item import *


class Yggdrasil:
    """ Galactic storage

    _gen_storage: general storage; does not belong to specific user
    _cored_storage: user list
    """
    _gen_storage: list[ItemStack]
    _cored_storage: list[UserCore]

    def __init__(self) -> None:
        self._gen_storage = []
        self._cored_storage = []


class BasicStorage:
    """ Basic Storage

    _cid: core id
    _inventory: storage of this core
    """
    _cid: str
    _inventory: list[ItemStack]

    def __init__(self, cid: str, inventory: list[ItemStack]) -> None:
        self._cid = cid
        self._inventory = inventory

    def get_id(self) -> str:
        return self._cid

    def get_inventory(self) -> list:
        # NOTE: Will eventually be accessible only to its user
        return [(i.get_id(), i.get_count) for i in self._inventory]


class UserCore(BasicStorage):
    """ Storage core for one user. Used by the Yggdrasil Storage

    _user: stores information of this core's user
    """
    _cid: str
    _user: User
    _inventory: list[ItemStack]

    def __init__(self, cid: str, username: str, password: str, inventory: list[ItemStack]) -> None:
        BasicStorage.__init__(self, cid, inventory)
        self._user = User(username, password)

    def __str__(self) -> None:
        """ Print info

        >>> uc = UserCore('100', 'bob', 'hunter23', [ItemStack('APPLE', 10), ItemStack('ORANGE', 3)])
        >>> print(uc)
        <BLANKLINE>
        === UserCore 100 ===
        User: bob
        Inventory: APPLE: 10, ORANGE: 3
        """
        total = '\n'
        total += f'=== UserCore {self._cid} ===\n' \
                 f'User: {self._user.get_id()}\n' \
                 f'Inventory: '
        for i in range(len(self._inventory)):
            item = self._inventory[i]
            if i == len(self._inventory) - 1:
                total += f'{item.get_id()}: {item.get_count()}'
            else:
                total += f'{item.get_id()}: {item.get_count()}, '
        return total

    def get_user(self) -> str:
        return self._user.get_id()


class User:
    """ User class of the Yggdrasil Storage

    _uid: user id
    _password: user password  # TODO
    _balance: user balance  # TODO
    """
    _uid: str
    _password: str

    def __init__(self, uid: str, password: str) -> None:
        self._uid = uid
        self._password = password

    def get_id(self) -> str:
        return self._uid
