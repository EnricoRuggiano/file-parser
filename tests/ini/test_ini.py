import pytest
from file_parser import FileParser

def test_ini_is_dict(ini_file:str):
    f = FileParser()
    f.read(ini_file)
    res = f.parse('ini')
    assert isinstance(res, dict)

def test_ini_has_dict_as_children(ini_file:str):
    f = FileParser()
    f.read(ini_file)
    res = f.parse('ini')
    assert len(list(res.keys())) == 2

    for k in list(res.keys()):
        assert isinstance(res[k], dict)

def test_ini_keys_always_lower(ini_file:str):
    f = FileParser()
    f.read(ini_file)
    res = f.parse('ini')
    print(res['DEVICE1'])

    assert 'GEN REF FILE5' not in list(res["DEVICE1"].keys())
    assert 'GEN REF FILE5'.lower() in list(res["DEVICE1"].keys())

def test_ini_supports_only_string(ini_file:str):
    f = FileParser()
    f.read(ini_file)
    res = f.parse('ini')
    print(res['DEVICE1'])

    assert res["DEVICE1"]['GEN REF FILE5'.lower()] != 0
    assert isinstance(res["DEVICE1"]['GEN REF FILE5'.lower()], str)