from django.urls import path
from . import api


urlpatterns = [
    path('api/post/create/', api.create_post),
    path('api/posts/', api.ListPost.as_view()),
    path('api/image/<int:pk>/', api.ListImage.as_view()),
]