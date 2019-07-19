from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from rest_framework import generics, filters
from blog.forms import SignUpForm
from .models import Post, PostComments
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsCommentOwner, IsPostOwner
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import ListPagination


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')
    else:
        form = SignUpForm
        return render(request, 'signup.html', {'form':form})

def mainUrl(request):
    return render(request, 'main.html', {})


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user_name', 'title')
    search_fields = ('user_name', 'title')


class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)


class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsPostOwner,)


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsPostOwner,)


class PostCommentListView(generics.ListAPIView):
    queryset = PostComments.objects.all()
    serializer_class = CommentSerializer


class PostCommentDetailView(generics.RetrieveUpdateAPIView):
    queryset = PostComments.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCommentOwner,)


class PostCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)


class PostCommentDeleteView(generics.DestroyAPIView):
    queryset = PostComments.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCommentOwner,)

class Marsel(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user_name', 'title')
    search_fields = ('user_name', 'title')
    

