from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Genre, Book

# Create your views here.


def index(request: HttpRequest):
    genries=Genre.objects.all()
    books=Book.objects.all()
    context={
        "genries":genries,
        "books":books,
        "title":"Asosiy sahifa"
    }
    return render(request, template_name='bookshop/index.html', context=context)



def genre_by_book(request, genre_id:int):
    genre=Genre.objects.get(id=genre_id)
    genries=Genre.objects.all()
    genres=Genre.objects.filter(id=genre_id)
    books=Book.objects.filter(genre_id=genre_id)
    context={
        "genres":genres,
        "books":books,
        "genries":genries,
        "title":genre.name,
    }
    return render(request, template_name="bookshop/index.html", context=context)



def book_detail(request: HttpRequest, book_id: int):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        "title": book.title,
    }
    return render(request, template_name="bookshop/detail.html", context=context)