"""
This type stub file was generated by pyright.
"""

from ..types.mutation import Mutation

class ClientIDMutation(Mutation):
    class Meta:
        abstract = ...

    @classmethod
    def __init_subclass_with_meta__(
        cls, output=..., input_fields=..., arguments=..., name=..., **options
    ): ...
    @classmethod
    def mutate(cls, root, info, input): ...
