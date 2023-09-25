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

def check_is_bytes(elem:Any) -> bool:
    if type(elem) == bytes:
        return True
    else:
        raise InvalidBytesException

def check_is_dict(elem:Any) -> bool:
    if type(elem) == Mapping:
        return True
    else:
        raise InvalidDictException
    
def check_extension_file(format:str, filename:str):
    if format == 'raw':
        ext = '.txt'
    elif format == 'csv':
        ext = '.csv'
    elif format == 'ini':
        ext = '.ini'
    elif format == 'json':
        ext = '.json'
    elif format == 'xml':
        ext = '.xml'
    elif format == 'xlsx':
        ext = '.xlsx'
    else:
        raise NotSupportedFileException()

    if not filename.endswith(ext):
        raise InvalidOutputExtension(ext=ext)
