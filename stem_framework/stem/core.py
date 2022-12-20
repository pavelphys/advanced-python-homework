from typing import Optional, Protocol


def pascal_case_to_snake_case(name: str) -> str:
    result = name[0]
    for i in range(1, len(name)-1):
        if name[i].isupper() and name[i+1].islower():
            result += "_" +  name[i]
        else:
            result +=  name[i]
    result += name[-1]
    return result.lower()


class Named:
    _name: Optional[str] = None

    @property
    def name(self):
        if self._name != None:
            return self._name
        return pascal_case_to_snake_case(self.__class__.__name__)


class Dataclass(Protocol):
    __dataclass_fields__:object
