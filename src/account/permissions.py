from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
	"""Permission for getting data about user"""

	message = 'This action is available only to the owner of this'

	def has_permission(self, request, view):
		return request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		return request.user == obj or request.user.is_admin