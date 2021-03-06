from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	"""Manager for User model"""

	def create_user(self, username, email, password):
		if not email:
			raise ValueError('User must have an email address')
		if not username:
			raise ValueError('User must have a username')

		user = self.model(username = username, email = self.normalize_email(email))
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, username, email, password):
		user = self.create_user(username = username, email = email, password = password)
		user.is_staff = True
		user.is_admin = True
		user.is_superuser = True
		user.save(using = self._db)
		return user


class User(AbstractBaseUser):
	"""Model of user"""

	username = models.CharField(max_length = 30, unique = True)
	email = models.EmailField(max_length = 30, unique = True)
	name = models.CharField(max_length = 30, null = True, blank = True)
	image = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d/users/')
	about = models.CharField(max_length=200, null=True, blank=True)
	date_joined = models.DateField(auto_now_add = True)
	is_staff = models.BooleanField(default = False)
	is_admin = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	class Meta:
		ordering = ['-date_joined']

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj = None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True