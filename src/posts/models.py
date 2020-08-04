from django.db import models

from account.models import User


class Post(models.Model):
	"""Model of post (article)"""

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	title = models.CharField(max_length=250)
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	views = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	dropped_rating_users = models.ManyToManyField(User, blank=True, related_name='dropped_posts', verbose_name='users who dropped the rating')
	raised_rating_users = models.ManyToManyField(User, blank=True, related_name='raised_posts', verbose_name='users who raised the rating')
	bookmarked_users = models.ManyToManyField(User, blank=True, related_name='bookmarked_posts', verbose_name='users who bookmarked the post')

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.title

	def drop_rating(self, user):
		if user in self.dropped_rating_users.all():
			return False
		if user in self.raised_rating_users.all():
			self.raised_rating_users.remove(user)
			self.rating -= 1

		self.dropped_rating_users.add(user)
		self.rating -= 1
		self.save()
		return self.rating

	def raise_rating(self, user):
		if user in self.raised_rating_users.all():
			return False
		if user in self.dropped_rating_users.all():
			self.dropped_rating_users.remove(user)
			self.rating += 1

		self.raised_rating_users.add(user)
		self.rating += 1
		self.save()
		return self.rating

	def restore_rating(self, user):
		if user in self.raised_rating_users.all():
			self.raised_rating_users.remove(user)
			self.rating -= 1
			self.save()
			return self.rating
		if user in self.dropped_rating_users.all():
			self.dropped_rating_users.remove(user)
			self.rating += 1
			self.save()
			return self.rating
		return False

	def add_to_bookmarks(self, user):
		if user in self.bookmarked_users.all():
			return False
		self.bookmarked_users.add(user)
		self.save()
		return self.bookmarked_users.count()

	def remove_from_bookmarks(self, user):
		if not user in self.bookmarked_users.all():
			return False
		self.bookmarked_users.remove(user)
		self.save()
		return self.bookmarked_users.count()
