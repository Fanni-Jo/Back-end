from django.urls import path
from .views import *


urlpatterns = [
path('signup/', signup, name='signup'),
path('register/',UserCreateView.as_view(),name='login'),
path('profile/edit',EditUpdateDelete.as_view()),
path('',home,name="home")
]