import json

class BuildJsonData:
    def data_for_use(self,name,job):
        data={"name": "{}".format(name),"job": "{}".format(job)}
        return json.dumps(data)

    def data_for_register(self,em,ps):
        data={"email": "{}".format(em),"password": "{}".format(ps)}
        return json.dumps(data)

    def data_unregister(self):
        data={"email": "sydney@fife"}
        return json.dumps(data)

    def login_data(self):
        data={
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
        return json.dumps(data)

    def update_data(self):
        data={"name": "morpheus",
    "job": "zion resident"}
        return data
