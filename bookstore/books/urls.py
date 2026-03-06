from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),

    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart, name='cart'),
    path('remove/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('buy-now/<int:book_id>/', views.buy_now, name='buy_now'),

    # NEW PAGES
    path('payment/', views.payment, name='payment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]