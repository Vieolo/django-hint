import binascii
import os
from datetime import datetime

from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from typing import Iterator, TypeVar, Generic, List, Optional, Union, Dict, DefaultDict, Set, FrozenSet, Counter, Deque, ChainMap

_Z = TypeVar("_Z")
List = List
Optional = Optional
Union = Union
Dict = Dict
DefaultDict = DefaultDict
Set = Set
FrozenSet = FrozenSet
Counter = Counter
Deque = Deque
ChainMap = ChainMap


class _Token(models.Model):
    """
    The default authorization token model.
    """
    key: str = models.CharField(_("Key"), max_length=40, primary_key=True)
    user: settings.AUTH_USER_Model = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created: datetime = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class QueryType(Generic[_Z], QuerySet):
    def __iter__(self) -> Iterator[_Z]: ...


class RequestType(WSGIRequest):
    user: settings.AUTH_USER_MODEL


class DRFTokenRequestType(WSGIRequest):
    user: settings.AUTH_USER_MODEL
    auth: _Token
