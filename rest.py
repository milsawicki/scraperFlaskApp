
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask import abort

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'filmweb_base'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/filmweb_base'

mongo = PyMongo(app)

@app.route('/movies', methods=['GET'])
def get_all_movies():
  movies = mongo.db.movies
  output = []
  for movie in movies.find():
    output.append({'title' : movie['title'], 'title_pl' : movie['title_pl'],
                   'image' : movie['image'], 'director' : movie['director'],
                   'year' : movie['year'], 'plot' : movie['plot'], 'genres' : movie['genres']})
  return jsonify({'movies' : output})

@app.route('/movie', methods = ["GET"])
def get_one_movie():

  title = request.headers.get("title")
  movies = mongo.db.movies
  movie = movies.find_one({'title': title})
  if movie:
    output = {'title' : movie['title'], 'title_pl' : movie['title_pl'],
                   'image' : movie['image'], 'director' : movie['director'],
                   'year' : movie['year'], 'plot' : movie['plot'], 'genres' : movie['genres']}
  else:
    abort(400)
  return jsonify(output)

if __name__ == '__main__':
  app.run(debug=True)