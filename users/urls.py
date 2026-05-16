from django.urls import path
from .views import create_book, delete_book, delete_profile, get_book, get_books, get_profile, get_profiles,create_profile, update_book, update_profile

urlpatterns = [
    path('', get_profiles),
    
    path('<int:pk>/', get_profile),

    path('create/', create_profile),

    path('update/<int:pk>/', update_profile),

    path('delete/<int:pk>/', delete_profile),

    # BOOK ROUTES
    path('books/', get_books),

    path('books/<int:pk>/', get_book),

    path('books/create/', create_book),

    path('books/update/<int:pk>/', update_book),

    path('books/delete/<int:pk>/', delete_book),
]