"""
This type stub file was generated by pyright.
"""

from kombu.utils.objects import cached_property

"""Task request.

This module defines the :class:`Request` class, that specifies
how tasks are executed.
"""
__all__ = ("Request",)
IS_PYPY = ...
logger = ...
_does_info = ...
_does_debug = ...

def __optimize__(): ...

tz_or_local = ...
send_revoked = ...
send_retry = ...
task_accepted = ...
task_ready = ...
revoked_tasks = ...

class Request:
    """A request for task execution."""

    acknowledged = ...
    time_start = ...
    worker_pid = ...
    time_limits = ...
    _already_revoked = ...
    _already_cancelled = ...
    _terminate_on_ack = ...
    _apply_result = ...
    _tzlocal = ...
    if notIS_PYPY:
        __slots__ = ...
    def __init__(
        self,
        message,
        on_ack=...,
        hostname=...,
        eventer=...,
        app=...,
        connection_errors=...,
        request_dict=...,
        task=...,
        on_reject=...,
        body=...,
        headers=...,
        decoded=...,
        utc=...,
        maybe_make_aware=...,
        maybe_iso8601=...,
        **opts
    ) -> None: ...
    @property
    def delivery_info(self): ...
    @property
    def message(self): ...
    @property
    def request_dict(self): ...
    @property
    def body(self): ...
    @property
    def app(self): ...
    @property
    def utc(self): ...
    @property
    def content_type(self): ...
    @property
    def content_encoding(self): ...
    @property
    def type(self): ...
    @property
    def root_id(self): ...
    @property
    def parent_id(self): ...
    @property
    def argsrepr(self): ...
    @property
    def args(self): ...
    @property
    def kwargs(self): ...
    @property
    def kwargsrepr(self): ...
    @property
    def on_ack(self): ...
    @property
    def on_reject(self): ...
    @on_reject.setter
    def on_reject(self, value): ...
    @property
    def hostname(self): ...
    @property
    def ignore_result(self): ...
    @property
    def eventer(self): ...
    @eventer.setter
    def eventer(self, eventer): ...
    @property
    def connection_errors(self): ...
    @property
    def task(self): ...
    @property
    def eta(self): ...
    @property
    def expires(self): ...
    @expires.setter
    def expires(self, value): ...
    @property
    def tzlocal(self): ...
    @property
    def store_errors(self): ...
    @property
    def task_id(self): ...
    @task_id.setter
    def task_id(self, value): ...
    @property
    def task_name(self): ...
    @task_name.setter
    def task_name(self, value): ...
    @property
    def reply_to(self): ...
    @property
    def replaced_task_nesting(self): ...
    @property
    def correlation_id(self): ...
    def execute_using_pool(self, pool, **kwargs):
        """Used by the worker to send this task to the pool.

        Arguments:
            pool (~celery.concurrency.base.TaskPool): The execution pool
                used to execute this request.

        Raises:
            celery.exceptions.TaskRevokedError: if the task was revoked.
        """
        ...
    def execute(self, loglevel=..., logfile=...):  # -> None:
        """Execute the task in a :func:`~celery.app.trace.trace_task`.

        Arguments:
            loglevel (int): The loglevel used by the task.
            logfile (str): The logfile used by the task.
        """
        ...
    def maybe_expire(self):  # -> Literal[True] | None:
        """If expired, mark the task as revoked."""
        ...
    def terminate(self, pool, signal=...): ...
    def cancel(self, pool, signal=...): ...
    def revoked(self):  # -> bool:
        """If revoked, skip task and mark state."""
        ...
    def send_event(self, type, **fields): ...
    def on_accepted(self, pid, time_accepted):  # -> None:
        """Handler called when task is accepted by worker pool."""
        ...
    def on_timeout(self, soft, timeout):  # -> None:
        """Handler called if the task times out."""
        ...
    def on_success(self, failed__retval__runtime, **kwargs):  # -> None:
        """Handler called if the task was successfully processed."""
        ...
    def on_retry(self, exc_info):  # -> None:
        """Handler called if the task should be retried."""
        ...
    def on_failure(self, exc_info, send_failed_event=..., return_ok=...):  # -> None:
        """Handler called if the task raised an exception."""
        ...
    def acknowledge(self):  # -> None:
        """Acknowledge task."""
        ...
    def reject(self, requeue=...): ...
    def info(self, safe=...): ...
    def humaninfo(self): ...
    def __str__(self) -> str:
        """``str(self)``."""
        ...
    def __repr__(self):  # -> str:
        """``repr(self)``."""
        ...
    @cached_property
    def chord(self): ...
    @cached_property
    def errbacks(self): ...
    @cached_property
    def group(self): ...
    @cached_property
    def group_index(self): ...

def create_request_cls(
    base,
    task,
    pool,
    hostname,
    eventer,
    ref=...,
    revoked_tasks=...,
    task_ready=...,
    trace=...,
    app=...,
):  # -> Type[Request]:
    class Request(base): ...
