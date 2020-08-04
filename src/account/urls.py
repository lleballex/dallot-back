from django.urls import path

from .views import CreateUserView
from .views import GetAuthToken, GetUserByAuthToken


urlpatterns = [
	# authentication token
	path('token/get_auth_token/', GetAuthToken.as_view(), name='get_auth_token'),
	path('token/get_user/', GetUserByAuthToken.as_view(), name='get_user_by_auth_token'),

	path('create_user/', CreateUserView.as_view(), name='create_user')
]
