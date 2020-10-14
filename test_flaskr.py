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
        self.testing = True
        self.database_name = "casting_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'Admin123','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
    
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.casting_assistant_auth_header = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImR5WEhRQThHUm1LSTI4SXozWWlJVCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kbmFuby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY1MmNjZWJjNjQ3OGIwMDY3ZDkxMjA1IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwMjcxNTA5MCwiZXhwIjoxNjAyODAxNDkwLCJhenAiOiJZeEo4Nkxoa0luN2NyWkNkMm9NRVpwcTV3Ykt4VzVMTCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.OG32HjVY1fRyBEExUklJEFWMasaZrm2mkqew-Es6BbfCGbL-r_yNBEqtRVCitQhUpt4W_tQzEupWl3cpD62T_R5gWKddwXquqMlljHjWuDcv-AXyyZM84Orj3PJTa2rVGXmn8KB5YzU9cfBvxuVGl1gkHs7tSsAJss43xnQMJ5GlCkJEtC735lcDJuWf8lXRdnKkr3u_tm9geVicUVjumDXxp5vngjqXDMVA3wvhuS-vm6tYP9w7Zgk_rP8tEjFg5dwnbe16HROMkaL_0DgpZM9-HHv2ti38xRr8vU04Zm8qX9w34zzC9h06OVBHByLyLo5a0-HCkwA-aKVFeJkuFg'
        self.casting_director_auth_header = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImR5WEhRQThHUm1LSTI4SXozWWlJVCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kbmFuby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY1MmNjYjRlOWVmNWYwMDY3YjY1MWRhIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwMjcxNTI0OCwiZXhwIjoxNjAyODAxNjQ4LCJhenAiOiJZeEo4Nkxoa0luN2NyWkNkMm9NRVpwcTV3Ykt4VzVMTCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.PsCBbBGeG6csT6pUdtH7uQBZXh-OE5d1brSMlLZGHsx2lePIqVjPLR2l6d90n4QffKJ_c7i-XgQ7Uh4XmNyqYiZCfPBU4KrQ1w6ayGDvC60_JD6LTjFkmSx3zo7Jjebzalewm3Y80j7xhSYd0mLyIWEenf6iuMnB0XH33Y21PsVC_TyWgxbmJPrwduB0UZcDNgu8NSBUDY452LlqA6KEhX8BbvY2J44YxbC-iDClDxCQ9cseX2fWKLkjp8JUpyKa7G7NBxgR4YQJ3f-AQpkqV6B7ndYwdp8vBYs9vsPgYtkq5ePH2l0Pz2FDBEMny1UNkgLMVoWoxNurcpGHQog5uw'
        self.casting_exeproducer_auth_header = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImR5WEhRQThHUm1LSTI4SXozWWlJVCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mc25kbmFuby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3YmJmMTRiNDk4ZTIwMDZiOTQ1ZDNmIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwMjcxNTQ1MSwiZXhwIjoxNjAyODAxODUxLCJhenAiOiJZeEo4Nkxoa0luN2NyWkNkMm9NRVpwcTV3Ykt4VzVMTCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.pYDkmXF6xIvOrigVI6j_uu5eUzbdRZxvQQW8mqWZYO4k4iXUHLJKfWI3OOeied0aLfo2KDpR0b4yxvIfyvuSSahcdpl7bFS7U5Uf11hkCAyVnQZp8HfamFN1k0byyC-LgDGlXVI7e42VgaQKkDmdhNG-FnDrybRFxt15R0jIKlIRvkNhgZc0eriG2BzBxRKHVeNNFywIkag5LlhhEm8Vvx22f8p6n4GRaYMbu7yXMcIxYb_BU2P7OgUPK-npDA--XVSGONKZAeW1MP-nRwEed99q5ua-rW_HIOWjyT3ptKfjDtRu846rfyEOSc6mQdukjwt3-OUY-bQcTWuFNy_0fQ'

        self.new_actor = {
            'id': '6',
            'name': 'Leonardo dicaprio', 
            'age': '44',
            'gender': 'male'
        }
        self.new_movie = {
            'id': '7',
            'title': 'Inception', 
            'release_date': '2010-11-01'
        }

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
        res = self.client().get('/actors', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
 
    def test_failed_get_actors_401(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        print(data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_get_movies(self):
        res = self.client().get('/movies', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_failed_get_movies(self):
        res = self.client().get('/movies',headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertFalse(len(data['movies']) > 25)
    '''
     DELETE /actors and /movies
    '''
    def test_delete_actors(self):
        res = self.client().delete('/actors/14', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header})
        print(res)
        data = json.loads(res.data)
        quest = Actor.query.filter(Actor.id == 14).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actorid'], 14)

    def test_failed_delete_actors(self):
        res = self.client().delete('/actors/50', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header})
        data = json.loads(res.data)
        quest = Actor.query.filter(Actor.id == 50).one_or_none()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertEqual(data['success'], False)

    def test_delete_movies(self):
        res = self.client().delete('/movies/20', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header})
        data = json.loads(res.data)
        quest = Movie.query.filter(Movie.id == 20).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movieid'], 20)

    # Using RBAC ROLE testing here ,casting Assistant  doesnt have permission to delete a field.
    def test_failed_delete_movies(self):
        res = self.client().delete('/movies/10', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)
        quest = Movie.query.filter(Movie.id == 10).one_or_none()

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    '''
     POST /actors and /movies
    '''
    def test_create_actors(self):
        res = self.client().post('/actors', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # def test_post_actor_400(self):
    #     res = self.client().post('/actors', json={'name': '', 'age': '', "gender": ""}, headers={'Authorization':  'Bearer ' + self.casting_director_auth_header})
    #     data = json.loads(res.data)
    #     print(data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Bad Request, pls check your inputs')

    def test_create_movies(self):
        res = self.client().post('/movies', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # using RBAC ROLE testing here ,casting assitant doesnt have permission to create new field.
    def test_failed_create_movies_403(self):
        res = self.client().post('/movies', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header}, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')
      

    # '''
    # PATCH /actors and /movies
    # '''

    def test_update_actors(self):
        res = self.client().patch('/actors/16', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json={'name': 'Al Pacino Sr', 'age': 40})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actorid'])

    # using RBAC ROLE testing here ,casting Exceutive producer doesnt have permission to update a field.
    def test_failed_update_actors_403(self):
        res = self.client().patch('/actors/14',headers = {'Authorization':  'Bearer ' + self.casting_exeproducer_auth_header}, json={'name': 'Al Pacino Sr', 'age': 40})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')
    
    def test_update_movies(self):
        res = self.client().patch('/movies/4', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json={'release_date': '1999-08-01'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movieid'])

    # Trying to Update a field/row which is not available in DB.
    def test_failed_update_movies_422(self):
        res = self.client().patch('/movies/25', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json={'release_date': '1999-08-01'})
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertEqual(data['success'], False)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
    app.run()