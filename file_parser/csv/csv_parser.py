from ..abstract import ParserInterface
from ..exceptions import *
from ..commons import *
from typing import Mapping, List

from io import StringIO
import csv

class CsvParser(ParserInterface):      
    format:str = 'csv'
    delimiter:str = ';'
    body:List[List[str]] = []

    def __init__(self, **kwargs):
        if 'delimiter' in kwargs.keys():
            self.delimiter = kwargs['delimiter'] 

    def parse_input(self) -> List[Mapping]:
        check_is_not_null(self.raw_content)
        check_is_str(self.raw_content)

        f:StringIO = StringIO(self.raw_content)
        csv_file = csv.reader(f, delimiter=self.delimiter)
        
        # reset body
        self.body = []
        
        # read csv file
        line:int = 1
        for r in csv_file:
            if line == 1:
                self.headers = r
            else:
                self.body.append(r)
            line += 1

        if len(self.headers) == 0:
            raise EmptyHeadersException()

        return self.__csv_to_dict(self.headers, self.body)
    
    def parse_output(self):
        pass


    @classmethod
    def __csv_to_dict(self, headers:List, content:List)->List[Mapping]:
        out:List[Mapping] = []
        line:int = 2            
        for x in content:
            d:Mapping = dict()
            if not x:
                pass
            else:
                try:                    
                    for y in range(0, len(headers)):
                        d[headers[y]] = x[y]
                    out.append(d)
                except:
                    print("Impossible to parse line {}".format(line))
            line += 1
        return out