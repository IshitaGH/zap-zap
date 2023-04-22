from django.contrib import admin
from .models import Profile
# from table.admin import DataInLineAdmin

# Register your models here.

# TODO: CHANGE THIS TO DISPLAY ALL THE NAMES OF THE PHOTOS THAT PEOPLE UPLOAD
# # lets all of the data records associated with a user to be displayed under the user in admin
class ProfileAdmin(admin.ModelAdmin):
    pass
#     inlines=[DataInLineAdmin]

admin.site.register(Profile, ProfileAdmin)