from ..abstract import ParserInterface
from ..exceptions import *
from ..commons import *
from typing import Mapping

from io import StringIO
import csv

class CsvParser(ParserInterface):      
    format = 'csv'
    delimiter = ';'

    def parse_input(self) -> Mapping:
        check_is_not_null(self.raw_content)
        check_is_str(self.raw_content)

        f:StringIO = StringIO(self.raw_content)
        csv_file = open(f)

        return dict(value=self.raw_content, format=self.format)
    
    def parse_output(self):
        pass


    # @classmethod
    # def __csv_to_dict(self, cfg:ConfigParser)->Mapping:
    #     sections:List[str] = cfg.sections()
    #     out:Mapping = dict()
    #     for s in sections:
    #         d:Mapping = dict() 
    #         for k, v in cfg[s].items():
    #             d[k] = v
    #         out[s] = d
    #     return out