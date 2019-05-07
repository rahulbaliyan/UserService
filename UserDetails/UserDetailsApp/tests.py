from django.test import TestCase
from django.test import Client
from django.urls import reverse
from UserDetailsApp.serializer import UserSerializer
# Create your tests here.
class UserGetAllRecordTest(TestCase):
    def test_user(self):
        c = Client()
        response = c.get(reverse('users'))
        response = response.status_code
        print(response)
        self.assertEqual(response, 200)


class CreateUserTest(TestCase):
    def test_user_create(self):
        c = Client()
        data =  {'ass':1}
        response = c.post('/api/users/',data)
        serializer = UserSerializer(data=data)
        # response = response.status_code
        self.assertEqual(serializer.is_valid(), True)


class UserSelectionTest(TestCase):
    def test_user_based_on_query_parameter(self):
        c = Client()
        request_parameters = {'page': 1,
                              'limit': 2,
                              'sort': '-age',
                              'name': 'ra'}
        response = c.get('/api/users/1/', request_parameters)
        response = response.status_code
        self.assertEqual(response, 200)