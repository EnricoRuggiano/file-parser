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
from .commons import *

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
        self.raw_content = ""

        # print warning for xml
        if input_path.endswith('.xml'):
            warn_xml:str = """ Warning: .xml files may exploit vulnerabilities in the xml parsers to perform some malicious attack. 
    Please be aware that your input '.xml' file comes from a trusted source."""

            print(warn_xml)
            f = open(input_path, 'rb')
        else:
            f = open(input_path, 'r')

        try:
            f.seek(0)
            self.raw_content = f.read()
        except UnicodeDecodeError:
            fb = open(input_path, 'rb')
            fb.seek(0)
            self.raw_content = fb.read()
            fb.close()
            print("Warning: input file not utf-8. Using bytes")

        f.close()

    def parse(self, format:str, **kwargs) -> Mapping:
        '''put here the implementation'''
        if format == 'raw':
            self.__engine = RawParser()
        elif format == 'csv':
            self.__engine = CsvParser(**kwargs)
        elif format == 'ini':
            self.__engine = IniParser()
        elif format == 'json':
            self.__engine = JsonParser()
        elif format == 'xml':
            self.__engine = XmlParser(**kwargs)
        elif format == 'xlsx':
            self.__engine = XlsxParser()
        else:
            raise NotSupportedFileException

        setattr(self.__engine, 'raw_content', self.raw_content)
        self.format = format
        self.parsed_content = self.__engine.parse_input() # may throw exception
        return self.parsed_content

    def write(self, format:str, output_path:str, **kwargs) -> str:
        _content = kwargs.get('content') if kwargs.get('content') else self.parsed_content
        check_is_not_null(_content)
        check_extension_file(format, output_path)        
        self.output_path = output_path

        if format == 'raw':
            self.__engine = RawParser()
        elif format == 'csv':
            self.__engine = CsvParser(**kwargs)
        elif format == 'ini':
            self.__engine = IniParser()
        elif format == 'json':
            self.__engine = JsonParser()
        elif format == 'xml':
            self.__engine = XmlParser(**kwargs)
        elif format == 'xlsx':
            self.__engine = XlsxParser()
        else:
            raise NotSupportedFileException

        self.__engine.parse_output(self.output_path, _content, **kwargs) # may throw exceptions
        return self.output_path


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