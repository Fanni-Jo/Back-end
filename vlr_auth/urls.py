from django.urls import path
from .views import (RegisterView,
                    LoadUserView,
                    password_reset_request,
                    home,
                    logout_view,
                    LoadUserdetail,
                    ServiceProviderSignupView,
                    ServiceProviderdetailView,
                    activate,
                    ProfileView,
                    WorkerProfileView,
                    ClientRegisterView,
                    ClientDetailView,
                    UserDetailView,
                    ReviewViewSet,
                    ReviewDetailViewSet,
                    CreateServiceProviderReview,
                    UpdateServiceProviderReview
                    )


urlpatterns = [
    path('signup/', RegisterView.as_view(),name="signup"),
    path('user/<str:username>/', UserDetailView.as_view(),name="user"),
    path('signup/client',ClientRegisterView.as_view(),name="client_signup"),
    path('client/<int:pk>',ClientDetailView.as_view(),name="client_detail"),
    path('signup/service-provider',ServiceProviderSignupView.as_view(),name="ServiceProvider_signup"),
    path('service-provider/<int:pk>',ServiceProviderdetailView.as_view(),name="ServiceProvider_detail"),
    
    # path('user/', LoadUserView.as_view(),name="user"),
    path("password-reset/", password_reset_request, name="password_reset"),
    path("home/", home, name="home"),
    path("logout/", logout_view, name="logout"),
    path("userdetail/<str:username>", LoadUserdetail.as_view(), name="userdetail"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    
    # path('test/',ProfileView.as_view(),name="test"),
    # path('worker/',WorkerProfileView.as_view(),name="worker"),
    
    path("review/", ReviewViewSet.as_view(), name="review"),
    path('review/<int:pk>', ReviewDetailViewSet.as_view(), name="review_detail"),
    path("review-provider/", CreateServiceProviderReview.as_view(), name="review"),
    path("review-provider/<str:username>", UpdateServiceProviderReview.as_view(), name="reviewdetail"),
]