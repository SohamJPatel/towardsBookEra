from django.shortcuts import render
from .models import Book
from .models import Order

def get_all_books(request):
    book_list = []
    books = []

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

        
        #book_list = list(books)

        context = {'books' : books}
        
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

def checkout(request):
    if request.method =='POST':
        address1 = request.POST.get('inputAddress1')
        address2 = request.POST.get('inputAddress2')
        city = request.POST.get('inputCity')
        state = request.POST.get('inputState')
        zip = request.POST.get('inputZip')
        order_total = request.POST.get('orderTotal')
        items_json = request.POST.get('itemsJson')
        user = request.user

        order = Order(address1=address1, address2=address2,city=city,state=state,zip=zip,user_name=user.username,items_json=items_json,order_total=order_total)
        order.save()
        thank = True
        oid = order.id
        return render(request,'checkout.html',{'thank':thank, 'oid':oid})


    return render(request,'checkout.html')

