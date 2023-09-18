from ..abstract import ParserInterface
from ..exceptions import *
from ..commons import *
from typing import Mapping
from io import StringIO
from io import BytesIO
import json
from os import access, R_OK
from os.path import exists
import os

'''
Take care there are a lot of vulnerability in the xml parsers
Check the documentation of https://pypi.org/project/defusedxml/
'''
from defusedxml.lxml import _etree, parse, fromstring

class XmlParser(ParserInterface):      
    format = 'xml'
    
    """
    Translating Xml to Json is not so simple and there are a lot of conventions. 
    We use the Parker convention because it produces clean json but it ignores the xml attributes.
    If you are curious, check here: http://wiki.open311.org/JSON_and_XML_Conversion/
    """
    convention = 'Parker'

    def __init__(self, **kwargs):
        if 'convention' in kwargs.keys():
            self.convention = kwargs['convention']
            
    def parse_input(self) -> Mapping:
        check_is_not_null(self.raw_content)
        check_is_bytes(self.raw_content)

        if self.convention == 'Parker':
            return self.__parker_parse(self.raw_content)
        else:
            raise InvalidXmlConventionOptArgException()
    
    def parse_output(self):
        pass

    @classmethod
    def __parker_parse(self, content:str)->Mapping:
        dom = parse(BytesIO(content), forbid_dtd=True, forbid_entities=True)

        # xslt
        __this_dir:List[str] = os.path.realpath(__file__).split(os.sep)[:-1]
        __this_dir:str = os.sep.join(__this_dir)
        xslt_path = os.sep.join([__this_dir, 'xml2json.xslt'])        
        xslt = parse(xslt_path, forbid_dtd=True, forbid_entities=True)

        # apply transformation
        transform = _etree.XSLT(xslt)
        newdom    = transform(dom)
        newdom    = str(newdom)

        # convert it to dict
        return json.load(StringIO(newdom))
