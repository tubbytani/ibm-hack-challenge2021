import import_ipynb
# import IPython as ip
# ip.enable_gui = lambda x: True
from mainfile import final
from flask import Flask, jsonify , request
#from werkzeug.utils import cached_property
from flask_restx import Api
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer
import json
import os 

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='APIs for Python Functions', validate=False)
#ns = api.namespace('platform', 'Returns the name of ott platform') 
#api.eu-gb.cf.cloud.ibm.com
@app.route('/', methods=['POST'])
@cross_origin(origin='*')
def func():
    string = json.loads(request.data)
    detail_analysis,winner = final(string) 
    return jsonify({"detail_analysis": detail_analysis,"winner":winner}) 
#port = os.getenv('VCAP_APP_PORT','8080')


if __name__ == "__main__": 
    #app.secret_key = os.urandom(12)
    #app.run(debug=True,host='0.0.0.0',port=port)
    #app.run(debug=True)
    app.run(debug=True,host='0.0.0.0')