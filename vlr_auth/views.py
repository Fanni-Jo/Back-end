from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Profile
from .permissions import IsOwnerOrReadOnly,EveryOne
from .serializers import UserSerializer
from rest_framework import permissions

class UserCreateView(ListCreateAPIView):
    permission_classes=permissions.AllowAny
    model = Profile
    queryset = Profile.objects.all()
    serializer_class=UserSerializer
    
class EditUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

#newly added function
def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mob': user.profile.mob,})
 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
 
            #newly added
            user.profile.mob = form.cleaned_data.get('mob')
            update_user_data(user)  
           
 
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
 
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
 
            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request,'home.html')
