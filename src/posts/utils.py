from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.mixins import BaseAPIView

from .models import Post
from .serializers import PostSerializer, UpdatePostSerializer


class UpdatePostRatingMixin(BaseAPIView):
	"""Mixin for updating rating of post"""

	message = 'You cannot do this'
	drop_rating = False
	raise_rating = False
	restore_rating = False

	lookup_field = 'id'
	queryset = Post.objects.all()
	permission_classes = [IsAuthenticatedOrReadOnly]

	def post(self, request, *args, **kwargs):
		post = self.get_object()

		if self.drop_rating:
			rating = post.drop_rating(request.user)
		elif self.raise_rating:
			rating = post.raise_rating(request.user)
		elif self.restore_rating:
			rating = post.restore_rating(request.user)
		else:
			raise ValueError('One of the parameters must be specified: \
							  drop_rating, raise_rating, restore_rating')

		if rating is False:
			return Response({'detail': self.message},
							status=HTTP_403_FORBIDDEN)
		return Response({'rating': rating})


class UpdatePostBookmarksMixin(BaseAPIView):
	"""Mixin for adding or removing post from bookmarks of authenticate user"""

	message = 'You cannot do this'
	add = False
	remove = False

	lookup_field = 'id'
	queryset = Post.objects.all()
	permission_classes = [IsAuthenticatedOrReadOnly]

	def post(self, request, *args, **kwargs):
		post = self.get_object()

		if self.add:
			result = post.add_to_bookmarks(request.user)
		elif self.remove:
			result = post.remove_from_bookmarks(request.user)
		else:
			raise ValueError('One of the parameters must be specified: \
							  add or remove')

		if result is False:
			return Response({'detail': self.message},
							status=HTTP_403_FORBIDDEN)
		return Response({'bookmarks': result})



def get_serializer_class(method):
	# Return post serializer depending on the request method
	if method in SAFE_METHODS:
		return PostSerializer
	return UpdatePostSerializer