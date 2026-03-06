from django.shortcuts import render, redirect
from .models import Book


def book_list(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'books/book_list.html', {'books': books})


def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)

    cart = request.session.get('cart', [])

    cart.append(book.id)

    request.session['cart'] = cart

    return redirect('/')


def cart(request):
    cart = request.session.get('cart', [])

    books = Book.objects.filter(id__in=cart)

    total = 0
    for book in books:
        total += book.price

    return render(request, 'books/cart.html', {
        'books': books,
        'total': total
    })


def remove_from_cart(request, book_id):
    cart = request.session.get('cart', [])

    if book_id in cart:
        cart.remove(book_id)

    request.session['cart'] = cart

    return redirect('cart')


def buy_now(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, 'books/buy_now.html', {'book': book})


def payment(request):
    return render(request, 'books/payment.html')


def about(request):
    return render(request, 'books/about.html')


def contact(request):
    return render(request, 'books/contact.html')