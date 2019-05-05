from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('', PostListView.as_view(),name="bloghome"),
    path('about/', views.about,name="aboutpage"),
    path('posts/<int:pk>/',PostDetailView.as_view(),name='postdetail'),
    path('posts/new/',PostCreateView.as_view(),name='postcreate'),
    path('posts/<int:pk>/update/',PostUpdateView.as_view(),name='postupdate'),
    path('posts/<int:pk>/delete/',PostDeleteView.as_view(),name='postdelete'),
    path('user/<str:username>', UserPostListView.as_view(),name="userposts"),
]
