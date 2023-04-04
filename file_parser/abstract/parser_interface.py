import abc
from typing import Mapping, List

class ParserInterface():
    __metaclass__ = abc.ABCMeta
    
    headers:List[str] = []
    raw_content:str
    content:Mapping

    @abc.abstractmethod
    def parse_input(self) -> Mapping:
        ...

    @abc.abstractmethod
    def parse_output(self):
        ...