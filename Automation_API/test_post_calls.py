import json

from helper import CommonHelper
import api_details
import pytest
import requests

@pytest.mark.post
def test_create_user():
    obj=CommonHelper()
    api=api_details.post_apis['create_use']
    resp=obj.post_data(api)
    if resp[0].is_success():
        assert resp[1]=='Created','Failed due to data is not created'
    else:
        pytest.fail('Due to POST CALL')

@pytest.mark.post
def test_register_user():
    obj=CommonHelper()
    api=api_details.post_apis['registration']
    resp=obj.post_data(api,True)
    if resp[0].is_success():
        assert resp[1]=='Created','Failed due to data is not created'
    else:
        pytest.fail('Due to POST CALL')

@pytest.mark.post
def test_unsuccessful_register_user():
    obj=CommonHelper()
    api=api_details.post_apis['unregister']
    resp=obj.post_data_unregister(api)
    if resp[0].is_success():
        assert resp[1]=='Not Created','Failed due to data is not created'
    else:
        pytest.fail('Due to POST CALL')

@pytest.mark.post
def test_successful_login():
    obj=CommonHelper()
    api=api_details.post_apis['login_success']
    resp=obj.post_data1(api)
    if resp[0]:
        assert 'Data' in resp[1],'Failed due to data is not created'
    else:
        pytest.fail('Due to POST CALL')

@pytest.mark.update
def test_update_statuscode():
    api='api/users/2'
    obj = CommonHelper()
    resp=obj.update_data(api)
    assert resp==True,'Failed due to status code'

@pytest.mark.update
def test_update_resp():
    api='api/users/2'
    obj = CommonHelper()
    resp=json.loads(obj.update_data(api,expected_Resp=True).content)
    assert 'updatedAt' in resp,'Failed due not updated'

@pytest.mark.delete
def test_delete_call_statuscode():
    api='https://reqres.in/'+'api/users/2'
    resp=requests.delete(api)
    assert resp.status_code==204,'Failed due to status code'

@pytest.mark.delete
@pytest.mark.skip
def test_delete_call_resp():
    api='https://reqres.in/'+'api/users/2'
    resp=requests.delete(api)
    result=json.loads(resp.headers)
    value=result['Content-Length']
    assert value=='0','Failed due to status code'