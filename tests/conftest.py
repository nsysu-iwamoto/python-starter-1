from types import ModuleType
from typing import Any

import pytest


def has_function(module: ModuleType, name: str) -> Any:
    # Return a callable function if exists
    if hasattr(module, name):
        f = getattr(module, name)
        if callable(f):
            return f
    return None


def assert_has_function(module: ModuleType, name: str) -> None:
    assert has_function(module, name), f"Function {name} not implemented."


def skip_if_no_function(module: ModuleType, name: str) -> Any:
    if not has_function(module, name):
        pytest.skip("Function {name} not implemented.")


""" def run_function(module: ModuleType, name: str, *args, **kwargs) -> Any:
    if not (f := has_function(module, name)):
        assert False, f"Function {name} not implemented."
    return f(*args, **kwargs)


def run_function_if_exists(module: ModuleType, name: str, *args, **kwargs) -> Any:

    # Return a callable function if exists
    if f := has_function(module, name):
        return f(*args, **kwargs)
    assert False, f"function {name} not found"
    return None
 """
