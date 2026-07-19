from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Profile
from .serializers import BookSerializer, ProfileSerializer


class BookListAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class BookDetailAPIView(APIView):

    def get(self, request, pk):

        try:
            book = Book.objects.get(id=pk)

        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookSerializer(book)

        return Response(serializer.data)

    def put(self, request, pk):

        try:
            book = Book.objects.get(id=pk)

        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        try:
            book = Book.objects.get(id=pk)

        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        book.delete()

        return Response(
            {"message": "Book deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
class ProfileListAPIView(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class ProfileDetailAPIView(APIView):

    def get(self, request, pk):

        try:
            profile = Profile.objects.get(id=pk)

        except Profile.DoesNotExist:
            return Response(
                {"error": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProfileSerializer(profile)

        return Response(serializer.data)

    def put(self, request, pk):

        try:
            profile = Profile.objects.get(id=pk)

        except Profile.DoesNotExist:
            return Response(
                {"error": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        try:
            profile = Profile.objects.get(id=pk)

        except Profile.DoesNotExist:
            return Response(
                {"error": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        profile.delete()

        return Response(
            {"message": "Profile deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
