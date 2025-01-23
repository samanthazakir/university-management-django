from django.shortcuts import get_object_or_404, render

from .models import Course


def index(request):
    course_queryset = Course.objects.all()
    context = {
        "course_list": course_queryset,
    }
    return render(request, 'courses/index.html', context)

def show(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        "course": course,
    }
    return render(request, 'courses/show.html', context)
