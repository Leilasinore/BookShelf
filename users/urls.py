from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailAPIView,
    ProfileListAPIView,
    ProfileDetailAPIView,
    AuthorListAPIView,AuthorDetailAPIView,CategoryListAPIView,CategoryDetailAPIView,PublisherListAPIView,PublisherDetailAPIView
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

     # Author endpoints
    path(
        "author/",
        AuthorListAPIView.as_view(),
        name="author-list"
    ),
    path(
        "author/<int:pk>/",
        AuthorDetailAPIView.as_view(),
        name="author-detail"
    ),

     # Publisher endpoints
    path(
        "publisher/",
        PublisherListAPIView.as_view(),
        name="publisher-list"
    ),
    path(
        "publisher/<int:pk>/",
        PublisherDetailAPIView.as_view(),
        name="publisher-detail"
    ),

     # Category endpoints
    path(
        "category/",
        CategoryListAPIView.as_view(),
        name="category-list"
    ),
    path(
        "category/<int:pk>/",
        CategoryDetailAPIView.as_view(),
        name="category-detail"
    ),
]