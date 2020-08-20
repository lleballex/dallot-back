from django.contrib.sitemaps import Sitemap

from dallot.settings import SITEMAP_URLS

from .models import User


user_url = SITEMAP_URLS['USERS']


class UsersSitemap(Sitemap):
	changefreq = 'daily'

	def items(self):
		return User.objects.all()

	def location(self, item):
		return user_url.replace(':username', str(item.username))