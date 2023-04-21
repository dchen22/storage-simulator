from typing import Optional, Union
from heart import *
from item import *


class StorageInterface:
    """ A Storage Interface """
    storage: Union[Yggdrasil, UserCore, None]

    def __init__(self, storage: Union[Yggdrasil, UserCore, None]) -> None:
        self.storage = storage

    def __str__(self) -> None:
        """ Print out interface of storage """
        pass
