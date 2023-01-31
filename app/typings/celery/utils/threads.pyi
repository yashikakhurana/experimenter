"""
This type stub file was generated by pyright.
"""

import threading
from contextlib import contextmanager

"""Threading primitives and utilities."""
__all__ = (
    "bgThread",
    "Local",
    "LocalStack",
    "LocalManager",
    "get_ident",
    "default_socket_timeout",
)
USE_FAST_LOCALS = ...

@contextmanager
def default_socket_timeout(timeout):  # -> Generator[None, None, None]:
    """Context temporarily setting the default socket timeout."""
    ...

class bgThread(threading.Thread):
    """Background service thread."""

    def __init__(self, name=..., **kwargs) -> None: ...
    def body(self): ...
    def on_crash(self, msg, *fmt, **kwargs): ...
    def run(self): ...
    def stop(self):  # -> None:
        """Graceful shutdown."""
        ...

def release_local(local):  # -> None:
    """Release the contents of the local for the current context.

    This makes it possible to use locals without a manager.

    With this function one can release :class:`Local` objects as well as
    :class:`StackLocal` objects.  However it's not possible to
    release data held by proxies that way, one always has to retain
    a reference to the underlying local object in order to be able
    to release it.

    Example:
        >>> loc = Local()
        >>> loc.foo = 42
        >>> release_local(loc)
        >>> hasattr(loc, 'foo')
        False
    """
    ...

class Local:
    """Local object."""

    __slots__ = ...
    def __init__(self) -> None: ...
    def __iter__(self): ...
    def __call__(self, proxy):  # -> Proxy:
        """Create a proxy for a name."""
        ...
    def __release_local__(self): ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def __delattr__(self, name): ...

class _LocalStack:
    """Local stack.

    This class works similar to a :class:`Local` but keeps a stack
    of objects instead.  This is best explained with an example::

        >>> ls = LocalStack()
        >>> ls.push(42)
        >>> ls.top
        42
        >>> ls.push(23)
        >>> ls.top
        23
        >>> ls.pop()
        23
        >>> ls.top
        42

    They can be force released by using a :class:`LocalManager` or with
    the :func:`release_local` function but the correct way is to pop the
    item from the stack after using.  When the stack is empty it will
    no longer be bound to the current context (and as such released).

    By calling the stack without arguments it will return a proxy that
    resolves to the topmost item on the stack.
    """

    def __init__(self) -> None: ...
    def __release_local__(self): ...
    __ident_func__ = ...
    def __call__(self): ...
    def push(self, obj):  # -> Any | list[Unknown]:
        """Push a new item to the stack."""
        ...
    def pop(self):  # -> Any | None:
        """Remove the topmost item from the stack.

        Note:
            Will return the old value or `None` if the stack was already empty.
        """
        ...
    def __len__(self): ...
    @property
    def stack(self): ...
    @property
    def top(self):  # -> None:
        """The topmost item on the stack.

        Note:
            If the stack is empty, :const:`None` is returned.
        """
        ...

class LocalManager:
    """Local objects cannot manage themselves.

    For that you need a local manager.
    You can pass a local manager multiple locals or add them
    later by appending them to ``manager.locals``.  Every time the manager
    cleans up, it will clean up all the data left in the locals for this
    context.

    The ``ident_func`` parameter can be added to override the default ident
    function for the wrapped locals.
    """

    def __init__(self, locals=..., ident_func=...) -> None: ...
    def get_ident(self):  # -> int:
        """Return context identifier.

        This is the identifier the local objects use internally
        for this context.  You cannot override this method to change the
        behavior but use it to link other context local objects (such as
        SQLAlchemy's scoped sessions) to the Werkzeug locals.
        """
        ...
    def cleanup(self):  # -> None:
        """Manually clean up the data in the locals for this context.

        Call this at the end of the request or use ``make_middleware()``.
        """
        ...
    def __repr__(self): ...

class _FastLocalStack(threading.local):
    def __init__(self) -> None: ...
    @property
    def top(self): ...
    def __len__(self): ...

if USE_FAST_LOCALS:
    LocalStack = ...
else:
    LocalStack = ...
