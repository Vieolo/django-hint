from datetime import datetime as datetime

from django.db.models import QuerySet as QuerySet
from django.http.request import HttpRequest as HttpRequest
from django.contrib.auth.models import User as User
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned as Mor


from typing import Iterator
from typing import TypeVar
from typing import Generic
from typing import List
from typing import Optional
from typing import Union
from typing import Dict
from typing import DefaultDict
from typing import Set
from typing import FrozenSet
from typing import Counter
from typing import Deque
from typing import ChainMap
from typing import Callable
from typing import Tuple
from typing import Type
from typing import ClassVar

_Z = TypeVar("_Z")


class Token:
    """
    The default authorization token model.
    """
    key: str
    user: User
    created: datetime

    def save(self, *args, **kwargs):
        pass

    def generate_key(self) -> str:
        pass

    def __str__(self):
        pass

    @classmethod
    def from_db(cls, db, field_names, values):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

    def __reduce__(self):
        pass

    def __getstate__(self):
        """Hook to allow choosing the attributes to pickle."""
        pass

    def __setstate__(self, state):
        pass

    def get_deferred_fields(self):
        """
        Return a set containing names of deferred fields for this instance.
        """
        pass

    def refresh_from_db(self, using=None, fields=None):
        """
        Reload field values from the database.

        By default, the reloading happens from the database this instance was
        loaded from, or by the read router if this instance wasn't loaded from
        any database. The using parameter will override the default.

        Fields can be used to specify which fields to reload. The fields
        should be an iterable of field attnames. If fields is None, then
        all non-deferred fields are reloaded.

        When accessing deferred fields of an instance, the deferred loading
        of the field will call this method.
        """
        pass

    def serializable_value(self, field_name):
        """
        Return the value of the field name for this instance. If the field is
        a foreign key, return the id value instead of the object. If there's
        no Field object with this name on the model, return the model
        attribute's value.

        Used to serialize a field's value (in the serializer, or form output,
        for example). Normally, you would just access the attribute directly
        and not use this method.
        """
        pass

    def save_base(self, raw=False, force_insert=False,
                  force_update=False, using=None, update_fields=None):
        """
        Handle the parts of saving which should be done only once per save,
        yet need to be done in raw saves, too. This includes some sanity
        checks and signal sending.

        The 'raw' argument is telling save_base not to save any parent
        models and not to do any changes to the values before save. This
        is used by fixture loading.
        """
        pass

    def delete(self, using=None, keep_parents=False):
        pass

    def prepare_database_save(self, field):
        pass

    def clean(self):
        """
        Hook for doing any extra model-wide validation after clean() has been
        called on every field by self.clean_fields. Any ValidationError raised
        by this method will not be associated with a particular field; it will
        have a special-case association with the field defined by NON_FIELD_ERRORS.
        """
        pass

    def validate_unique(self, exclude=None):
        """
        Check unique constraints on the model and raise ValidationError if any
        failed.
        """
        pass

    def date_error_message(self, lookup_type, field_name, unique_for):
        pass

    def unique_error_message(self, model_class, unique_check):
        pass

    def full_clean(self, exclude=None, validate_unique=True):
        """
        Call clean_fields(), clean(), and validate_unique() on the model.
        Raise a ValidationError for any errors that occur.
        """
        pass

    def clean_fields(self, exclude=None):
        """
        Clean all fields and raise a ValidationError containing a dict
        of all validation errors if any occur.
        """
        pass

    @classmethod
    def check(cls, **kwargs):
        pass


class RequestType(HttpRequest):
    user: User


class DRFTokenRequestType(HttpRequest):
    user: User
    auth: Token



############################
#    QuerySet and Model    #
############################


class QueryType(Generic[_Z], QuerySet):
    def __iter__(self) -> Iterator[_Z]: pass


class QuerySetBase(Generic[_Z], QuerySet):
    def get(self, *args, **kwargs) -> _Z:
        """
        Perform the query and return a single object matching the given
        keyword arguments.
        """
        pass
    
    def create(self, **kwargs) -> _Z:
        """
        Create a new object with the given kwargs, saving it to the database
        and returning the created object.
        """
        pass
        
    def first(self) -> _Z:
        """Return the first object of a query or None if no match is found."""
        pass

    def last(self) -> _Z:
        """Return the last object of a query or None if no match is found."""
        pass

    def get_or_create(self, defaults=None, **kwargs) -> Tuple[_Z, bool]: 
        """
        Look up an object with the given kwargs, creating one if necessary.
        Return a tuple of (object, created), where created is a boolean
        specifying whether an object was created.
        """
        pass

    def update_or_create(self, defaults=None, create_defaults=None, **kwargs) -> Tuple[_Z, bool]:
        """
        Look up an object with the given kwargs, updating one with defaults
        if it exists, otherwise create a new one. Optionally, an object can
        be created with different values than defaults by using
        create_defaults.
        Return a tuple (object, created), where created is a boolean
        specifying whether an object was created.
        """
        pass

class QueryFilter(Generic[_Z], QuerySetBase[_Z]):
    def __iter__(self) -> Iterator[_Z]: pass


class QuerySetType(Generic[_Z], QuerySetBase[_Z]):
    def all(self) -> QueryFilter[_Z]:
        """
        Return a new QuerySet that is a copy of the current one. This allows a
        QuerySet to proxy for a model manager in some cases.
        """
        pass
    
    def filter(self, *args, **kwargs) -> QueryFilter[_Z]:
        """
        Return a new QuerySet instance with the args ANDed to the existing
        set.
        """
        pass
    
    def exclude(self, *args, **kwargs) -> QueryFilter[_Z]:
        """
        Return a new QuerySet instance with NOT (args) ANDed to the existing
        set.
        """
        pass
    
    def select_for_update(self, nowait=False, skip_locked=False, of=(), no_key=False) -> QueryFilter[_Z]:
        """
        Return a new QuerySet instance that will select objects with a
        FOR UPDATE lock.
        """
        pass
    
    def select_related(self, *fields) -> QueryFilter[_Z]:
        """
        Return a new QuerySet instance that will select related objects.

        If fields are specified, they must be ForeignKey fields and only those
        related objects are included in the selection.

        If select_related(None) is called, clear the list.
        """
        pass
    
    def prefetch_related(self, *lookups) -> QueryFilter[_Z]:
        """
        Return a new QuerySet instance that will prefetch the specified
        Many-To-One and Many-To-Many related objects when the QuerySet is
        evaluated.

        When prefetch_related() is called more than once, append to the list of
        prefetch lookups. If prefetch_related(None) is called, clear the list.
        """
        pass
    
    def annotate(self, *args, **kwargs) -> QueryFilter[_Z]:
        """
        Return a query set in which the returned objects have been annotated
        with extra data or aggregations.
        """
        pass
    
    def alias(self, *args, **kwargs) -> QueryFilter[_Z]:
        """
        Return a query set with added aliases for extra data or aggregations.
        """
        pass
    
    def order_by(self, *field_names) -> QueryFilter[_Z]:
        """Return a new QuerySet instance with the ordering changed."""
        pass
    
    def distinct(self, *field_names) -> QueryFilter[_Z]:
        """
        Return a new QuerySet instance that will select only distinct results.
        """
        pass
    def reverse(self) -> QueryFilter[_Z]:
        """Reverse the ordering of the QuerySet."""
        pass

class StandardModelType(Generic[_Z]):
    objects: QuerySetType[_Z]
    DoesNotExist: Union[ObjectDoesNotExist, Callable]
    MultipleObjectsReturned: Union[Mor, Callable]
