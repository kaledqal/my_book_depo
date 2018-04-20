from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                 CreateView,ListView,
                                 DetailView,UpdateView,
                                 DeleteView)
from my_books.models import Book,AuthoredBook,Author
from django.urls import reverse,reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookListView(ListView):
    template_name = 'my_books/book_list.html'
    context_object_name = 'book_list'
    model = Book

class BookDetailView(DetailView):
    context_object_name = 'book_detail'
    template_name = 'my_books/book_details.html'
    model = Book

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'my_books/book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("my_books:booksList")

class BookSearchView(TemplateView):
    template_name = 'book_search.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
