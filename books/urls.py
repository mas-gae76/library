from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:genre_id>/', by_genre, name='by_genre'),
    path('add/', add, name='add'),
    path('delete/<int:book_id>/', delete, name='delete'),
    path('edit/<int:book_id>/', edit, name='edit'),
]