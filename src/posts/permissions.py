from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):
	"""Permissions for getting and updating post"""

	message = 'This action is available only to the owner of this'

	def has_permission(self, request, view):
		return bool(
			request.method in SAFE_METHODS or 
			request.user.is_authenticated
		)
		

	def has_object_permission(self, request, view, obj):
		return bool(
			request.method in SAFE_METHODS or
			request.user == obj.user or request.user.is_admin
		)
