from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=256)
    isbn = models.CharField(max_length=13,primary_key=True)
    price = models.DecimalField(decimal_places=2,max_digits=6,default=1.00)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("my_books:booksList")



class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional fields for this member
    about_member = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures',blank=True)


    def __str__(self):
        return self.user.name

class Author(models.Model):

    name = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    book =  models.ManyToManyField(Book)#to be revised,you don't really want to delete an author just in case
    #he/she has authored other books so deleting this author will leave some books without an author

    def __str__(self):
        return self.name
    class Meta:
        indexes = [
            models.Index(fields = ['name'])
        ]

class AuthoredBook(models.Model):
    book= models.ForeignKey(Book,on_delete=models.CASCADE,related_name='authors')
    author= models.ForeignKey(Author,on_delete=models.CASCADE,related_name='authored')
    unique_togeter = (('book.isbn','author.name'),)

    def __str__(self):
        return self.book.isbn
