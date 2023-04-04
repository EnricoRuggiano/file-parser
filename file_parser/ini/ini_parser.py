from ..abstract import ParserInterface
from ..exceptions import *
from ..commons import *
from typing import Mapping, List, Any

import configparser
from configparser import ConfigParser

class IniParser(ParserInterface):      
    format = 'ini'
    config:Union[ConfigParser, None]

    def __init__(self):
        super().__init__()

    def parse_input(self) -> Mapping:
        check_is_not_null(self.raw_content)
        check_is_str(self.raw_content)

        self.config = ConfigParser()
        self.config.read_string(self.raw_content)
        
        out: Mapping = IniParser.__cfg_to_dict(self.config)
        del self.config

        return out
    
    def parse_output(self):
        pass

    @classmethod
    def __cfg_to_dict(self, cfg:ConfigParser)->Mapping:
        sections:List[str] = cfg.sections()
        out:Mapping = dict()
        for s in sections:
            d:Mapping = dict() 
            for k, v in cfg[s].items():
                d[k] = v
            out[s] = d
        return out