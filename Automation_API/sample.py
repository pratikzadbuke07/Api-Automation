import requests
import json
resp=requests.get('https://www.amazon.in/')

print(resp.content)