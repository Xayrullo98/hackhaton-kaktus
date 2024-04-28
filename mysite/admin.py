from django.contrib import admin
from mysite.models import *


# Register your models here.
class AdminJunior(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'field', 'technologies']


admin.site.register(Junior, AdminJunior)


class AdminField(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Field, AdminField)


class AdminMentor(admin.ModelAdmin):
    list_display = ['id', 'name', 'field', 'technologies', 'comment']


admin.site.register(Mentor, AdminMentor)


class AdminVacancy(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'technologies', ]


admin.site.register(Vacancy, AdminVacancy)


class AdminCourse(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'field', 'mentor', 'technologies']


admin.site.register(Course, AdminCourse)


class AdminEvent(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']


admin.site.register(Event, AdminEvent)


class AdminComment(admin.ModelAdmin):
    list_display = ['id', 'mentor', 'text', 'junior', 'event', 'source']


admin.site.register(Comment, AdminComment)


class AdminProject(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'field', 'deadline', 'price', 'requirements']


admin.site.register(Project, AdminProject)

class AdminReferral(admin.ModelAdmin):
    list_display = ['id', 'text', 'mentor', 'junior', 'vacancy', 'status', ]


admin.site.register(Referral, AdminReferral)

class AdminArticle(admin.ModelAdmin):
    list_display = ['id', 'text', 'mentor', 'rating', ]


admin.site.register(Article, AdminArticle)