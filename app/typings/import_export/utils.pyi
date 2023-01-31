"""
This type stub file was generated by pyright.
"""

class atomic_if_using_transaction:
    """Context manager wraps `atomic` if `using_transactions`.

    Replaces code::

        if using_transactions:
            with transaction.atomic(using=using):
                return something()
        return something()
    """

    def __init__(self, using_transactions, using) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...
