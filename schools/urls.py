from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='schools.index'),
    path('<int:id>', views.show, name='schools.show'),
]