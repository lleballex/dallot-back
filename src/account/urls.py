from django.urls import path

from .views import UsersView, UserView
from .views import UserPostsView, UserOverView
from .views import GetAuthToken, GetUserByAuthToken


urlpatterns = [
	path('token/get_auth_token/', GetAuthToken.as_view(), name='get_auth_token'),
	path('token/get_user/', GetUserByAuthToken.as_view(), name='get_user_by_auth_token'),

	path('users/', UsersView.as_view(), name='users_view'),
	path('users/<int:id>/', UserView.as_view(), name='user_view'),
	path('users/<str:username>/', UserView.as_view(lookup_field='username'),
		 name='user_view_by_username'),

	path('users/<int:id>/overview/', UserOverView.as_view(), name='user_overview'),
	path('users/<str:username>/overview/', UserOverView.as_view(search_by_id=False),
		 name='user_overview_by_username'),
	path('users/<int:id>/posts/', UserPostsView.as_view(), name='user_posts'),
	path('users/<str:username>/posts/', UserPostsView.as_view(search_by_id=False),
		 name='user_posts_by_username'),
]
