from collections.abc import Callable, Iterable
from typing import Any

from django.core.exceptions import ImproperlyConfigured

class InvalidCacheBackendError(ImproperlyConfigured): ...
class CacheKeyWarning(RuntimeWarning): ...

DEFAULT_TIMEOUT: int
MEMCACHE_MAX_KEY_LENGTH: int

def default_key_func(key: str, key_prefix: str, version: Any) -> str: ...
def get_key_func(key_func: Callable[..., Any] | str | None) -> Callable[..., Any]: ...

class BaseCache:
    default_timeout: int = ...
    key_prefix: str = ...
    version: int = ...
    key_func: Callable[..., Any] = ...
    def __init__(self, params: dict[str, Any]) -> None: ...
    def get_backend_timeout(self, timeout: int | None = ...) -> float | None: ...
    def make_key(self, key: str, version: int | None = ...) -> str: ...
    def add(
        self,
        key: str,
        value: Any,
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> bool: ...
    async def aadd(
        self,
        key: str,
        value: Any,
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> bool: ...
    def get(
        self, key: str, default: Any | None = ..., version: int | None = ...
    ) -> Any: ...
    async def aget(
        self, key: str, default: Any | None = ..., version: int | None = ...
    ) -> Any: ...
    def set(
        self,
        key: str,
        value: Any,
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> None: ...
    async def aset(
        self,
        key: str,
        value: Any,
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> None: ...
    def touch(
        self, key: str, timeout: int | None = ..., version: int | None = ...
    ) -> bool: ...
    def delete(self, key: str, version: int | None = ...) -> None: ...
    def get_many(
        self, keys: Iterable[str], version: int | None = ...
    ) -> dict[str, int | str]: ...
    async def aget_many(
        self, keys: Iterable[str], version: int | None = ...
    ) -> dict[str, int | str]: ...
    def get_or_set(
        self,
        key: str,
        default: Any | None,
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> Any | None: ...
    async def aget_or_set(
        self,
        key: str,
        default: Any | None,
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> Any | None: ...
    def has_key(self, key: str, version: int | None = ...) -> bool: ...
    def incr(self, key: str, delta: int = ..., version: int | None = ...) -> int: ...
    def decr(self, key: str, delta: int = ..., version: int | None = ...) -> int: ...
    def __contains__(self, key: str) -> bool: ...
    def set_many(
        self,
        data: dict[str, Any],
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> list[Any]: ...
    async def aset_many(
        self,
        data: dict[str, Any],
        timeout: int | None = ...,
        version: int | None = ...,
    ) -> list[Any]: ...
    def delete_many(self, keys: Iterable[str], version: int | None = ...) -> None: ...
    async def adelete_many(
        self, keys: Iterable[str], version: int | None = ...
    ) -> None: ...
    def clear(self) -> None: ...
    def validate_key(self, key: str) -> None: ...
    def incr_version(
        self, key: str, delta: int = ..., version: int | None = ...
    ) -> int: ...
    def decr_version(
        self, key: str, delta: int = ..., version: int | None = ...
    ) -> int: ...
    def close(self, **kwargs: Any) -> None: ...
