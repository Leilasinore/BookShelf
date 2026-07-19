from rest_framework import generics
from .models import Book, Profile,Publisher,Category,Author
from .serializers import BookSerializer, ProfileSerializer,PublisherSerializer,CategorySerializer,AuthorSerializer


# -------------------------
# BOOKS
# -------------------------

class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


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