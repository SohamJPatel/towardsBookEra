from django.shortcuts import render
from .models import Book
from .models import Order
import json


def get_all_books(request):
    book_list = []
    books = Book.objects.none()

    if request.method == 'POST':

        crm = request.POST.get('CRM')
        adn = request.POST.get('ADN')
        edu = request.POST.get('EDU')
        bgr = request.POST.get('BGR')
        fic = request.POST.get('FIC')
        mot = request.POST.get('MOT')

        if crm:
            books = Book.objects.filter(book_category="CRM")
        if adn:
            books = books | Book.objects.filter(book_category="ADN")
        if edu:
            books = books | Book.objects.filter(book_category="EDU")
        if bgr:
            books = books | Book.objects.filter(book_category="BGR")
        if fic:
            books = books | Book.objects.filter(book_category="FIC")
        if mot:
            books = books | Book.objects.filter(book_category="MOT")

        print(books)
        

        if not (request.POST.get('txtMin') == "" and request.POST.get('txtMin') == ""):
            min = request.POST.get('txtMin')
            max = request.POST.get('txtMax')
            if(len(books)>0):
                books = books.filter(book_price__range=(min, max))
            else:
                books = Book.objects.filter(book_price__range=(min, max))
            
            print(books)

        searchby = request.POST.get('rbtnSearchBy')
        
        print(searchby)

        if searchby == 'book_name':
            searchkey = request.POST.get('txtSearchName')
            if(len(books)>0):
                books = books.filter(book_name=searchkey)
            else:
                books = Book.objects.filter(book_name=searchkey)

            #books = Book.objects.filter(book_name=searchkey)
            print(books)

        if searchby == 'author_name':
            searchkey = request.POST.get('txtSearchAuthor')
            if(len(books)>0):
                #books = Book.objects.filter(author_name=searchkey)
                books = books.filter(author_name=searchkey)
            else:
                books = Book.objects.filter(author_name=searchkey)
                
            print(books)

        #book_list = list(books)

        context = {'books': books}

        return render(request, "Bookspage.html", context)

    books = Book.objects.all()
    book_list = list(books)
    context = {'books': book_list}
    return render(request, "Bookspage.html", context)


def bookview(request, book_id):
    book = Book.objects.filter(id=book_id)
    context = {'bookdata': book[0]}
    print(book)
    return render(request, "Book.html", context)


def checkout(request):
    if request.method == 'POST':
        address1 = request.POST.get('inputAddress1')
        address2 = request.POST.get('inputAddress2')
        city = request.POST.get('inputCity')
        state = request.POST.get('inputState')
        zip = request.POST.get('inputZip')
        order_total = request.POST.get('orderTotal')
        items_json = request.POST.get('itemsJson')
        user = request.user

        order = Order(address1=address1, address2=address2, city=city, state=state, zip=zip,
                      user_name=user.username, items_json=items_json, order_total=order_total)
        order.save()
        thank = True
        oid = order.id
        return render(request, 'checkout.html', {'thank': thank, 'oid': oid})

    return render(request, 'checkout.html')


def get_orders(request):
    context = {}
    orderList = Order.objects.filter(user_name=request.user.username)
    context = {'orderList': orderList}

    return render(request, 'orders.html', context)
