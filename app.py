from flask import Flask, jsonify
from flask_restful import Resource, Api,request
from scrappers.sprouts import sprouts

app = Flask(__name__)
api = Api(app)


class home(Resource):
    def get(self):
        return jsonify(
            {
                'Message': 'crawlandscrap is running',
                'description': 'check api documentation for details',
                'status': 200
            }
        )

class get_item(Resource):
    def get(self):
        args = request.args
        if args is None:
            return jsonify({'error': 'Missing keyword'})
        else:
            keyword = str(args['keyword'])
        return jsonify(sprouts(keyword))
    
api.add_resource(home, '/')
api.add_resource(get_item, '/get_item')

if __name__ == "__main__":
	app.run(debug=True)
