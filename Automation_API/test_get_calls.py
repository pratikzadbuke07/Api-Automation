from helper import CommonHelper
import api_details
import pytest



@pytest.mark.get
def test_get_users():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_users']
    result=obj.get_api_validation(api,200)
    if result[0].is_success():
        assert 'Valide' in result[1],'Failed due to status code'
    else:
        pytest.fail('this tc is failed')

@pytest.mark.get
def test_current_url_users():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_users']
    result=obj.current_url_validation(api)
    if result[0].is_success():
        assert 'Valide' in result[1],'Failed due to current url'
    else:
        pytest.fail('this tc is failed')

@pytest.mark.get
def test_validate_last_name():
    obj = CommonHelper()
    api = api_details.dict_of_apis['get_users']
    result=obj.get_response(api)
    resp=obj.check_name(result,'Lawson')
    assert resp==True,'Name not found'

@pytest.mark.get
def test_single_user():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_single_user']
    result = obj.get_response(api)
    assert len(result['data'])>1,'Failed due to zero user'

@pytest.mark.get
def test_invalide_user():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_invalide_user']
    resp=obj.invalide_status_code(api)
    assert resp==True,'Failed due to status code'

@pytest.mark.get
def test_list_of_resouces_statuscode():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_list_resource']
    resp=obj.get_api_validation(api,200)
    if resp[0].is_success():
        assert True

@pytest.mark.get
def test_list_of_resouces_status():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_list_resource']
    resp=obj.get_response(api)
    if type(resp['data'])==list and len(resp['data'])>1:
        assert True,'list not found'

@pytest.mark.get
def test_name_list_of_resouces():  #"year": 2000
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_list_resource']
    resp=obj.get_response(api)
    for i in range(len(resp['data'])):
        if (resp['data'][i]['year']) == 2000:
            assert (resp['data'][i]['name'])=='cerulean','Failed'

@pytest.mark.get
def test_resource_not_found():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_resouce_not_found']
    resp=obj.invalide_status_code(api)
    assert resp==True,'Failed due to status code'

@pytest.mark.get
def test_validate_delay():
    obj=CommonHelper()
    api=api_details.dict_of_apis['get_delay_response']
    resp=obj.get_response(api,True)
    assert resp>=3,'Failed due to response time'
