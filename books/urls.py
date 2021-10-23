from django.urls import path, include
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('<int:pk>/', BookGenre.as_view(), name='by_genre'),
    path('add/', CreateBookView.as_view(), name='add'),
    path('delete/<int:pk>/', DeleteBookView.as_view(), name='delete'),
    path('edit/<int:pk>/', UpdateBookView.as_view(), name='edit'),
    path('details/<int:pk>/', BookDetailView.as_view(), name='details'),
    path('api/', include('books.api.urls'))
]