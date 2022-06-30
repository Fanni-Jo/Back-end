from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.models import User
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
from django.contrib import messages
from .models import Profile,ServiceProviderProfile,Review
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly
from .serializers import (UserSerializer,
                          ServiceProviderProfileSerializer,
                          ClientSerializer,
                          ReviewSerializer,
                          ReviewWorkerRating                      
                          )

# {
#     "first_name": "John",
#     "last_name": "Doe",
#     "username": "testprofile",
#     "email": "testprofile@bar.com",
#     "phone_number":"+962785436262",
#     "password": "123456barham",
#     "re_password": "123456barham",
#     "profile_picture":"3.jpg"
# }
class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_object(self):
        return self.request.user
    
class ClientRegisterView(ListCreateAPIView):
    permission_classes = permissions.IsAuthenticated,
    queryset=Profile.objects.all()
    serializer_class=ClientSerializer
    
class ClientDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = IsOwnerOrReadOnly,
    queryset=Profile.objects.all()
    serializer_class=ClientSerializer
    lookup_field="username"
    
class ServiceProviderdetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset=ServiceProviderProfile.objects.all()
    serializer_class = ServiceProviderProfileSerializer     
    lookup_field = 'username'

class ServiceProviderSignupView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset=ServiceProviderProfile.objects.all()
    serializer_class = ServiceProviderProfileSerializer     
    

class LoadUserdetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    
def activate(request,uidb64, token):
    try:
        user=User.objects.get(pk=uidb64)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')

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
					'domain':'https://fanni-jo.herokuapp.com/',
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

class ProfileView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset=User.objects.all()
    serializer_class = UserSerializer      

class WorkerProfileView(APIView):
    permission_classes = (permissions.AllowAny, )
    queryset=ServiceProviderProfile.objects.all()
    
class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:

            data = request.data
            
            first_name = data['first_name']
            last_name = data['last_name']
            username = data['username']
            email= data['email'].lower()
            password = data['password']
            re_password = data['re_password']
            # phone_number=data['phone_number'],
            # birthdate=data['birthdate'],
            # gender=data['gender'] ,
            # profile_picture=data['profile_picture']
            # num=Profile.objects.filter(phone_number=phone_number)
            # if num:
            #     raise ValidationError(" Phone Number Already In Use")  

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
                        user.save()
                        
                        #delete workerdatafields
                        
                        # Create a user profile
                        # profile = Profile()
                        # profile.add_to_class("phone_number", phone_number)
                        # profile.phone_number=phone_number
                        # profile.profile_picture = profile_picture
                        # profile.gender=gender
                        # profile.birthdate=birthdate
                        # profile.save()
                        # profile=Profile.objects.create(
                        #         phone_number=phone_number,
                        #         profile_picture=profile_picture,
                        #     )                       
                        # profile.save()
                        if User.objects.filter(username=username).exists():
                            # # USER ACTIVATION
                            # current_site = get_current_site(request)
                            # subject = 'Please activate your account'
                            # message = render_to_string('account_verification_email.html', {
                            # 'user': {user.first_name}+' '+{user.last_name},
                            # 'domain': current_site,
                            # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            # 'token': default_token_generator.make_token(user),
                            #    })
                            # try:
                            #     send_mail(subject, message, 'fanni.jo22@gmail.com' , [email], fail_silently=False)
                            #     messages.success(request, 'Thank you for registering with us. We have sent you a verification email to your email address [{email}]. Please verify it.')

                            # except ValueError:
                            #     messages.error(request, 'Something went wrong when trying to send email')

                            # profile=Profile(user=username)
                            # profile=Profile()._base_manager.create(
                            # # profile=Profile.objects.create(
                            #         user=User.objects.get(username=username),
                            #         user_id=User.objects.get(username=username).id,
                            #         phone_number=phone_number,
                            #         birthdate=birthdate,
                            #         gender=gender,
                            #         profile_picture=profile_picture,
                            # )                
                            # profile.save()

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
# {
#     "first_name": "John",
#     "last_name": "Doe",
#     "username": "testprofile2",
#     "email": "barhamfarraj@icloud.com",
#     "password": "123456barham",
#     "re_password": "123456barham",
#     "phone_number":"+962785436262",
#     "profile_picture":"3.jpg",
#     "birthdate":"2020-01-01",
#     "gender":"MALE"
# }            
# class ClientRegisterView(ListCreateAPIView):
#     permission_classes = permissions.IsAuthenticated,
#     queryset=Profile.objects.all()
#     serializer_class=ProfileSerializer
    
# class ClientDetailView(RetrieveUpdateDestroyAPIView):
#     permission_classes = IsOwnerOrReadOnly,
#     queryset=Profile.objects.all()
#     serializer_class=ProfileSerializer
#     lookup_field="user"
    
    # def post(self, request):
    #     try:

    #             data = request.data
                
    #             user=data['user']
    #             phone_number=data['phone_number'],
    #             birthdate=data['birthdate'],
    #             gender=data['gender'] ,
    #             profile_picture=data['profile_picture']
    #             num=Profile.objects.filter(phone_number=phone_number)
    #             if num:
    #                 raise ValidationError(" Phone Number Already In Use")  

    #             if User.objects.filter(username=user).exists():
    #                 if not Profile.objects.filter(user=user).exists():
                        
    #                     user = Profile.objects.create(
    #                         user=user,
    #                         phone_number=phone_number,
    #                         birthdate=birthdate,
    #                         gender=gender,
    #                         profile_picture=profile_picture
    #                     )
    #                     user.save()
                        
                        
    #                     if Profile.objects.filter(user=user).exists():
                            
    #                         return Response(
    #                             {'success': 'Account created successfully'},
    #                             status=status.HTTP_201_CREATED
    #                         )
    #                     else:
    #                         return Response(
    #                             {'error': 'Something went wrong when trying to create Client Account'},
    #                             status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #                         )
    #                 else:
    #                     return Response(
    #                         {'error': 'Username already exists'},
    #                         status=status.HTTP_400_BAD_REQUEST
    #                     )
    #             else:
    #                 return Response(
    #                     {'error': 'User does not exist'},
    #                     status=status.HTTP_400_BAD_REQUEST
    #                 )        
    #     except:
    #         return Response(
    #             {'error': 'Something went wrong when trying to register client account'},
    #             status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #         )            
class ReviewViewSet(ListCreateAPIView):
    permission_classes = IsOwnerOrReadOnly,
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetailViewSet(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "username"
    
class CreateReview(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset=ReviewWorkerRating.objects.all()
    serializer_class = ReviewSerializer 

class UpdateReview(RetrieveUpdateDestroyAPIView): 
    permission_classes = (permissions.IsAuthenticated, )
    queryset=ReviewWorkerRating.objects.all()
    serializer_class = ReviewSerializer