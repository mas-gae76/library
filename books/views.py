from django.shortcuts import render, redirect
from .models import Books, Genre
from .forms import BookForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
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
        return Books.objects.filter(genre=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cg'] = Genre.objects.get(pk=self.kwargs['pk']).name
        context['gs'] = Genre.objects.all()
        return context


class BookDetailView(DetailView):
    model = Books
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['gs'] = Genre.objects.all()
        return context


class CreateBookView(CreateView):
    form_class = BookForm
    template_name = 'add.html'
    success_url = '/books/details/{id}'


class DeleteBookView(DeleteView):
    model = Books
    success_url = '/books/'
    template_name = 'delete.html'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])


class UpdateBookView(UpdateView):
    form_class = BookForm
    template_name = 'edit.html'
    success_url = '/books/details/{id}'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])
