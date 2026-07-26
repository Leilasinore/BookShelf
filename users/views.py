import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Author, Book, Category, Profile, Publisher
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    CategorySerializer,
    ProfileSerializer,
    PublisherSerializer,
)

logger = logging.getLogger(__name__)


# =====================================================
# BOOKS
# =====================================================

class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "author",
        "publisher",
        "categories",
    ]

    search_fields = [
        "title",
        "description",
        "author__first_name",
        "author__last_name",
        "publisher__name",
    ]

    ordering_fields = [
        "price",
        "published_date",
        "created_at",
    ]

    def get_queryset(self):
        logger.info(
            "Fetching books | user=%s | query_params=%s",
            self.request.user,
            dict(self.request.query_params),
        )
        return super().get_queryset()

    def perform_create(self, serializer):
        book = serializer.save()

        logger.info(
            "Book created | id=%s | title=%s | author=%s | user=%s",
            book.id,
            book.title,
            book.author,
            self.request.user,
        )


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        book = serializer.save()

        logger.info(
            "Book updated | id=%s | title=%s | user=%s",
            book.id,
            book.title,
            self.request.user,
        )

    def perform_destroy(self, instance):
        logger.info(
            "Book deleted | id=%s | title=%s | user=%s",
            instance.id,
            instance.title,
            self.request.user,
        )

        instance.delete()


# =====================================================
# PROFILES
# =====================================================

class ProfileListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        logger.info(
            "Fetching profiles | user=%s | query_params=%s",
            self.request.user,
            dict(self.request.query_params),
        )
        return super().get_queryset()

    def perform_create(self, serializer):
        profile = serializer.save()

        logger.info(
            "Profile created | id=%s | email=%s | user=%s",
            profile.id,
            profile.email,
            self.request.user,
        )


class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_update(self, serializer):
        profile = serializer.save()

        logger.info(
            "Profile updated | id=%s | email=%s | user=%s",
            profile.id,
            profile.email,
            self.request.user,
        )

    def perform_destroy(self, instance):
        logger.info(
            "Profile deleted | id=%s | email=%s | user=%s",
            instance.id,
            instance.email,
            self.request.user,
        )

        instance.delete()


# =====================================================
# AUTHORS
# =====================================================

class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        logger.info(
            "Fetching authors | user=%s | query_params=%s",
            self.request.user,
            dict(self.request.query_params),
        )
        return super().get_queryset()

    def perform_create(self, serializer):
        author = serializer.save()

        logger.info(
            "Author created | id=%s | name=%s %s | user=%s",
            author.id,
            author.first_name,
            author.last_name,
            self.request.user,
        )


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_update(self, serializer):
        author = serializer.save()

        logger.info(
            "Author updated | id=%s | name=%s %s | user=%s",
            author.id,
            author.first_name,
            author.last_name,
            self.request.user,
        )

    def perform_destroy(self, instance):
        logger.info(
            "Author deleted | id=%s | name=%s %s | user=%s",
            instance.id,
            instance.first_name,
            instance.last_name,
            self.request.user,
        )

        instance.delete()


# =====================================================
# PUBLISHERS
# =====================================================

class PublisherListAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_queryset(self):
        logger.info(
            "Fetching publishers | user=%s | query_params=%s",
            self.request.user,
            dict(self.request.query_params),
        )
        return super().get_queryset()

    def perform_create(self, serializer):
        publisher = serializer.save()

        logger.info(
            "Publisher created | id=%s | name=%s | user=%s",
            publisher.id,
            publisher.name,
            self.request.user,
        )


class PublisherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def perform_update(self, serializer):
        publisher = serializer.save()

        logger.info(
            "Publisher updated | id=%s | name=%s | user=%s",
            publisher.id,
            publisher.name,
            self.request.user,
        )

    def perform_destroy(self, instance):
        logger.info(
            "Publisher deleted | id=%s | name=%s | user=%s",
            instance.id,
            instance.name,
            self.request.user,
        )

        instance.delete()


# =====================================================
# CATEGORIES
# =====================================================

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        logger.info(
            "Fetching categories | user=%s | query_params=%s",
            self.request.user,
            dict(self.request.query_params),
        )
        return super().get_queryset()

    def perform_create(self, serializer):
        category = serializer.save()

        logger.info(
            "Category created | id=%s | name=%s | user=%s",
            category.id,
            category.name,
            self.request.user,
        )


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_update(self, serializer):
        category = serializer.save()

        logger.info(
            "Category updated | id=%s | name=%s | user=%s",
            category.id,
            category.name,
            self.request.user,
        )

    def perform_destroy(self, instance):
        logger.info(
            "Category deleted | id=%s | name=%s | user=%s",
            instance.id,
            instance.name,
            self.request.user,
        )

        instance.delete()