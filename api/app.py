import os
from flask import Flask, request, Response
from database import initialize_db
from models.movie import Movie

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    'host': os.environ.get('DB')
}

initialize_db(app)


@app.route('/movies', )
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json(force=True)
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200


@app.route('/movies/<id>', methods=['GET'])
def get_movie(id):
    movie = Movie.objects.get(id=id).to_json()
    return Response(movie, mimetype="application/json", status=200)


@app.route('/movies/<id>', methods=['PUT'])
def update_movie(index):
    body = request.get_json(force=True)
    Movie.objects.get(id=id).update(**body)
    return '', 200


@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(index):
    Movie.objects.get(id=id).delete()
    return '', 200


app.run(host="0.0.0.0", debug=True)
