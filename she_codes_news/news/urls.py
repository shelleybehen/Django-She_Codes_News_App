from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #/news/
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #/news/4
    path('add-story/', views.AddStoryView.as_view(), name='newStory') #where we had our form to add a new story
]
