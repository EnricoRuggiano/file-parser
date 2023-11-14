import pytest
from file_parser import FileParser

def test_csv_is_list(csv_file:str):
    f = FileParser()
    f.read(csv_file)
    res = f.parse('csv')
    assert isinstance(res, list)
    assert len(res) == 5
    
def test_csv_values(csv_file:str):
    f = FileParser()
    f.read(csv_file)
    res = f.parse('csv')

    assert res[0]['Username']   == 'booker12'
    assert res[0]['Identifier'] == '9012'
    assert res[0]['First name'] == 'Rachel'
    assert res[0]['Last name']  == 'Booker'
