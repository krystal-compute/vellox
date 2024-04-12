# HTTP

## Configuring binary responses

Binary responses are determined using the `Content-Type` and `Content-Encoding` headers from the event request and a list of text MIME types.

### Compression

If the `Content-Encoding` header is set to `gzip` or `br`, then a binary response will be returned regardless of MIME type.

## State machine

The `HTTPCycle` is used by the adapter to communicate message events between the application and GCP. It is a state machine that handles the entire ASGI request and response cycle.

### HTTPCycle

::: vellox.protocols.http.HTTPCycle
    :docstring:
    :members: run receive send

### HTTPCycleState

::: vellox.protocols.http.HTTPCycleState
    :docstring:
