from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter

from posts.models import Post, Group, Follow
from .serializers import GroupSerializer, PostSerializer, CommentSerializer
from .serializers import FollowSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAuthenticatedOrReadOnly(),)
        return super().get_permissions()


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAuthenticatedOrReadOnly(),)
        return super().get_permissions()


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('user__username', 'following__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset
