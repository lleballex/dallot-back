from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from posts.sitemap import PostsSitemap
from account.sitemap import UsersSitemap
from dallot.sitemap import PagesSitemap


sitemaps = {
	'posts': PostsSitemap,
	'users': UsersSitemap,
	'pages': PagesSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/account/', include('account.urls')),
    path('api/posts/', include('posts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
