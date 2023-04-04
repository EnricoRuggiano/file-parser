import abc
from typing import Mapping

class ParserInterface():
    __metaclass__ = abc.ABCMeta
    
    raw_content:str
    content:str

    @abc.abstractmethod
    def parse_input(self) -> Mapping:
        ...

    @abc.abstractmethod
    def parse_output(self):
        ...