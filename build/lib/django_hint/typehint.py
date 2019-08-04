from datetime import datetime as datetime

from django.db.models import QuerySet as QuerySet
from django.http.request import HttpRequest as HttpRequest
from django.contrib.auth.models import User as User
from django.db import models as models

from typing import Iterator as _Iterator
from typing import TypeVar as _TypeVar
from typing import Generic as _Generic
from typing import List as _List
from typing import Optional as _Optional
from typing import Union as _Union
from typing import Dict as _Dict
from typing import DefaultDict as _DefaultDict
from typing import Set as _Set
from typing import FrozenSet as _FrozenSet
from typing import Counter as _Counter
from typing import Deque as _Deque
from typing import ChainMap as _ChainMap

_Z = _TypeVar("_Z")
List = _List
Optional = _Optional
Union = _Union
Dict = _Dict
DefaultDict = _DefaultDict
Set = _Set
FrozenSet = _FrozenSet
Counter = _Counter
Deque = _Deque
ChainMap = _ChainMap


class Token(models.Model):
    """
    The default authorization token model.
    """
    key: str
    user: User
    created: datetime

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self) -> str:
        pass

    def __str__(self):
        return self.key


class QueryType(_Generic[_Z], QuerySet):
    def __iter__(self) -> _Iterator[_Z]: ...


class RequestType(HttpRequest):
    user: User


class DRFTokenRequestType(HttpRequest):
    user: User
    auth: Token


