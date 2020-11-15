from typing import TypeVar, Generic, get_type_hints


def render_int(num: int) -> str:
    return str(num)


print(render_int.__annotations__)


T = TypeVar("T")


class LinkedList(Generic[T]):
    data: T
    next: "LinkedList[T]"


print(LinkedList.__annotations__)
# {'data': ~T, 'next': 'LinkedList[T]'}


print(get_type_hints(LinkedList))
# {'data': ~T, 'next': __main__.LinkedList[~T]}
