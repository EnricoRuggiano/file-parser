from ..abstract import ParserInterface
from ..exceptions import *
from ..commons import *

import json

class JsonParser(ParserInterface):      
    format = 'json'

    def parse_input(self):
        check_is_not_null(self.raw_content)
        check_is_str(self.raw_content)

        return json.loads(self.raw_content)
    
    def parse_output(self):
        pass