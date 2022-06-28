from django.shortcuts import render
from .models import User

from django.views.generic import CreateView
from .forms import CustomerSignUpForm , WorkerSignUpForm

# Create your views here.
def register(request):
    return render(request,'../templates/registration/signup.html')


class Customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name ="../templates/registration/customer_reg.html"

# to direct the user for other page 

    # def validation (self,form):
    #     user=form.save()
    #     login(self.request,user)
    #     return redirect(/)


class Worker_register(CreateView):
    model = User
    form_class = WorkerSignUpForm
    template_name ="../templates/registration/worker_reg.html"