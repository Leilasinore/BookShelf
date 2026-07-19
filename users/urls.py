from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIView,
    ProfileListAPIView,
    ProfileDetailAPIView,
)

urlpatterns = [
    # Profile endpoints
    path(
        "profiles/",
        ProfileListAPIView.as_view(),
        name="profile-list"
    ),
    path(
        "profiles/<int:pk>/",
        ProfileDetailAPIView.as_view(),
        name="profile-detail"
    ),

    # Book endpoints
    path(
        "books/",
        BookListAPIView.as_view(),
        name="book-list"
    ),
    path(
        "books/<int:pk>/",
        BookDetailAPIView.as_view(),
        name="book-detail"
    ),
]