import pytest
from file_parser import FileParser

def test_xml_is_a_dict(xml_file:str):
    f = FileParser()
    f.read(xml_file)
    res = f.parse('xml')
    print(res)
    assert isinstance(res, dict)
    assert len(res['EmployerData']) == 4
    
def test_xml_values(xml_file:str):
    f = FileParser()
    f.read(xml_file)
    res = f.parse('xml')

    assert res["EmployerData"][0]['userName']  == 'booker12'
    assert res["EmployerData"][0]['firstName'] == 'Rachel'
    assert res["EmployerData"][0]['lastName']  == 'Booker'
