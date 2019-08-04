`Django_hint` is a module to help you type hint your django project to work with different IDEs.

```
Notice: Python3.6 or later is required for this module
```
<br>

## Installation
You can use the `pip` to install django_hint

```
pip3 install django_hint
```

## Usage
The following use cases can be type hinted using django_hint to help you IDE recognize the type of variable.
1. Database QuerySet
2. WSGIRequest
3. Django-Rest-Framework Token Authentication

As a bonus, all of the native python type hints such as `List`, `Union`, `Optional` etc. from `typing` module can be imported from `django_hint`

## Database QuerySet
It is used to hint that the variable is an `QuerySet` object containing multiple objects whose nature we will determine.<br>
You need to hint it to `QueryType` and pass the object type inside the `[]`. Example:
```python
from django_hint import QueryType

sample_query: QueryType[SampleModel] = SampleModel.objects.filter(name='sample')
```

The `sample_query` variable will be treated as a `QuerySet`. While looping through the objects, each object will be treated as a `SampleModel`

## WSGIRequest
It is used to hint the nature of the `request` argument of the view (both function and class based). 
The `request` will be treated as a `HttpRequest` having the `user` variable attached to it. Example:
```python
from django_hint import RequestType

def sample_view(request: RequestType):
    if request.user.is_authenticated:
        print(request.POST.get('data'))
```

## Django-Rest-Framework Token Authentication
If you are using the token authentication of the `Django-Rest-Framework`, the request object will have a `user` variable and an `auth` variable of `rest_framework.authtoken.models.Token` instance. `DRFTokenRequestType` will hint the IDE of those two variables.

```python
from django_hint import DRFTokenRequestType

def sample_view(request: DRFTokenRequestType):
    print(request.auth.key)
```


