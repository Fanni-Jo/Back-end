from django.contrib import admin
from .models import Profile,Category,ServiceProviderProfile,Review,ReviewWorkerRating
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProfileInLine (admin.StackedInline):
    model=Profile
    extra=0
    verbose_name_plural="Profiles"
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    
class WorkerProfileInLine (admin.StackedInline):
    model=ServiceProviderProfile
    extra=0
    verbose_name_plural="WorkerProfiles"
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)    
    
        
class CustomizedUserAdmin (UserAdmin):
    inlines=(ProfileInLine,WorkerProfileInLine )
    
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name','category','phone_number','email','years_of_experience','address','city','created_at')
    
admin.site.unregister (User)
admin.site.register (User, CustomizedUserAdmin)
admin.site.register(Category)
admin.site.register(ServiceProviderProfile)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(ReviewWorkerRating)