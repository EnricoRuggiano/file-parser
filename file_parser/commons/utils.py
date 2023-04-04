from ..exceptions import *
from typing import Union, Mapping, Any, List

def check_is_not_null(elem:Any) -> bool:
    if elem is None:
        raise EmptyContentException
    return True

def check_is_str(elem:Any) -> bool:
    if type(elem) == str:
        return True
    else:
        raise InvalidStringException

def check_is_dict(elem:Any) -> bool:
    if type(elem) == Mapping:
        return True
    else:
        raise InvalidDictException