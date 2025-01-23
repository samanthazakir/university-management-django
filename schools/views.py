from django.shortcuts import get_object_or_404, render

from .models import School


def index(request):
    school_queryset = School.objects.all()
    context = {
        "school_list": school_queryset,
    }
    return render(request, 'schools/index.html', context)

def show(request, id):
    school = get_object_or_404(School, id=id)
    context = {
        "school": school,
        "course_list": school.courses.all(),
    }
    return render(request, 'schools/show.html', context)
