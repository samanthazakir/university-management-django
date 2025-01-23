from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='courses.index'),
    path('<int:id>', views.show, name='courses.show'),
]