"""
This type stub file was generated by pyright.
"""

"""Trace task execution.

This module defines how the task execution is traced:
errors are recorded, handlers are applied and so on.
"""
__all__ = (
    "TraceInfo",
    "build_tracer",
    "trace_task",
    "setup_worker_optimizations",
    "reset_worker_optimizations",
)
logger = ...
LOG_RECEIVED = ...
LOG_SUCCESS = ...
LOG_FAILURE = ...
LOG_INTERNAL_ERROR = ...
LOG_IGNORED = ...
LOG_REJECTED = ...
LOG_RETRY = ...
log_policy_t = ...
log_policy_reject = ...
log_policy_ignore = ...
log_policy_internal = ...
log_policy_expected = ...
log_policy_unexpected = ...
send_prerun = ...
send_postrun = ...
send_success = ...
STARTED = ...
SUCCESS = ...
IGNORED = ...
REJECTED = ...
RETRY = ...
FAILURE = ...
EXCEPTION_STATES = ...
IGNORE_STATES = ...
_localized = ...
_patched = ...
trace_ok_t = ...

def info(fmt, context):  # -> None:
    """Log 'fmt % context' with severity 'INFO'.

    'context' is also passed in extra with key 'data' for custom handlers.
    """
    ...

def task_has_custom(task, attr):  # -> None:
    """Return true if the task overrides ``attr``."""
    ...

def get_log_policy(task, einfo, exc): ...
def get_task_name(request, default):  # -> Any:
    """Use 'shadow' in request for the task name if applicable."""
    ...

class TraceInfo:
    """Information about task execution."""

    __slots__ = ...
    def __init__(self, state, retval=...) -> None: ...
    def handle_error_state(self, task, req, eager=..., call_errbacks=...): ...
    def handle_reject(self, task, req, **kwargs): ...
    def handle_ignore(self, task, req, **kwargs): ...
    def handle_retry(self, task, req, store_errors=..., **kwargs):  # -> ExceptionInfo:
        """Handle retry exception."""
        ...
    def handle_failure(
        self, task, req, store_errors=..., call_errbacks=...
    ):  # -> ExceptionInfo:
        """Handle exception."""
        ...

def traceback_clear(exc=...): ...
def build_tracer(
    name,
    task,
    loader=...,
    hostname=...,
    store_errors=...,
    Info=...,
    eager=...,
    propagate=...,
    app=...,
    monotonic=...,
    trace_ok_t=...,
    IGNORE_STATES=...,
):  # -> (uuid: Unknown, args: Unknown, kwargs: Unknown, request: Unknown | None = None) -> Unknown:
    """Return a function that traces task execution.

    Catches all exceptions and updates result backend with the
    state and result.

    If the call was successful, it saves the result to the task result
    backend, and sets the task status to `"SUCCESS"`.

    If the call raises :exc:`~@Retry`, it extracts
    the original exception, uses that as the result and sets the task state
    to `"RETRY"`.

    If the call results in an exception, it saves the exception as the task
    result, and sets the task state to `"FAILURE"`.

    Return a function that takes the following arguments:

        :param uuid: The id of the task.
        :param args: List of positional args to pass on to the function.
        :param kwargs: Keyword arguments mapping to pass on to the function.
        :keyword request: Request dict.

    """
    ...

def trace_task(task, uuid, args, kwargs, request=..., **opts):  # -> trace_ok_t:
    """Trace task execution."""
    ...

def trace_task_ret(
    name,
    uuid,
    request,
    body,
    content_type,
    content_encoding,
    loads=...,
    app=...,
    **extra_request
): ...
def fast_trace_task(
    task,
    uuid,
    request,
    body,
    content_type,
    content_encoding,
    loads=...,
    _loc=...,
    hostname=...,
    **_
): ...
def report_internal_error(task, exc): ...
def setup_worker_optimizations(app, hostname=...):  # -> None:
    """Setup worker related optimizations."""
    ...

def reset_worker_optimizations(app=...):  # -> None:
    """Reset previously configured optimizations."""
    ...
