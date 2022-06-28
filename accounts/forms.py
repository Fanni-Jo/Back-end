from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Worker , Customer,User
from django import forms    


class CustomerSignUpForm (UserCreationForm):
    first_name =forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    phone_number=forms.CharField(required=True)

    class Meta (UserCreationForm.Meta):
        model =User



    @transaction.atomic
    def save(self):
        user =super().save(commit=False)
        user.is_customer=True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        
        user.save()
        customer =customer.objects.create (user=user)
        
        customer.phone_number =self.cleaned_data.get('phone_number')
        customer.save()
        return user








class WorkerSignUpForm (UserCreationForm):
    first_name =forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    phone_number=forms.CharField(required=True)
    designation=forms.CharField(required=True)


    class Meta (UserCreationForm.Meta):
        model =User

    
    @transaction.atomic
    def save(self):
        user =super().save(commit=False)
        user.is_worker=True
        user.is_staff=True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        
        user.save()
        worker  =Worker.objects.create (user=user)
        
        worker.phone_number =self.cleaned_data.get('phone_number')
        worker.designation =self.cleaned_data.get('worker')
        worker.save()
        return user