from . import views
from django.urls import path

urlpatterns = [
     path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('student', views.student, name='student'),
    path('list', views.list, name='list'),
    path('delete/<int:id>', views.delete, name='delete'),
]
