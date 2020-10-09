import os
import unittest
import json
import pdb
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class CastingTestCase(unittest.TestCase):
    """This class represents the Castingagency test case"""
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'Admin123','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        
        self.new_actor = {
            'name': 'Leonardo dicaprio', 
            'age': '44',
            'gender': 'male'
        }
        self.new_movie = {
            'title': 'Inception', 
            'release_date': '2010-11-01'
        }
    

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    '''
     GET /actors and /movies
    '''
    def test_get_actors(self):
        res = self.client().get('/actors')
        print(res)
        # data = json.loads(res.data)
        # print(data)

        # self.assertEqual(res.status_code, 200)
        # self.assertEqual(data['success'], True)
        # self.assertTrue(data['actors'])
 
    # def test_failed_get_actors(self):
    #     res = self.client().get('/actors?page=15')
    #     data = json.loads(res.data)
        
    #     self.assertEqual(res.status_code, 200)
    #     self.assertFalse(data['actors'])
    #     self.assertEqual(data['success'], True)

    # def test_get_movies(self):
    #     res = self.client().get('/movies')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['movies'])
    #     self.assertTrue(len(data['movies']))

    # def test_failed_get_movies(self):
    #     res = self.client().get('/movies')
    #     data = json.loads(res.data)
    #     # pdb.set_trace()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['movies'])
    #     self.assertFalse(len(data['movies']) > 10)
    # '''
    #  DELETE /actors and /movies
    # '''
    # def test_delete_actors(self):
    #     res = self.client().delete('/actors/14')
    #     data = json.loads(res.data)
    #     quest = Actor.query.filter(Actor.id == 14).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['actorid'], 14)

    # def test_failed_delete_actors(self):
    #     res = self.client().delete('/actors/1')
    #     data = json.loads(res.data)
    #     quest = Actor.query.filter(Actor.id == 1).one_or_none()

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Unprocessable')

    # def test_delete_movies(self):
    #     res = self.client().delete('/movies/13')
    #     data = json.loads(res.data)
    #     quest = Movie.query.filter(Movie.id == 13).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['movieid'], 13)

    # def test_failed_delete_movies(self):
    #     res = self.client().delete('/movies/1')
    #     data = json.loads(res.data)
    #     quest = Movie.query.filter(Movie.id == 1).one_or_none()

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Unprocessable')

    # '''
    #  POST /actors and /movies
    # '''
    # def test_create_actors(self):
    #     res = self.client().post('/actors', json=self.new_actor)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])

    # def test_failed_create_actors(self):
    #     res = self.client().post('/actors/40', json=self.new_actor)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_create_movies(self):
    #     res = self.client().post('/movies', json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])

    # def test_failed_create_movies(self):
    #     res = self.client().post('/movies/40', json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # '''
    # PATCH /actors and /movies
    # '''

    # def test_update_actors(self):
    #     res = self.client().patch('/actors/11', json={'name': 'Al Pacino Sr', 'age': 40})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['actorid'])

    # def test_failed_update_actors(self):
    #     res = self.client().patch('/actors/14', json={'name': 'Al Pacino Sr', 'age': 40})
    #     data = json.loads(res.data)
    #     print(data)

    #     self.assertEqual(res.status_code, 404)
    #     # self.assertFalse(data['question'])
    #     self.assertEqual(data['actorid'], False)

    # def test_update_movies(self):
    #     res = self.client().patch('/movies/4', json={'release_date': '1999-08-01'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['movieid'])

    # def test_failed_update_movies(self):
    #     res = self.client().patch('/movies/14', json={'release_date': '1999-08-01'})
    #     data = json.loads(res.data)
    #     print(data)

    #     self.assertEqual(res.status_code, 404)
    #     # self.assertFalse(data['question'])
    #     self.assertEqual(data['movieid'], False)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()