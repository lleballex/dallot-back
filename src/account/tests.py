from django.test import TestCase

from .serializers import CreateUserSerializer
from .models import User


class CreateUserTest(TestCase):
	def test_create_user_by_serializer(self):
		seralizer = CreateUserSerializer(data={
			'username': 'username',
			'password': 'asdfasdfas72343',
			'email': 'email@email.ru'
			})
		self.assertTrue(seralizer.is_valid(raise_exception=True))
		seralizer.save()

	def test_create_user_by_url(self):
		response = self.client.post('/api/account/create_user/', {
			'username': 'username',
			'password': 'sodifasf7yarywr232123',
			'email': 'email@email.ru'
			})
		print(response.json())
		self.assertEqual(response.status_code, 201)