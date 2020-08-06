from django.urls import path

from .views import UsersView, UserView
from .views import UserPostsView, UserOverView
from .views import GetAuthToken, GetUserByAuthToken


urlpatterns = [
	# authentication token
	path('token/get_auth_token/', GetAuthToken.as_view(), name='get_auth_token'),
	path('token/get_user/', GetUserByAuthToken.as_view(), name='get_user_by_auth_token'),

	path('users/', UsersView.as_view(), name='users_view'),
	path('users/<int:id>/', UserView.as_view(), name='user_view'),

	path('users/<int:id>/overview/', UserOverView.as_view(), name='user_overview'),
	path('users/<int:id>/posts/', UserPostsView.as_view(), name='user_posts'),
]
