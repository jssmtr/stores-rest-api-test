from models.user import UserModel
from tests.base_test import BaseTest
import json

class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context(): #allow to save things to database and retreive from it
                response = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(response.status_code, 201) # Estado success de Post en resources.user
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully'},
                                     json.loads(response.data))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context(): #allow to save things to database and retreive from it
                client.post('/register', data={'username': 'test', 'password': '1234'})
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_request.data).keys())


    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context(): #allow to save things to database and retreive from it
                client.post('/register', data={'username': 'test', 'password': '1234'})
                response = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message':'A user with that username already exists'}, json.loads(response.data))
