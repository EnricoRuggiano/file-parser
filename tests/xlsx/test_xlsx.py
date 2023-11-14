import pytest
from file_parser import FileParser

def test_xlsx_is_list(xlsx_file:str):
    f = FileParser()
    f.read(xlsx_file)
    res = f.parse('xlsx')
    assert isinstance(res, list)
    assert len(res) == 5
    
def test_xlsx_values(xlsx_file:str):
    f = FileParser()
    f.read(xlsx_file)
    res = f.parse('xlsx')

    assert res[0]['Username']   == 'booker12'
    assert res[0]['Identifier'] == '9012'
    assert res[0]['First name'] == 'Rachel'
    assert res[0]['Last name']  == 'Booker'
