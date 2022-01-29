from django.urls import path
from .views import DeletePostView, UpdateCommentView, UpdatePostView, PostsView, CommentsView, \
     AddCommentView, DeleteCommentView, AddPostView
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('posts', PostsView.as_view(), name='posts'),
    # path('post/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('addpost', AddPostView.as_view(), name='add_post'),
    path('editpost/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('deletepost/<int:pk>', DeletePostView.as_view(), name='delete_post'),

    path('comments', CommentsView.as_view(), name='comments'),
    # path('comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
    path('addcomment', AddCommentView.as_view(), name='add_comment'),
    path('editcomment/<int:pk>', UpdateCommentView.as_view(), name='edit_comment'),
    path('deletecomment/<int:pk>', DeleteCommentView.as_view(), name='delete_comment'),
]
