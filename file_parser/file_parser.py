from .exceptions import *
from .abstract import ParserInterface
from .raw import RawParser
from .json import JsonParser
from .xml import XmlParser
from .xlsx import XlsxParser
from .ini import IniParser
from .csv import CsvParser

from os import access, R_OK
from os.path import exists
from typing import Any, Mapping, Union
from io import BytesIO

class FileParser():
    input_path:str
    output_path:str

    raw_content:str
    parsed_content:Mapping
    
    format:str
    __engine:ParserInterface

    def read(self, input_path:str):
        if not exists(input_path):
            raise InputFileNotFoundException
        
        if not access(input_path, R_OK):
            raise InputFileNotPermissionToReadException

        self.input_path = input_path
        f = open(input_path, 'r')
        try:
            self.raw_content = f.read()
        except UnicodeDecodeError:
            fb = open(input_path, 'rb')
            self.raw_content = fb.read()
            fb.close()
            print("Warning: input file not utf-8. Using bytes")

        f.close()

    def parse(self, format:str) -> Mapping:
        '''put here the implementation'''
        if format == 'raw':
            self.__engine = RawParser()
        elif format == 'csv':
            self.__engine = CsvParser()
        elif format == 'ini':
            self.__engine = IniParser()
        elif format == 'json':
            self.__engine = JsonParser()
        elif format == 'xml':
            raise NotImplementedException
        elif format == 'xlsx':
            self.__engine = XlsxParser()
        else:
            raise NotSupportedFileException

        setattr(self.__engine, 'raw_content', self.raw_content)
        self.format = format
        self.parsed_content = self.__engine.parse_input() # may throw exception
        return self.parsed_content

    def write(self, output_path:str):
        self.output_path = output_path

    def __dict__(self) -> Mapping:
        return dict(
            input_path      = self.input_path       if hasattr(self, 'input_path')  else '' \
            ,output_path    = self.output_path      if hasattr(self, 'output_path') else '' \
            ,raw_content    = self.raw_content      if hasattr(self, 'raw_content') else '' \
            ,format         = self.format           if hasattr(self, 'format')      else '' \
            ,parsed_content = self.parsed_content   if hasattr(self, 'parsed_content') else '' \
            )
    
    def __repr__(self) -> str:
        return str(self.__dict__())

    def __str__(self) -> str:
        return str(self.__dict__())