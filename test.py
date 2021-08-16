import requests
import json
import time

#url = 'http://127.0.0.1:5000/'
#url = 'http://0.0.0.0:5000/'
#url="https://ott-recommender-app.eu-gb.mybluemix.net/"
#url = "https://sentiment-analysis-tan1-brash-sable-ir.eu-gb.mybluemix.net"
#url = "https://sentiment-analysis-tan-patient-possum-xv.eu-gb.mybluemix.net"
url = "https://sentiment-analysis-tan2-cheerful-oryx-jv.eu-gb.mybluemix.net"


#data = {"m_or_tv":"movie","age":"18+","imdb":7,"genre":["Drama"],"language":["English"],"impact_factor":[0.5,1.5,0.5,0.5,0.5]}
data="1"
j_data = json.dumps(data)
#headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
headers = {'content-type': 'content_type_value', 'Accept-Charset': 'UTF-8'}
#time.sleep(5)
#for i in range(14):
r = requests.post(url, data=data)
print(r.text)
#time.sleep(30)
#{"param1":jdata,"param2":impact_factor}