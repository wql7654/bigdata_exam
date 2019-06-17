from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'lee'}

api.add_resource(HelloWorld,'/oh') # 주소뒤쪽에 붙일 이름(태그 http://218.51.230.241:5000/oh)

if __name__ ==  '__main__':
    app.run(host='218.51.230.241')

