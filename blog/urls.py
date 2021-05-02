from django.urls import path
from .views import  BlogUpdateView, BlogUpdateViews, school





app_name = 'blog'
urlpatterns = [
    
    path('update-view/<pk>/',  BlogUpdateView.as_view()),
    path('update/<pk>/',  BlogUpdateViews.as_view()),
    path('school/',  school),


]

