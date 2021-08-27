from django.urls import path
from .views import CreateAccountView
from .views import UserProfile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    path('<int:pk>/',UserProfile.as_view(),name='userProfile')
]