"""
This type stub file was generated by pyright.
"""

from markus.main import MetricsFilter

class AddTagFilter(MetricsFilter):
    """Metrics filter that adds tags.

    Contrived example that adds the host for all metrics generated in this
    module::

        import markus
        from markus.main import AddTagFilter

        from someplace import get_host

        metrics = markus.get_metrics(
            __name__,
            filters=[AddTag("host:" + get_host())]
        )

    """

    def __init__(self, tag) -> None: ...
    def filter(self, record): ...
