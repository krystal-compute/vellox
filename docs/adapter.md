# Adapter

The heart of Vellex is the adapter class. It is a configurable wrapper that allows any [ASGI](https://asgi.readthedocs.io/en/latest) application (or framework) to run in [GCP Cloud Functions](https://cloud.google.com/functions) deployment. The adapter accepts a number of keyword arguments to configure settings related to HTTP responses, ASGI lifespan, and Base path configuration.

```python
handler = Vellox(
    app,
    lifespan="auto",
    base_path="/",
    custom_handlers=None,
    text_mime_types=None,
    exclude_headers=None
)
```

All arguments are optional.

## Configuring an adapter instance

::: vellox.adapter.Vellox
    :docstring:

## Creating an Cloud Functions handler

The adapter can be used to wrap any application without referencing the underlying methods. It defines a `__call__` method that allows the class instance to be used as an [Cloud Functions](https://cloud.google.com/functions) handler function.

```python
from fastapi import FastAPI
from vellox import Vellox

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

vellox = Vellox(app=app, lifespan="off")

def handler(request):
    return vellox(request)
```

However, this is just one convention, you may also intercept events and construct the adapter instance separately. This may be useful if you need to implement custom event handling. The `handler` in the example above could be replaced with a function.

```python
def handler(request : flask.Request):
    if request.method not in ["GET", "POST"]:
        # Do something or return, etc.
        return

    asgi_handler = Vellox(app)
    response = vellox(request) # Call the instance with the event arguments

    return response
```

## Retrieving the AWS event and context

The [GCP Cloud Functions](https://cloud.google.com/functions) handler `request` arguments are made available to an ASGI application in the ASGI connection scope.

```python
scope['flask.request']
```

For example, if you're using FastAPI it can be retrieved from the `scope` attribute of the request object.

```python
from fastapi import FastAPI
from vellox import Vellox
from starlette.requests import Request

app = FastAPI()


@app.get("/")
def hello(request: Request):
    return {"aws_event": request.scope['flask.request']}

vellox = Vellox(app=app)

def handler(request):
    return vellox(request)
```
