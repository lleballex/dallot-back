from django.contrib.sitemaps import Sitemap

from dallot.settings import SITEMAP_URLS

from .models import Post


post_url = SITEMAP_URLS['POSTS']


class PostsSitemap(Sitemap):
	changefreq = 'daily'

	def items(self):
		return Post.objects.all()

	def location(self, item):
		return post_url.replace(':id', str(item.id))