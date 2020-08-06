from django.http import Http404
from rest_framework import mixins
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST

from core.mixins import BaseAPIView
from posts.serializers import PostSerializer

from . import utils
from .models import User
from .permissions import UserPermission
from .serializers import UserSerializer, CreateUserSerializer


class GetAuthToken(APIView):
	"""Returns authentication JWT and user"""

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')

		if not username or not password:
			return Response({'detail': 'Request must have \'username\' and \'password\''},
							status=HTTP_400_BAD_REQUEST)

		user = authenticate(username=username, password=password)
		if not user:
			return Response({'detail': 'Username or password are invalid'},
							status=HTTP_400_BAD_REQUEST)
		serializer = UserSerializer(user)

		return Response({
			'token': utils.get_auth_token(user.id),
			'user': serializer.data,
		})


class GetUserByAuthToken(APIView):
	"""Returns user if authentication token is valid or exception"""

	def post(self, request):
		token = request.data.get('token')
		if not token:
			return Response({'detail': 'Request must have \'token\''},
							status=HTTP_400_BAD_REQUEST)

		user_id = utils.decode_auth_token(token)
		if not user_id:
			return Response({'detail': 'Token is invalid or expired'},
							status=HTTP_400_BAD_REQUEST)

		try:
			user = User.objects.get(id=user_id)
		except User.DoesNotExist:
			return Response({'detail': 'Token is invalid'},
							status=HTTP_400_BAD_REQUEST)

		serializer = UserSerializer(user)
		return Response(serializer.data)


class UsersView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
	"""Returns list of users and create a new one"""

	queryset = User.objects.all()

	def get(self, request):
		return self.list(request)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def get_serializer_class(self):
		return utils.get_user_serializer(self.request.method, public=True)


class UserView(mixins.RetrieveModelMixin, BaseAPIView):
	"""Returns user"""

	lookup_field = 'id'
	queryset = User.objects.all()
	permission_classes = [UserPermission]

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def get_serializer_class(self):
		return utils.get_user_serializer(self.request.method)


class UserOverView(BaseAPIView):
	"""Returns user overview (popular posts)"""

	def get(self, request, id):
		try:
			user = User.objects.get(id=id)
		except User.DoesNotExist:
			raise Http404

		post_serializer = PostSerializer(user.posts.order_by('-views')[:5],
										 many=True)

		return Response({'posts': post_serializer.data})


class UserPostsView(mixins.ListModelMixin, BaseAPIView):
	"""Return list of user posts"""

	serializer_class = PostSerializer

	def get(self, request, id):
		try:
			user = User.objects.get(id=id)
		except User.DoesNotExist:
			raise Http404

		self.queryset = user.posts.all()

		return self.list(request)