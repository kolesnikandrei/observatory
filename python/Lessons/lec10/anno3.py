from typing import Any, cast

#
# class LinkedList:
#     data: Any
#     next: 'LinkedList'   #?


#--------------------------

def get_next_type(arg=None):
    if arg:
        return LinkedList
    else:
        return Any


class LinkedList:
    data: Any
    next: 'get_next_type()'  # error: invalid type comment or annotation
