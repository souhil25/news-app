from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email', 
        'username', 
        'age', 
        'is_staff', 
                    ] # new
    
    # add_fieldsets = UserAdmin.add_fieldsets 
    add_fieldsets = (
        (None, 
            {'fields': ('age', 'username', 'email',)}),)
    


# admin.site.register(CustomUser, CustomUserAdmin) # User can be managed by UserAdmin
# admin.site.register(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)
