from django.contrib import admin
from profile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'get_username', 'get_email', 'get_firstname', 'get_lastname')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Name'
    get_username.admin_order_field = 'user__username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'

    def get_firstname(self, obj):
        return obj.user.first_name
    get_firstname.short_description = 'First Name'
    get_firstname.admin_order_field = 'user__first_name'

    def get_lastname(self, obj):
        return obj.user.last_name
    get_lastname.short_description = 'Last Name'
    get_lastname.admin_order_field = 'user__last_name'


admin.site.register(Profile, ProfileAdmin)
