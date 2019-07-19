from rest_framework.permissions import BasePermission
from .models import Post, PostComments


class IsPostOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        post = Post.objects.get(pk=view.kwargs['pk'])
        if post.user_name == request.user:
            return True


class IsCommentOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        comment = PostComments.objects.get(pk=view.kwargs['pk'])
        if comment.user_name == request.user:
            return True