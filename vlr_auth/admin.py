from django.contrib import admin
from .models import Profile,Category,Worker
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProfileInLine (admin.StackedInline):
    model=Profile
    can_delete=False
    verbose_name_plural="Profiles"
    
class CustomizedUserAdmin (UserAdmin):
    inlines=(ProfileInLine, )
    
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name','category','phone_number','email','years_of_experience','address','city','created_at')
    
    
admin.site.unregister (User)
admin.site.register (User, CustomizedUserAdmin)
admin.site.register(Category)
admin.site.register(Worker)