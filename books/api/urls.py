from django.urls import path
from .views import *


urlpatterns = [
    path('read/', get_books),
    path('create/', add),
    path('update/<int:book_id>', edit),
    path('delete/<int:book_id>', delete)
]