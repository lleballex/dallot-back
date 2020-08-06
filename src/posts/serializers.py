from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
	"""Serializer for getting post"""

	user = UserSerializer()

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


class CommentSerializer(serializers.ModelSerializer):
	"""Serialzer for comment"""

	class Meta:
		model = Comment
		fields = ['id', 'post', 'user', 'text', 'date_created']