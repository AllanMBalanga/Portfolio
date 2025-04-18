from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)                                                          #initializes restful api
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"         #name of the database file to be created in the same directory/file
db = SQLAlchemy(app)

#creating database, use db.create_all() only once, delete or comment it out after
class VideoModel(db.Model):                                             #VideoModel interacts with the database
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)                   #must have value
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(title = {self.title}, views = {self.views}, likes = {self.likes})"

#defines the expected arguments for creating or replacing a video (post, put, patch).
video_put_args = reqparse.RequestParser()                                                     #creates a RequestParser() object to validate and extract data from incoming requests.
video_put_args.add_argument("title", type=str, help="Invalid title", required=True)     #add_argument() - Defines rules for each field in the request
video_put_args.add_argument("views", type=int, help="Invalid views", required=True)
video_put_args.add_argument("likes", type=int, help="Invalid likes", required=True)

#not required arguments for update(patch)
update_args = reqparse.RequestParser()
update_args.add_argument("title", type=str, help="Invalid title")
update_args.add_argument("views", type=int, help="Invalid views")
update_args.add_argument("likes", type=int, help="Invalid likes")


resource_fields = {                             #response formatting - Defines how VideoModel objects are serialized to JSON when returned to the client.
    "id": fields.Integer,
    "title": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

class Videos(Resource):                                                       #Resource - Base class that enables HTTP method handling.
    @marshal_with(resource_fields)                                            #automatically formats the output of API endpoints using resource_fields
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()              #gets the first video inside VideoModel that has id=video_id
        if not result:
            abort(404, message="Could not find video with that id")
        return result


    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_put_args.parse_args()                                    #gets all the arguments created earlier using add_argument()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")

        video = VideoModel(id=video_id, title=args["title"], views=args["views"], likes=args["likes"])
        db.session.add(video)                                                #adds video to the database
        db.session.commit()
        return video, 201


    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = update_args.parse_args()                                     #gets all update_args
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")

        if args['name']:                                                    #updates the result if args have some of the following (name, views, likes)
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result


    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot delete")

        db.session.delete(result)                           # delete from database
        db.session.commit()                                 # Commit the changes
        return '', 204

api.add_resource(Videos, "/videos/<int:video_id>")     #http://127.0.0.1:5000/videos/<int:video_id> - When a request comes to this URL, use this Resource class to handle it (Videos class).




# names = {"allan":{"gender":"male", "age": 23},
#          "lab":{"gender":"female","age": 23}}

# class HelloWorld(Resource):
#     def get(self,name):                                             #passes in the <> info from api.add_resource
#         return names[name]
#
#     def post(self, name, age):
#         return {'data': name, "age": age}

# api.add_resource(HelloWorld, "/hello/<string:name>")

# videos = {}
#
# def abort_if_not_video(video_id):
#     if video_id not in videos:
#         abort(404, message="Video ID not valid")
#
# def abort_if_video(video_id):
#     if video_id in videos:
#         abort(409,message="Video already exists")
#
# class Videos(Resource):
#     def get(self, video_id):
#         abort_if_not_video(video_id)
#         return videos[video_id]
#
#     def put(self, video_id):
#         abort_if_video(video_id)
#         args = video_put_args.parse_args()                      #gets all the arguments created earlier using add_argument()
#         videos[video_id] = args
#         return videos[video_id], 201
#
#     def delete(self, video_id):
#         abort_if_not_video(video_id)
#         del videos[video_id]
#         return '', 204
#
# api.add_resource(Videos, "/videos/<int:video_id>")



if __name__ == "__main__":
    app.run(debug=True)