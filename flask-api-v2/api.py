from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class MyApi(Resource):
  def get(self):
    return {'Version':'2.0'}
api.add_resource(MyApi,'/')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
