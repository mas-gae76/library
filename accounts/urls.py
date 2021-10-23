from . import views
from django.urls import path


urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('signup/', views.UserRegisterView.as_view(), name='signup'),
    path('profile/', views.show_person_cabinet, name='profile'),
]