from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='posts_user')
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostComments(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='comments_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content_comment = models.TextField()
    image_comment = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content_comment
