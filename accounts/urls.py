from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    url('signup/', views.register, name='signup'),
    url('profile/', views.show_person_cabinet, name='profile'),
]