from flask import Flask, jsonify, request
import csv 

all_movies = []
with open('movies.csv') as f : 
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data [1:]

liked_movies = []
unliked_movies = []
did_not_watched_movies = []

app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status" : "success"
    })

@app.route("/liked-movies",methods = ["POST"])
def liked_movie():
    movies = all_movies[0],
    all_movies = all_movies[1:]
    liked_movies.append(movies)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/unliked-movies",methods = ["POST"])
def unliked_movie():
    movies = all_movies[0],
    all_movies = all_movies[1:]
    unliked_movies.append(movies)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/did-not-watch-movies",methods = ["POST"])
def did_not_watched_movie():
    movies = all_movies[0],
    all_movies = all_movies[1:]
    did_not_watched_movies.append(movies)
    return jsonify({
        "status" : "success"
    }),201
if __name__ == "__main__":
    app.run()


