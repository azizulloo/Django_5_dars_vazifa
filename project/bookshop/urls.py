from django.urls import path
from .views import index, genre_by_book, book_detail

urlpatterns = [
    path('', index, name='home'),
    path('genre/<int:genre_id>/', genre_by_book, name="by_genre"),
    path('book/<int:book_id>/', book_detail, name="detail")
]