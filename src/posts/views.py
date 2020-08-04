from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.mixins import BaseAPIView

from . import utils
from .models import Post
from .permissions import PostPermission


class PostsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
	"""Returns list of all posts and creates a new one"""

	queryset = Post.objects.all()
	permission_classes = [IsAuthenticatedOrReadOnly]

	def get(self, request):
		return self.list(request)

	def post(self, request):
		return self.create(request)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def get_serializer_class(self):
		return utils.get_serializer_class(self.request.method)


class PostView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
			   mixins.DestroyModelMixin, BaseAPIView):
	"""Returns, updates and destroys post"""

	lookup_field = 'id'
	queryset = Post.objects.all()
	permission_classes = [PostPermission]

	def get(self, request, *args, **kwargs):
		response = self.retrieve(request, *args, **kwargs)
		post = self.get_object()
		post.views += 1
		post.save()
		return response

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

	def get_serializer_class(self):
		return utils.get_serializer_class(self.request.method)


class DropRatingView(utils.UpdatePostRatingMixin):
	"""Drops rating of the post"""

	drop_rating = True
	message = 'You cannot drop the rating twice'


class RaiseRatingView(utils.UpdatePostRatingMixin):
	"""Raises rating of the post"""

	raise_rating = True
	message = 'You cannot raise the rating twice'


class RestoreRatingView(utils.UpdatePostRatingMixin):
	"""Restores vote at rating of the post"""

	restore_rating = True
	message = 'You cannot restore vote if you did not vote'


class AddToBookmarksView(utils.UpdatePostBookmarksMixin):
	"""Adds post to bookmarks of authenticate user"""

	add = True
	message = 'You cannot bookmark post twice'


class RemoveFromBookmarksView(utils.UpdatePostBookmarksMixin):
	"""Removes post to bookmarks of authenticate user"""

	remove = True
	message = 'You cannot remove post from bookmarks twice'

	