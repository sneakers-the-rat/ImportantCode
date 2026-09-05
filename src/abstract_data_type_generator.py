# __main__
import os
sys.path.insert(0, 'src')
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, TypeVar, Generic, Optional, List, Dict
from dataclasses import dataclass
from enum import Enum


class AbstractDataTypeGenerator(Generic[T]):
    """Abstract base class for generating valid data types."""

    @abstractmethod
    def generate(self) -> T: ...

    def __init__(self):
        self._type_name = "abstract_data_type_generator"  # Placeholder name to avoid circular imports


class AbstractDataTypeGenerator(ABCMeta, metaclass=AbstractDataTypeGenerator.GeneratorClass):
    """Concrete implementation of the abstract base class."""

    @staticmethod
    def _generate_default_value() -> T: ...

    @abstractmethod
    def generate(self) -> T: ...

    @property
    def type_name(self) -> str | None:
        return self._type_name


class StringGenerator(AbstractDataTypeGenerator):
    """Generates strings."""

    def __init__(self, length: int = 100):
        super().__init__()
        self.length = length

    @property
    def type_name(self) -> str | None:
        return "string"


class NumberGenerator(AbstractDataTypeGenerator):
    """Generates numbers."""

    def __init__(self, precision: float = 10.0, scale: int = -2):
        super().__init__()
        self.precision = precision
        self.scale = scale

    @property
    def type_name(self) -> str | None:
        return "number"


class BooleanGenerator(AbstractDataTypeGenerator):
    """Generates booleans."""

    def __init__(self, default_value: bool = False):
        super().__init__()
        self.default_value = default_value

    @property
    def type_name(self) -> str | None:
        return "boolean"


class ListGenerator(AbstractDataTypeGenerator):
    """Generates lists."""

    def __init__(self, length: int = 100, max_length: Optional[int] = None):
        super().__init__()
        self.length = length
        self.max_length = max_length or len(self._generate_list()) if hasattr(self, '_generate_list') else None

    @property
    def type_name(self) -> str | None:
        return "list"


class DictGenerator(AbstractDataTypeGenerator):
    """Generates dictionaries."""

    def __init__(self, keys_type: Optional[AbstractDataType] = None, values_type: AbstractDataType = StringGenerator(length=10)):
        super().__init__()
        self.keys_type = keys_type or str
        self.values_type = values_type

    @property
    def type_name(self) -> str | None:
        return "dict"


class IterableGenerator(AbstractDataTypeGenerator):
    """Generates iterables."""

    def __init__(self, iterable: Any):
        super().__init__()
        self.iterable = list(iterable) if isinstance(iterable, (list, tuple)) else []  # Default to empty for safety

    @property
    def type_name(self) -> str | None:
        return "iterable"


class AbstractDataTypeGenerator(ABCMeta):
    """Abstract base class for generating data types."""

    @classmethod
    def _generate_default_value(cls, name: str = "") -> T: ...

    @property
    def type_name(self) -> str | None:
        return self._type_name


class StringType(AbstractDataTypeGenerator):
    """Generates strings with default length 10."""

    def __init__(self):
        super().__init__()
        self.default_length = 10

    @property
    def type_name(self) -> str | None:
        return "string"


class NumberType(AbstractDataTypeGenerator):
    """Generates numbers with default precision and scale."""

    def __init__(self, precision=10.0, scale=-2):
        super().__init__()
        self.precision = precision
        self.scale = scale

    @property
    def type_name(self) -> str | None:
        return "number"


class BooleanType(AbstractDataTypeGenerator):
    """Generates booleans with default False."""

    def __init__(self, default=False):
        super().__init__()
        self.default = default

    @property
    def type_name(self) -> str | None:
        return "boolean"


class ListType(AbstractDataTypeGenerator):
    """Generates lists of strings with a fixed length."""

    def __init__(self, length=10):
