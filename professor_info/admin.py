from django.contrib import admin

# Register your models here.
from professor_info.models import *

admin.site.register(College)
admin.site.register(Professor)
admin.site.register(ResearchWork)

admin.site.register(Department)
