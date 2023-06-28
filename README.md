# django-hint

`Django_hint` is a module to help you type hint your django project to work with different IDEs. It has been tested in PyCharm and with pylint in VSCode.

```
Notice: Python3.6 or later is required for this module
```
<br>

## Installation
You can use the `pip` to install django_hint

```
pip3 install django_hint
```

<br>

## Usage
The following use cases can be type hinted using `django_hint` to help your IDE recognize the type of variable.
1. Database QuerySet
2. Model Class
3. WSGIRequest
4. Django-Rest-Framework Token Authentication

As a bonus, all of the native python type hints such as `List`, `Union`, `Optional` etc. from `typing` module can be imported from `django_hint`

<br>

## Database QuerySet
It is used to hint that the variable is an `QuerySet` object containing multiple objects whose nature we will determine. This type is used for filter functions that return a iterable query, such as `filter`, `all`, `order_by`, etc.<br>
You need to hint it to `QueryType` and pass the object type inside the `[]`. Example:
```python
from django_hint import QueryType

sample_query: QueryType[SampleModel] = SampleModel.objects.filter(name='sample')
```

The `sample_query` variable will be treated as a `QuerySet`. While looping through the objects, each object will be treated as a `SampleModel`

*Please note that if you extend your model to `StandardModelType` as explained below, `QueryType` will not usually be needed*

<br>

## Model Class
Django adds a few attributes to a `Model` instance which are not available in the `models.Model` and will not be available in your IDE. 
The most notable attribute is the `Manager` which is accessible via an attribute called `objects`.<br>

To include these attributes in your IDE, You have to extend your model to the `StandardModelType` class of `django_hint` as well as `models.Model` and use it just like any other model class.<br>

`StandardModelType` provides the `objects` property and provides the return type of the `objects`'s functions such as `filter`, `get`, etc. In order to provide the correct return types, you have to pass the model's name as the generic type to `StandardModelType`

Note that `StandardModeltype` will NOT have any effect on your database and will NOT make new migrations on `makemigrations` command.

```python
from django.db import models
from django_hint import StandardModelType

class SampleModel(models.Model, StandardModelType['SampleModel']):
    """Just like any other model"""
    name: str = models.CharField(max_length=100)



all_samples = SampleModel.objects.all()
for sample in all_samples:
    print(sample.name)
```
<br>

## WSGIRequest
It is used to hint the nature of the `request` argument of the view (both function and class based). 
The `request` will be treated as a `HttpRequest` having the `user` variable attached to it. Example:
```python
from django_hint import RequestType

def sample_view(request: RequestType):
    if request.user.is_authenticated:
        print(request.POST.get('data'))
```
<br>

## Django-Rest-Framework Token Authentication
If you are using the token authentication of the `Django-Rest-Framework`, the request object will have a `user` variable and an `auth` variable of `rest_framework.authtoken.models.Token` instance. `DRFTokenRequestType` will hint the IDE of those two variables.

```python
from django_hint import DRFTokenRequestType

def sample_view(request: DRFTokenRequestType):
    print(request.auth.key)
```

  

