from django.urls import path
from .views import *


urlpatterns = [
    path('', APIBookList.as_view()),
    path('details/<int:pk>', APIBookDetail.as_view()),
]