import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  return app

app = create_app()
db = SQLAlchemy(app)

'''
  GET /actors and /movies
'''

@app.route('/actors',methods=['GET'])
@requires_auth('get:movies')
def get_actors(jwt):
  try:
    actorsall = Actor.query.all()
    actorslist = [actor.format() for actor in actorsall]
    if len(actorslist) == 0:
          abort(404)
    return jsonify({
      'success': True,
      'actors': actorslist
    })
  except:
    abort(400)

@app.route('/movies',methods=['GET'])
@requires_auth('get:movies')
def get_movies(jwt):
  try:
    moviesall = Movie.query.all()
    movielist = [movie.format() for movie in moviesall]
    if len(movielist) == 0:
          abort(404)
    return jsonify({
      'success': True,
      'movies': movielist
    })
  except:
    abort(404)

'''
  POST /actors and /movies
'''

@app.route('/movies',methods=['POST'])
@requires_auth('post:movies')
def new_movies(jwt):
  body = request.get_json()
  newtitle = body.get('title',None)
  newrelease = body.get('release_date', None)
  try:
    entry = Movie(title=newtitle, release_date=newrelease)
    entry.insert()
    db.session.commit()
    moviesall = Movie.query.all()
    movielist = [movie.format() for movie in moviesall]
    return jsonify({
      'success': True,
      'movies': movielist
    })
  except:
    abort(422)

@app.route('/actors',methods=['POST'])
@requires_auth('post:actors')
def new_actors(jwt):
  body = request.get_json()
  newname = body.get('name',None)
  newage = body.get('age', None)
  newgender = body.get('gender', None)
  try:
    entry = Actor(name=newname, age=newage, gender=newgender)
    entry.insert()
    actorsall = Actor.query.all()
    actorslist = [actor.format() for actor in actorsall]
    return jsonify({
      'success': True,
      'actors': actorslist
    })
  except:
    abort(422)

'''
  DELETE /actors and /movies
'''
@app.route('/movies/<int:movie_id>',methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(jwt,movie_id):
  movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
  try:
    if movie is None:
      abort(404)
    else:
      movie.delete()
      return jsonify({
        'success': True,
        'movieid': movie_id
      })
  except:
    abort(422)

@app.route('/actors/<int:actor_id>',methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(jwt,actor_id):
  actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
  try:
    if actor is None:
      abort(404)
    else:
      actor.delete()
      return jsonify({
        'success': True,
        'actorid': actor_id
      })
  except:
    abort(422)

'''
  PATCH /actors and /movies
'''

@app.route('/movies/<int:movie_id>',methods=['PATCH'])
@requires_auth('patch:movies')
def update_movies(jwt,movie_id):
  movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
  try:
    if movie is None:
      abort(404)
    else:
      body = request.get_json()
      movie.release_date = body.get('release_date', None)
      movie.update()
      return jsonify({
        'success': True,
        'movieid': movie_id
      }),200
  except:
    abort(422)

@app.route('/actors/<int:actor_id>',methods=['PATCH'])
@requires_auth('patch:actors')
def update_actors(jwt,actor_id):
  actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
  try:
    if actor is None:
      abort(404)
    else:
      body = request.get_json()
      actor.name = body.get('name', None)
      actor.age = body.get('age', None)
      actor.update()
      return jsonify({
        'success': True,
        'actorid': actor_id
      }),200
  except:
    abort(422)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

@app.errorhandler(404)
def resource_not_found(error):
      return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
      }), 404

@app.errorhandler(500)
def unprocessable(error):
      return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
      }), 500