'''
The main one is the principle of metadata processor. According to this principle, during the
processing of data, only data (immutable initial data in any textual or binary format) and metadata
(user-defined tree of values) are allowed to be used as input, meaning no user instructions (scripts) or
manually managed intermediate states are possible. This means that user is forced to use declarative
approach to describe what should be done instead of imperative one. Of course such restriction limits
user capabilities, but on the other hand, processing description in the form of metadata could be a
subject of programming itself. One can automatically transform metadata, use it to cache analysis
results or even send instructions to remote computing node. All these features are hard to implement
using scripting approach. Automatic script transformation is unreliable and requires sophisticated
code processing tools like parsers and syntax analyzers. While remote procedure call is possible
via scripts, in most cases it is restricted to simple imperative commands. Here we give only three
examples of the usefulness of the metadata processor
'''


from dataclasses import dataclass
from typing import Optional, Any, Union


Meta = ... # TODO()

SpecificationField = ... # TODO()

Specification = ... # TODO()


class SpecificationError(Exception):
    pass


@dataclass
class MetaFieldError:
    required_key: str
    required_types: Optional[tuple[type]] = None
    presented_type: Optional[type] = None
    presented_value: Any = None


class MetaVerification:

    def __init__(self, *errors: Union[MetaFieldError, "MetaVerification"]):
        self.error = errors
        # TODO("checked_success")

    @staticmethod
    def verify(meta: Meta,
               specification: Optional[Specification] = None) -> "MetaVerification":
        ...  # TODO()


def get_meta_attr(meta : Meta, key : str, default : Optional[Any] = None) -> Optional[Any]:
    ...
    # TODO()


def update_meta(meta: Meta, **kwargs):
    ...
    # TODO()
