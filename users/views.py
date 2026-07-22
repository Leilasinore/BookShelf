from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from .models import Book, Profile,Publisher,Category,Author
from .serializers import BookSerializer, ProfileSerializer,PublisherSerializer,CategorySerializer,AuthorSerializer
import logging

logger = logging.getLogger(__name__)

# -------------------------
# BOOKS
# -------------------------

class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def get_queryset(self):
     logger.info(
        "Fetching books | user=%s | query_params=%s",
        self.request.user,
        dict(self.request.query_params),
    )

     return Book.objects.all()

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
    def perform_create(self, serializer):
      book = serializer.save()

      logger.info(
        "Book created | id=%s | title=%s",
        book.id,
        book.title,
    )
    


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# -------------------------
# PROFILES
# -------------------------

class ProfileListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# -------------------------
# Publisher
# -------------------------

class PublisherListAPIView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Publisher.objects.all()
     serializer_class = PublisherSerializer

# -------------------------
# Category
# -------------------------

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# -------------------------
# Author
# -------------------------

class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer