import requests
import api_details
import libs_constant
from json_builder import BuildJsonData
import json

from TaskCheck import TaskStatus
class CommonHelper:
    def __init__(self):
        self.start=libs_constant.StatusCode.api_start
        self.json_obj=BuildJsonData()
    def get_api_validation(self,api,exp_status):
        try:
            resp=requests.get(self.start+api)
            if resp.status_code==exp_status:
                return TaskStatus.success(),'Valide Code'
            else:
                return TaskStatus.error('this is failed due to status code')
        except Exception as e:
            print(str(e))
    def current_url_validation(self,api):
        try:
            resp=requests.get(self.start+api)
            if api in resp.url:
                return TaskStatus.success(),'Valide API'
            else:
                return TaskStatus.error('this is failed due url')
        except Exception as e:
            print(str(e))
    def get_response(self,api,time_req=None):
        try:
            resp=requests.get(self.start+api)
            if time_req:
                return resp.elapsed.total_seconds()
            result=json.loads(resp.content)
            return result
        except Exception as e:
            print(str(e))
    def check_name(self,result,name):
        try:
            for i in range(len(result['data'])):
                if result['data'][i]['last_name']==name:
                    return True
                else:
                    return False
        except Exception as e:
            print(str(e))

    def invalide_status_code(self,api):
        try:
            resp=requests.get(self.start+api)
            if resp.status_code==libs_constant.StatusCode.invalide_msg:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))

    def post_data(self,api,register=None):
        try:
            name=libs_constant.StatusCode.name
            job=libs_constant.StatusCode.job
            email=libs_constant.StatusCode.email
            password=libs_constant.StatusCode.password
            if register:
                payload = self.json_obj.data_for_register(email, password)
            else:
                payload=self.json_obj.data_for_use(name,job)
            resp=requests.post(self.start+api,payload)
            if resp.status_code==libs_constant.StatusCode.created_msg:   #201
                return TaskStatus.success(),'Created'   #tuple[0],[1]
            else:
                return TaskStatus.error('Data is not created')
        except Exception as e:
            print(str(e))


    def post_data_unregister(self,api):
        try:
            payload=self.json_obj.data_unregister()
            resp=requests.post(self.start+api,payload)
            if resp.status_code==400:   #201
                return TaskStatus.success(),'Not Created'   #tuple[0],[1]
            else:
                return TaskStatus.error('Data is not created')
        except Exception as e:
            print(str(e))


    def post_data1(self,api):
        try:

            payload=self.json_obj.login_data()
            resp=requests.post(self.start+api,payload)
            if resp.status_code==201:   #201
                return TaskStatus.success(),'Created'   #tuple[0],[1]
            else:
                return True,TaskStatus.error('Data is not created')
        except Exception as e:
            print(str(e))

    def update_data(self,api,expected_Resp=None):
        payload=self.json_obj.update_data()
        resp=requests.put(self.start+api,json.dumps(payload))
        if expected_Resp:
            return resp
        if resp.status_code==libs_constant.StatusCode.success_msg:
            return True
        else:
            return False









if __name__=='__main__':   #current python module will consider as main module
    obj=CommonHelper()
    url=api_details.dict_of_apis['get_users']
    obj.post_data()
