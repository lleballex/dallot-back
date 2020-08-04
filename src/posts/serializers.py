from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
	"""Serializer for getting post"""

	user = UserSerializer()
	#dropped_rating_users = UserSerializer(many=True)
	#raised_rating_users = UserSerializer(many=True)
	#bookmarked_users = UserSerializer(many=True)

	class Meta:
		model = Post
		fields = ['id', 'user', 'title', 'content', 'date_created', 'views', 'rating',
				  'dropped_rating_users', 'raised_rating_users', 'bookmarked_users']


class UpdatePostSerializer(serializers.ModelSerializer):
	"""Serializer for creating or updating post"""

	class Meta:
		model = Post
		fields = ['id', 'user', 'title', 'content', 'date_created', 'views', 'rating',
				  'dropped_rating_users', 'raised_rating_users', 'bookmarked_users']
