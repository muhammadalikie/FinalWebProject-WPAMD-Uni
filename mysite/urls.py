from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('article', views.article, name='article'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('sign', views.sign, name='sign'),
    path('comment/<int:pk>', views.comment, name='comment'),
    # path('subcomment/<int:pk>', views.sub_comment, name='sub-comment'),
    # path('search/', views.search, name='search'),
]
