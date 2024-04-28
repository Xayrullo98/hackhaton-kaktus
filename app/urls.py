"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mysite.views import *
from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('project/', project,name="project"),
    path('projectfilter/<id>/', projectfilter,name="projectfilter"),
    path('article/', article,name="article"),
    path('article/<id>/', articlefilter,name="articlefilter"),
    path('mentor/', mentor,name="mentor"),
    path('mentorfilter/<id>/', mentorfilter,name="mentorfilter"),
    path('course/', course,name="course"),
    path('coursefilter/<id>/', coursefilter,name="coursefilter"),
    path('event/', event,name="event"),
    path('eventfilter/<id>/', eventfilter,name="eventfilter"),
    path('work/', works,name="works"),
    path('work/<id>/', work,name="work"),
    path('articlesingle/<id>/', article_single,name="article_single"),
    path('coursesingle/<id>/', course_single,name="course_single"),
    path('eventsingle/<id>/', event_single,name="event_single"),
    path('mentorsingle/<id>/', mentor_single,name="mentor_single"),
    path('projectsingle/<id>/', project_single,name="project_single"),
    path('worksingle/<id>/', work_single,name="work_single"),
    path('feedback/', feedback,name="feedback"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIAFILE_DIRS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
