from .serializers import *
from .serializers import Books
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView


class APIBookList(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class APIBookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookDetailSerializer

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs.get('pk'))
