import pytest
@pytest.fixture(autouse=True)
def setup_start_api():
    print('**** this is the starting of tc ****')
    yield
    print('*** ending of test case')