
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors of of the posts to edit it.
    Assumes the model instance has an `author` attribute.
    """
    info_message = 'You cannot change the content of the other users'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
