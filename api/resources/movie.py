from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.movie import Movie
from models.user import User
from flask_restful import Resource


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json(force=True)
        user = User.objects.get(id=user_id)
        movie = Movie(**body, added_by=user)
        movie.save()
        user.update(push__movies=movie)
        user.save()
        id = movie.id
        return {'id': str(id)}, 200


class MovieApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        body = request.get_json(force=True)
        movie.update(**body)
        return '', 200

    def get(self, id):
        movie = Movie.objects.get(id=id).to_json()
        return Response(movie, mimetype="application/json", status=200)

    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        Movie.objects.get(id=id, added_by=user_id).delete()
        return '', 200
