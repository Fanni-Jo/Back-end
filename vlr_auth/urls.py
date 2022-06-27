from django.urls import path
from .views import (RegisterView,
                    LoadUserView,
                    password_reset_request,
                    home,
                    logout_view,
                    LoadUserdetail,
                    Signup,
                    workerkerdetail,
                    ReviewViewSet
                    )


urlpatterns = [
    path('signup/', RegisterView.as_view(),name="signup"),
    path('user/', LoadUserView.as_view(),name="user"),
    path("password_reset/", password_reset_request, name="password_reset"),
    path("home/", home, name="home"),
    path("logout/", logout_view, name="logout"),
    path("userdetail/<str:username>", LoadUserdetail.as_view(), name="userdetail"),
    path("signup/worker", Signup.as_view(), name="signup"),
    path("workerdetail/<str:username>", workerkerdetail.as_view(), name="workerdetail"),
    path("review/", ReviewViewSet.as_view(), name="review"),
]