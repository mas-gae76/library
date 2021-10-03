from django.shortcuts import render, redirect
from .models import Books, Genre
from .forms import BookForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q


class MainView(ListView):
    model = Books
    paginate_by = 10
    queryset = Books.objects.all()
    template_name = 'index.html'

    def get_queryset(self):
        filter = self.request.GET.get('filter')
        if not filter:
            context = Books.objects.all()
        else:
            query = Q(author__initials__icontains=filter)
            context = Books.objects.filter(query)
        order = self.request.GET.get('orderby', 'title')
        new_context = context.order_by(order)
        return new_context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gs'] = Genre.objects.all()
        context['filter'] = self.request.GET.get('filter', '')
        return context


class BookGenre(ListView):
    model = Books
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        return Books.objects.filter(genre=self.kwargs['genre_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cg'] = Genre.objects.get(pk=self.kwargs['genre_id']).name
        context['gs'] = Genre.objects.all()
        return context


def details(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    return render(request, 'details.html', {'book': book})


def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                form.image = request.FILES['image']
            form.save()
            return redirect('index')
        else:
            return render(request, 'add.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'add.html', {'form': form})


def delete(request, book_id):
    deleted_book = Books.objects.filter(id=book_id)
    deleted_book.delete()
    return redirect('index')


def edit(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Объявление исправлено')
            return redirect('index')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit.html', {'form': form})
