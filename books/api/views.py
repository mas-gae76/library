from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer, BookDetailSerializer
from .serializers import Books, Author
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request):
    books = Books.objects.all()
    serializer = BookSerializer(books, many=True)
    return HttpResponse(serializer.data)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_book_detail(request, book_id):
    book = Books.objects.filter(id=book_id)
    serializer = BookDetailSerializer(book, many=True)
    return HttpResponse(serializer.data)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add(request):
    load = json.loads(request.body)
    try:
        author = Author.objects.get(id=load['author'])
        book = Books.objects.create(
            title=load['title'],
            description=load['description'],
            image=load['image'],
            author=load['author'],
            release_date=load['release_date']
        )
        serializer = BookSerializer(book)
        return HttpResponse({'book': serializer.data}, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return HttpResponse({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return HttpResponse({'error': 'Что-то пошло не так'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def edit(request, book_id):
    load = json.loads(request.body)
    book_element = Books.objects.filter(id=book_id)
    try:
        book_element.update(**load)
        book = Books.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return HttpResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return HttpResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return HttpResponse({'error': 'Что-то пошло не так'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        book.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return HttpResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return HttpResponse({'error': 'Что-то пошло не так'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


'''
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
'''