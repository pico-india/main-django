from django.contrib import admin
from Accounts.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pf_pic', 'bio', 'insta', 'fb')

admin.site.register(Profile, ProfileAdmin)
