from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.models import User
from .serializers import UserSerializer,UserDetailSerializer
from django.core.exceptions import ValidationError 
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import logout
from .models import Profile
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly

# {
#     "first_name": "John",
#     "last_name": "Doe",
#     "username": "johndoe",
#     "email": "doe@bar.com",
#     "phone_number":"+639123456789",
#     "password": "123456barham",
#     "re_password": "123456barham",
    
# }
class Sigup(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            
            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            email= data['email'].lower()
            phone_number = data['phone_number']
            password = data['password']
            re_password = data['re_password']
            # profile_picture = data['profile_picture']
            
            num=Profile.objects.filter(phone_number=phone_number)
            if num:
                raise ValidationError(" Phone Number Already In Use")  

            new = User.objects.filter(email=email)  
            if new.count():  
                raise ValidationError(" Email Already Exist")  
            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(username=username).exists():
                        user = User.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            password=password,
                        )
                        # profile=Profile.objects.create(
                        #         phone_number=phone_number,
                        #         profile_picture=profile_picture,
                        #     )
                    
                        user.save()
                        # profile.save()
                        if User.objects.filter(username=username).exists():
                            return Response(
                                {'success': 'Account created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        else:
                            return Response(
                                {'error': 'Something went wrong when trying to create account'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )
                    else:
                        return Response(
                            {'error': 'Username already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'Password must be at least 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when trying to register account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            
            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            email= data['email'].lower()
            phone_number = data['phone_number']
            password = data['password']
            re_password = data['re_password']
            # profile_picture = data['profile_picture']
            
            num=Profile.objects.filter(phone_number=phone_number)
            if num:
                raise ValidationError(" Phone Number Already In Use")  

            new = User.objects.filter(email=email)  
            if new.count():  
                raise ValidationError(" Email Already Exist")  
            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(username=username).exists():
                        user = User.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            password=password,
                        )
                        # profile=Profile.objects.create(
                        #         phone_number=phone_number,
                        #         profile_picture=profile_picture,
                        #     )
                    
                        user.save()
                        # profile.save()
                        if User.objects.filter(username=username).exists():
                            return Response(
                                {'success': 'Account created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        else:
                            return Response(
                                {'error': 'Something went wrong when trying to create account'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )
                    else:
                        return Response(
                            {'error': 'Username already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'Password must be at least 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when trying to register account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LoadUserView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class LoadUserdetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'fanni.jo22@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})       

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return home(request)
