import pytest
from file_parser import FileParser

def test_json_parse_keys(json_file:str):
    f = FileParser()
    f.read(json_file)
    res = f.parse('json')

    assert '1'     in list(res.keys())
    assert 'two'   in list(res.keys())
    assert 'hello' in list(res.keys())
    assert 'mnnn'  in list(res.keys())

def test_json_parse_values(json_file:str):
    f = FileParser()
    f.read(json_file)
    res = f.parse('json')

    assert res["1"]     == 'this is something'
    assert res['two']   ==  2
    assert res['hello'] == 'ehila manson!'
    assert res['mnnn']  == None
