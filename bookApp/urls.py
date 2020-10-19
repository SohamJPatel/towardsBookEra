from django.urls import path, include
from . import views as book_view


urlpatterns = [
    path('', book_view.get_all_books, name="bookshopPath"),
    path('bookview/<int:book_id>', book_view.bookview, name="bookViewPath"),
]
