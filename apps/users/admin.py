from django.contrib import admin
from .models import User
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')

    fieldsets = (
        ('پایه', {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password',
            ),
        }),
        ('اجازه ها', {
            'classes': ('collapse',),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('Important Dates', {
            'classes': ('collapse',),
            'fields': (
                'last_login',
                'date_joined',
            ),
        }),
    )

    add_fieldsets = (
        ('ساخت کاربر جدید', {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
            ),
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
