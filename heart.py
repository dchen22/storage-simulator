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


class UserCore:
    """ Storage core for one user. Used by the Yggdrasil Storage

    _cid: core id
    _user: stores information of this core's user
    _inventory: storage of this core
    """
    _cid: str
    _user: User
    _inventory: list[ItemStack]

    def __init__(self, username: str, password: str, cid: str) -> None:
        self._user = User(username, password)
        self._cid = cid

    def get_id(self) -> str:
        return self._cid

    def get_user(self) -> str:
        return self._user.get_id()

    def get_inventory(self) -> list:
        # NOTE: Will eventually be accessible only to its user
        return [(i.get_id(), i.get_count) for i in self._inventory]


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
