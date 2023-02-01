"""
This type stub file was generated by pyright.
"""

from celery.exceptions import ImproperlyConfigured
from kombu.serialization import (
    disable_insecure_serializers as _disable_insecure_serializers,
)
from kombu.serialization import registry

from .serialization import register_auth

"""Message Signing Serializer."""
CRYPTOGRAPHY_NOT_INSTALLED = ...
SECURITY_SETTING_MISSING = ...
SETTING_MISSING = ...
__all__ = ("setup_security",)

def setup_security(
    allowed_serializers=...,
    key=...,
    cert=...,
    store=...,
    digest=...,
    serializer=...,
    app=...,
):  # -> None:
    """See :meth:`@Celery.setup_security`."""
    ...

def disable_untrusted_serializers(whitelist=...): ...
