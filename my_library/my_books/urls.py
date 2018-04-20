from django.conf.urls import url
from my_books import views

app_name = 'my_books'

urlpatterns = [
    url(r'^$',views.BookListView.as_view(),name='booksList'),
    url(r'^(?P<pk>[\d|\w]{13})$',views.BookDetailView.as_view(),name='booksDetail'),
    url(r'^create/',views.BookCreateView.as_view(),name='book_create'),
    url(r'^search/',views.BookSearchView.as_view(),name='book_search'),
    url(r'^update/(?P<pk>[\d|\w]{13})/$',views.BookUpdateView.as_view(),name='book_update'),
    url(r'^delete/(?P<pk>[\d|\w]{13})/$',views.BookDeleteView.as_view(),name='book_delete'),
]
