from flask import Flask, request
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form['likes'])
        return {}

api.add_resource(Video, "/video/<int:video_id>")

# names = {"tim": {"age": 19, "gender": "male"},
#          "ben": {"age": 14, "gender": "male"}}
#
#
# class HelloWorld(Resource):
#     def get(self, name):
#         return {name: names[name]}

    # def get(self, name, test):
    #     return {"name": name, "test": test}
    # # def post(self):
    #     return {"data": "Posted"}

# api.add_resource(HelloWorld, "/")
# api.add_resource(HelloWorld, "/<string:name>/<int:test>")


# api.add_resource(HelloWorld, "/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
