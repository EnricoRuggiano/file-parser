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
        self.headers = []
     
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
    
    def parse_output(self, output_path:str, _parsed_content, **kwargs):

        if type(_parsed_content) == list and type(_parsed_content[0]) == dict:
            self._list_of_dict_to_csv(_parsed_content, output_path, **kwargs)
        elif type(_parsed_content) == dict:
            self.dict_to_csv(_parsed_content, output_path, **kwargs)
        elif type(_parsed_content) == str:
            self.str_to_csv(_parsed_content, output_path, **kwargs)
        else:
            raise GenericException()

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
    

    @classmethod
    def _list_of_dict_to_csv(self, _parsed_content:List[Mapping], output_path:str, **kwargs):
        
        _headers = list(map(lambda x:str(x), list(_parsed_content[0].keys())))
        delimiter = kwargs.get('delimiter', ',')
        headers   = kwargs.get('headers') if kwargs.get('headers') is not None else _headers  

        f = open(output_path, 'w', newline='')
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(headers)
        
        for row in _parsed_content:
            _sorted_row = dict()
            for h in headers:
                _sorted_row[h] = row.get(h, None)
            
            values:List = list(_sorted_row.values())
            writer.writerow(values)

        f.close()        

    @classmethod
    def dict_to_csv(self, _parsed_content:Mapping, output_path:str, **kwargs):
        
        _headers = list(map(lambda x:str(x), list(_parsed_content.keys())))
        delimiter = kwargs.get('delimiter', ',')
        headers   = kwargs.get('headers') if kwargs.get('headers') is not None else _headers  

        f = open(output_path, 'w', newline='')
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(headers)

        _sorted_row = dict()
        for h in headers:
            _sorted_row[h] = _parsed_content.get(h, None)

        values:List = list(_sorted_row.values())
        writer.writerow(values)

        f.close()

    @classmethod
    def str_to_csv(self, _parsed_content:str, output_path:str, **kwargs):
        
        _headers = "Content"
        delimiter = kwargs.get('delimiter', ',')
        headers   = kwargs.get('headers') if kwargs.get('headers') is not None else _headers  

        f = open(output_path, 'w', newline='')
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow([headers])
        
        writer.writerow([_parsed_content])

        f.close()