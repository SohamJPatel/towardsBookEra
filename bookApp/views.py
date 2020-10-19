from django.shortcuts import render
from .models import Book


def get_all_books(request):
    book_list = []
    if request.method == 'POST':
        searchby = request.POST.get('rbtnSearchBy')
        print(searchby)

        if searchby == 'book_name':
            searchkey = request.POST.get('txtSearchName')
            books = Book.objects.filter(book_name=searchkey)
            print(searchby)

        if searchby == 'author_name':
            searchkey = request.POST.get('txtSearchAuthor')
            books = Book.objects.filter(author_name=searchkey)
            print(searchby)

        book_list = list(books)

        context = {'books' : book_list}
        return render(request, "Bookspage.html", context)

    books = Book.objects.all()
    book_list = list(books)
    context = {'books': book_list}
    return render(request, "Bookspage.html", context)

def bookview(request, book_id):
    book = Book.objects.filter(id=book_id)
    context = {'bookdata' : book[0]}
    print(book)
    return render(request, "Book.html", context)
