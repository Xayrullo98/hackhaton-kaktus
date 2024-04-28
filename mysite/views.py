from django.shortcuts import render
from mysite.models import *


# Create your views here.
def index(request):
    # courses
    courses = Course.objects.all()
    if len(courses) >= 3:
        courses = Course.objects.all()[:3]
    # articles
    articles = Article.objects.all()
    if len(articles) >= 3:
        articles = Article.objects.all()[:3]
    # Events
    events = Event.objects.all()
    if len(events) >= 3:
        events = Event.objects.all()[:3]
    mentors = Mentor.objects.all()
    context = {
        "courses": courses,
        "articles": articles,
        "events": events,
        "mentors": mentors,
    }

    return render(request, 'index.html', context)


# Projects
def project(request):
    data = Project.objects.all()
    context = {
        "data": data,
    }
    return render(request, 'projects.html', context)


def projectfilter(request, id):
    data = Project.objects.filter(field_id=id)
    context = {
        "data": data,
    }
    return render(request, 'projects.html', context)


# Articles
def article(request):
    data = Article.objects.all()
    context = {
        "data": data,
    }
    return render(request, 'articles.html', context)


def articlefilter(request, id):
    data = Article.objects.filter(field_id=id)
    context = {
        "data": data,
    }
    return render(request, 'articles.html', context)


# Mentors
def mentor(request):
    data = Mentor.objects.all()
    context = {
        "data": data,
    }
    return render(request, 'mentors.html', context)


def mentorfilter(request, id):
    data = Mentor.objects.filter(field_id=id)
    context = {
        "data": data,
    }
    return render(request, 'mentors.html', context)


def course(request):
    data = Course.objects.all()
    context = {
        "data": data,
    }
    return render(request, 'courses.html', context)


def coursefilter(request, id):
    data = Course.objects.filter(field_id=id)
    context = {
        "data": data,
    }
    return render(request, 'courses.html', context)


# Events
def event(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'events.html', context)


def eventfilter(request, id):
    events = Event.objects.filter(field_id=id)
    context = {
        "events": events,
    }
    return render(request, 'events.html', context)


def works(request):
    data = Vacancy.objects.all()
    context = {
        "works": data,
    }
    return render(request, 'works.html', context)


def work(request, id):
    id = int(id)
    works = Vacancy.objects.filter(type=id)
    print(id == 1)
    if id == 1:
        work_type = "Stajirovka"
        context = {
            "works": works,
            "work": work_type,
        }

        return render(request, 'works.html', context)
    elif id == 2:
        work_type = "Bo'sh ish o'rinlari"
        context = {
            "works": works,
            "work": work_type,

        }

        return render(request, 'works.html', context)
    else:
        work_type = "Bir martalik ishlar"

        context = {
            "works": works,
            "work": work_type,

        }

        return render(request, 'works.html', context)


def article_single(request, id):
    data = Article.objects.get(id=id)
    author = Mentor.objects.get(id=data.mentor_id)
    context = {
        "data": data,
        "mentor": author,

    }

    return render(request, 'article_single.html', context)


def course_single(request, id):
    data = Course.objects.get(id=id)
    author = Mentor.objects.get(id=data.mentor_id)
    context = {
        "data": data,
        "mentor": author,

    }

    return render(request, 'single_mentor.html', context)


def event_single(request, id):
    data = Event.objects.get(id=id)

    context = {
        "data": data,

    }

    return render(request, 'single_event.html', context)


def mentor_single(request, id):
    data = Mentor.objects.get(id=id)

    context = {
        "data": data,
    }
    return render(request, 'single_mentor.html', context)


def project_single(request, id):
    data = Project.objects.get(id=id)

    context = {
        "data": data,
    }
    return render(request, 'single_project.html', context)


def work_single(request, id):
    data = Vacancy.objects.get(id=id)

    context = {
        "data": data,
    }
    return render(request, 'single_work.html', context)

def feedback(request):
    return render(request,'feedback.html')