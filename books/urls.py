from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('<int:genre_id>/', BookGenre.as_view(), name='by_genre'),
    path('add/', add, name='add'),
    path('delete/<int:book_id>/', delete, name='delete'),
    path('edit/<int:book_id>/', edit, name='edit'),
    path('details/<int:book_id>/', details, name='details')
]