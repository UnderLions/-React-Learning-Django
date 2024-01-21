from django.urls import path
from .views import BlogPostCreateView

urlpatterns = [
   
    path('api/blogposts/', BlogPostCreateView.as_view(), name='blogpost-create'),
]
