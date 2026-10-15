from django.urls import path
from . import views

urlpatterns = [
    # ======================================
    # Previous Labs - Keep Existing URLs
    # ======================================

    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),

    # ======================================
    # Lab 4 - HTML and CSS Pages
    # ======================================

    # Home page
    path('lab4/', views.lab4_index, name='books.index'),

    # List of books
    path('lab4/list_books/', views.lab4_list_books, name='books.list_books'),

    # One book details
    path('lab4/<int:bookId>/', views.lab4_viewbook, name='books.view_one_book'),

    # About Us page
    path('lab4/aboutus/', views.lab4_aboutus, name='books.aboutus'),
]