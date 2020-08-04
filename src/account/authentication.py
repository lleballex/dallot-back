from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication

from . import utils
from .models import User

class Authentication(BaseAuthentication):
	"""Authorization when going to any page"""

	def authenticate(self, request):
		auth_token = request.META.get('HTTP_AUTH_TOKEN')

		if not auth_token:
			return None

		user_id = utils.decode_auth_token(auth_token)
		if not user_id:
			raise AuthenticationFailed('Token is invalid or expired')

		try:
			return (User.objects.get(id=user_id), None)
		except User.DoesNotExist:
			raise AuthenticationFailed('Token is invalid')