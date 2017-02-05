from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html

from professor_info.models import *

class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    # readonly_fields=('id',)
    def profile_link(obj):
        return format_html('<a href="%s" target="_blank">Profile Link</a>' %obj.profile_link,)

    list_max_show_all = 300
    ordering = ('id',)
    search_fields = ('name', 'college','id')
    list_display = ('id', 'name', 'college','department',profile_link)

class CollegeAdmin(admin.ModelAdmin):

    model = College

    list_max_show_all = 500
    list_display = ('id','name', 'address')
    ordering = ('name','address')
    readonly_fields=('id',)
    search_fields = ('name','id')

# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(College, CollegeAdmin)
admin.site.register(Professor,ProfessorAdmin )
admin.site.register(ResearchWork)

admin.site.register(Department)
