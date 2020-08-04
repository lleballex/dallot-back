from django.test import TestCase

from account.models import User

from .models import Post


class UpdatePostRatingTest(TestCase):
	@classmethod
	def setUpTestData(self):
		user = User.objects.create(username='username', password='password',
								   email='email@yandex.ru')
		self.post = Post.objects.create(user=user, title='Test post', content='Test post')

	def test_drop_post_rating(self):
		response = self.client.post(f'/api/posts/{self.post.id}/drop_rating/')
		print(self.post.id)
		print(response.status_code)


'''class PostRatingTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		user = User.objects.create(username='username', password='password',
								   email='email@yandex.ru')
		Post.objects.create(user=user, title='Test post', content='Test post')

	def setUp(self):
		self.post = Post.objects.get(id=1)

	def test_drop_post_rating(self):
		rating = self.post.drop_rating(self.post.user)
		self.assertEquals(rating, -1)

	def test_raise_post_rating(self):
		rating = self.post.raise_rating(self.post.user)
		self.assertEquals(rating, 1)

	def test_drop_and_restore_post_rating(self):
		self.post.drop_rating(self.post.user)
		rating = self.post.restore_rating(self.post.user)
		self.assertEquals(rating, 0)

	def test_raise_and_restore_post_rating(self):
		self.post.raise_rating(self.post.user)
		rating = self.post.restore_rating(self.post.user)
		self.assertEquals(rating, 0)

	def test_double_drop_rating(self):
		self.post.drop_rating(self.post.user)
		rating = self.post.drop_rating(self.post.user)
		self.assertFalse(rating)

	def test_double_raise_rating(self):
		self.post.raise_rating(self.post.user)
		rating = self.post.raise_rating(self.post.user)
		self.assertFalse(rating)

	def test_double_restore_rating(self):
		self.post.restore_rating(self.post.user)
		rating = self.post.restore_rating(self.post.user)
		self.assertFalse(rating)


class CreatePostTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		User.objects.create(username='username', password='password',
							email='email@yandex.ru')

	def test_create_post(self):
		user = User.objects.get(id=1)
		serializer = UpdatePostSerializer(data={'user': user.id, 'title': 'Test post',
										  'content': 'Test post'})
		self.assertTrue(serializer.is_valid())
		serializer.save()


class UpdateBookmarksTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		user = User.objects.create(username='username', password='password',
								   email='email@yandex.ru')
		Post.objects.create(user=user, title='Test post', content='Test post')

	def setUp(self):
		self.post = Post.objects.get(id=1)

	def test_bookmark_post(self):
		result = self.post.add_to_bookmarks(self.post.user)
		self.assertEquals(result, 1)
		self.assertTrue(self.post.user in self.post.bookmark_users.all())

	def test_remove_post_from_bookmarks(self):
		result = self.post.remove_from_bookmarks(self.post.user)
		self.assertEquals(result, 0)
		self.assertFalse(self.post.user in self.post.bookmark_users.all())'''