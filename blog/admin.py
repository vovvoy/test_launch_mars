from django.contrib import admin
from .models import Post as PostAdmin
from .models import PostComments as PostCommentsAdmin


admin.site.register(PostAdmin)
admin.site.register(PostCommentsAdmin)


