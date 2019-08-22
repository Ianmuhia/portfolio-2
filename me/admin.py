from django.contrib import admin
# Register your models here.
from .models import Education, Personal_info, Expirience, Awards

admin.site.register(Education)
admin.site.register(Personal_info)
admin.site.register(Expirience)
admin.site.register(Awards)
