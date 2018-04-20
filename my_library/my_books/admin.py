from django.contrib import admin
from my_books.models import Book,Member,AuthoredBook,Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Author)
admin.site.register(AuthoredBook)
