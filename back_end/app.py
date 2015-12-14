from flask import Flask 
from flask_restful import Resource, Api
from icloud import ICloud
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)



class ICloudChecker(Resource):
	def get(self, imei):
		phone_information = ICloud().get_details('http://iphoneimei.info', {'imei': imei})
		return phone_information

api.add_resource(ICloudChecker, '/<string:imei>')

if __name__ == '__main__':
	app.run(debug=True)