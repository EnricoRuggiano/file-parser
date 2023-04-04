from ..abstract import ParserInterface
from ..exceptions import *
from ..commons import *
from typing import Mapping

class XlsxParser(ParserInterface):      
    format = 'xlsx'

    def parse_input(self) -> Mapping:
        check_is_not_null(self.raw_content)
        check_is_str(self.raw_content)
        return dict(value=self.raw_content, format=self.format)
    
    def parse_output(self):
        pass