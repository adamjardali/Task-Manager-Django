from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
	
	def has_object_permission(self, request, view, obj):
# Read-only permissions are allowed for any request
		if request.method in permissions.SAFE_METHODS:
			return True
# Write permissions are only allowed to the author of a post
		# print("The object is::::::::")
		# print(obj)
		# print(obj.userId.id)
		# print(request.user.id)
		# # print(request)
		return obj.userId.id == request.user.id

