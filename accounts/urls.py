from django.urls import path 
from .import views 

urlpatterns =[
    path ('register/',views.register,name="register"),
    path ('customer_register/',views.Customer_register.as_view(),name="customer_register"),
    path ('worker_register/',views.Worker_register.as_view(),name="worker_register")
]