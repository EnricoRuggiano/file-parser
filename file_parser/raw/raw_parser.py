from ..abstract import ParserInterface
from ..exceptions import InvalidStringException

class RawParser(ParserInterface):      

    def parse_input(self):
        if self.raw_content is None or type(self.raw_content) != str:
            raise InvalidStringException
        return dict(value=self.raw_content, format='raw')
    
    def parse_output(self):
        pass