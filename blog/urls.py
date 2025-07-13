from django.urls import path
from . import views 
urlpatterns=[
    path("",views.home.as_view(),name="home-page"),
    path("posts",views.all_posts.as_view(),name="posts-page"),
    path("posts/read-later",views.ReadLaterView.as_view(),name="read-later"),
    path("posts/<slug:slug>",views.post_detail.as_view(),name="post-detail-page"),
]