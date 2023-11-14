import os
import pytest

def sample_file_path(ext:str)->str:
    return os.path.join('example', f'sample.{ext}')

@pytest.fixture
def csv_file():
    return sample_file_path('csv')

@pytest.fixture
def ini_file():
    return sample_file_path('ini')

@pytest.fixture
def json_file():
    return sample_file_path('json')

@pytest.fixture
def xlsx_file():
    return sample_file_path('xlsx')

@pytest.fixture
def xml_file():
    return sample_file_path('xml')