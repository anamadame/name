from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Hotel)
admin.site.register(Comment)
admin.site.register(Images)
admin.site.register(Room)
admin.site.register(Booking)
